""" Module for checking if debugpy is installed """

import importlib
import sys
import os


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
    ext_packages_dir = globals().get("ext_packages_dir")
    debugpy_install_dir = os.path.join(ext_packages_dir, "Python%s%s" %(sys.version_info.major, sys.version_info.minor))
    installed = is_module_installed("debugpy", debugpy_install_dir)

    # output is sent back to VS Code
    print(installed)


main()
