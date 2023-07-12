""" Moudle to install Debugpy """

import subprocess
import tempfile
import sys
import os

MOBU_PYTHON_EXECUTABLE = os.path.join(os.path.dirname(sys.executable), "mobupy.exe")
VSCODE_MOBU_TEMPDIR = os.path.join(tempfile.gettempdir(), "VSCode-MotionBuilder-Utils")


def is_pip_installed():
    try:
        import pip
    except ModuleNotFoundError:
        return False

    return True


def install_pip():
    try:
        import ensurepip
    except ModuleNotFoundError:
        return None

    temp_installation_dir = os.path.join(VSCODE_MOBU_TEMPDIR, "TempPipInstall")
    subprocess.check_call([MOBU_PYTHON_EXECUTABLE, "-m", "ensurepip", "--root", temp_installation_dir])

    # Find the pip module path
    pip_module_path = ""
    for root, directory, files in os.walk(temp_installation_dir):
        if "__init__.py" in files and os.path.basename(root) == "pip":
            pip_module_path = os.path.join(root)
            break
    else:
        return None

    return pip_module_path


def install_debugpy(target=""):
    args = [MOBU_PYTHON_EXECUTABLE]

    # Make sure pip is installed
    if not is_pip_installed():
        pip_module_path = install_pip()
        if not pip_module_path:
            return False

        args.extend([pip_module_path])
    else:
        args.extend(("-m", "pip"))

    args.extend(("install", "debugpy"))
    if target:
        args.append(f'--target="{target}"')

    subprocess.call(args)

    # Check if installation was sucessfull by trying to import debugpy
    try:
        import debugpy
    except ModuleNotFoundError:
        return False

    return True


def main():
    ext_packages_dir = globals().get("ext_packages_dir")
    install_dir = os.path.join(ext_packages_dir, "Python%s%s" % (sys.version_info.major, sys.version_info.minor))
    success = install_debugpy(install_dir)

    # Output is read by the VS Code extension
    print(success)


main()
