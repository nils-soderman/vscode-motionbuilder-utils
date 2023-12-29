"""
Reloads all imported modules that are not standard library modules
"""
import importlib
import time
import glob
import sys
import os
import site


def main():
    start_time = time.perf_counter()
    reloaded_paths = []

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

        try:
            importlib.reload(variable)
            reloaded_paths.append(filepath)
        except Exception as e:
            pass

    elapsed_time = time.perf_counter() - start_time
    reloaded_paths_str = ",".join(reloaded_paths)
    print(f"{len(reloaded_paths)},{elapsed_time:.2f}-{reloaded_paths_str}")

main()
