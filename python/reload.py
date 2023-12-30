"""
Reloads all imported modules that are not standard library modules
"""
from __future__ import annotations

import importlib
import time
import glob
import sys
import os
import site


def main():
    start_time = time.perf_counter()
    reloaded_paths: list[tuple[str, str]] = []

    glob_patterns = globals().get("vsc_reload_ignore", [])

    mobu_installation_dir = os.path.dirname(os.path.dirname(sys.executable))
    site_packages = site.getsitepackages()

    for variable in list(sys.modules.values()):
        # Check if variable is a module
        if not hasattr(variable, '__file__') or not variable.__file__:
            continue

        filepath = variable.__file__

        # Check if the module resides in the Mobu installation directory
        if filepath.startswith(mobu_installation_dir):
            continue

        # Check if the module is a site-package
        if any(filepath.startswith(path) for path in site_packages):
            continue

        # Exclude custom glob patterns
        if any(glob.fnmatch.fnmatch(filepath, pattern) for pattern in glob_patterns):
            continue

        start_time_module_reload = time.perf_counter()
        try:
            importlib.reload(variable)
        except Exception as e:
            pass

        elapsed_time_module_reload = time.perf_counter() - start_time_module_reload
        reloaded_paths.append((f"{elapsed_time_module_reload * 1000:.2f}", f"| {filepath}"))

    padding = max(len(x[0]) for x in reloaded_paths)
    paths_table = [f"{reload_time:{padding}} ms {path}" for reload_time, path in reloaded_paths]

    elapsed_time = time.perf_counter() - start_time
    reloaded_paths_str = ",".join(paths_table)
    print(f"{len(reloaded_paths)},{elapsed_time:.2f}-{reloaded_paths_str}")

main()
