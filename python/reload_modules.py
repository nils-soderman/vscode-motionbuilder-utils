"""
Reloads all imported modules that are not standard library modules
"""

import importlib
import traceback
import time
import sys
import os


def reload(workspace_folders):
    start_time = time.perf_counter()

    num_reloads = 0
    num_failed = 0

    workspace_folders = [os.path.normpath(folder).lower() for folder in workspace_folders]

    for variable in list(sys.modules.values()):
        # Check if variable is a module
        if not hasattr(variable, '__file__') or not variable.__file__:
            continue

        filepath = variable.__file__.lower()

        if not any(filepath.startswith(x) for x in workspace_folders):
            continue

        try:
            importlib.reload(variable)
        except Exception as e:
            print('Failed to reload "%s":\n%s' % (filepath, traceback.format_exc()))
            num_failed += 1
            continue

        num_reloads += 1

    elapsed_time_ms = int((time.perf_counter() - start_time) * 1000)

    print("Reloaded %s modules in %sms" %(num_reloads, elapsed_time_ms))

    return {"num_reloads": num_reloads, "time": elapsed_time_ms, "num_failed": num_failed}
