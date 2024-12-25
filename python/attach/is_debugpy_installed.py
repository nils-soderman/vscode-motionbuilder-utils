""" Module for checking if debugpy is installed """

import importlib
import sys
import os

# for Python 2 compatibility
try:
    ModuleNotFoundError
except NameError:
    ModuleNotFoundError = ImportError

def is_module_installed(module, extra_sys_path=""):
    try:
        importlib.import_module(module)
        return True
    except ModuleNotFoundError:
        pass

    if extra_sys_path and extra_sys_path not in sys.path:
        if os.path.isdir(extra_sys_path):
            sys.path.append(extra_sys_path)
            try:
                importlib.import_module(module)
                return True
            except ModuleNotFoundError:
                return False
            finally:
                sys.path.remove(extra_sys_path)

    return False


def main():
    vsc_target = globals().get("vsc_target")
    debugpy_install_dir = os.path.join(vsc_target, "Python%s%s" %(sys.version_info.major, sys.version_info.minor))
    installed = is_module_installed("debugpy", debugpy_install_dir)

    # output is sent back to VS Code
    if installed:
        return globals().get("vsc_suceess_id")

    return False

print(main())
