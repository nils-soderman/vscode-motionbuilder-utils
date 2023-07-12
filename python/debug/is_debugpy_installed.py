""" Module for checking if debugpy is installed """

import sys
import os


def is_debugpy_installed(extra_sys_path=""):
    try:
        import debugpy
        return True
    except ModuleNotFoundError:
        pass

    if extra_sys_path and extra_sys_path not in sys.path:
        sys.path.append(extra_sys_path)
        is_installed = False
        try:
            import debugpy
            is_installed = True
        except ModuleNotFoundError:
            pass

        sys.path.remove(extra_sys_path)
        return is_installed

    return False


def main():
    ext_packages_dir = globals().get("ext_packages_dir")
    debugpy_install_dir = os.path.join(ext_packages_dir, "Python%s%s" %(sys.version_info.major, sys.version_info.minor))
    installed = is_debugpy_installed(debugpy_install_dir)

    # output is sent back to VS Code
    print(installed)


main()
