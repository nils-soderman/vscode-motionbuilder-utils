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


EXCLUDE_MODULES = [
    "signature_bootstrap.py"
]


def main():
    start_time = time.perf_counter()

    info_reloaded_paths: list[str] = []
    info_failed_paths: list[str] = []

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

        if filepath in EXCLUDE_MODULES:
            continue

        start_time_module_reload = time.perf_counter()
        try:
            importlib.reload(variable)
        except Exception as e:
            info_failed_paths.append(filepath)
            continue

        elapsed_time_module_reload_ms = (time.perf_counter() - start_time_module_reload) * 1000
        info_reloaded_paths.append(
            f"{elapsed_time_module_reload_ms:.2f}-{filepath}"
        )

    elapsed_time_ms = int((time.perf_counter() - start_time) * 1000)

    data: list[str] = [
        str(elapsed_time_ms),
        ",".join(info_reloaded_paths),
        ",".join(info_failed_paths),
    ]

    print("|".join(data))


main()
