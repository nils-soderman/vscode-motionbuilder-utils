""" Moudle to install Debugpy """

import subprocess
import tempfile
import sys
import os

MOBU_PYTHON_EXECUTABLE = os.path.join(os.path.dirname(sys.executable), "mobupy.exe")
VSCODE_MOBU_TEMPDIR = os.path.join(tempfile.gettempdir(), "VSCode-MotionBuilder-Utils")

# for Python 2 compatibility
try:
    ModuleNotFoundError
except NameError:
    ModuleNotFoundError = ImportError

def is_pip_installed():
    """ Check if pip is installed """
    try:
        import pip
    except ModuleNotFoundError:
        return False

    return True


def install_pip():
    """ 
    Install pip module 
    Returns the path to the installed pip module
    """
    try:
        import ensurepip
    except ModuleNotFoundError:
        print("ensurepip module not found, aborting installation of pip")
        return None

    temp_installation_dir = os.path.join(VSCODE_MOBU_TEMPDIR, "TempPipInstall")

    process = subprocess.Popen([MOBU_PYTHON_EXECUTABLE, "-m", "ensurepip", "--root", temp_installation_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print(stdout.decode())
    print(stderr.decode())

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
    """ 
    pip install the debugpy module 

    ### Parameters:
        - target: The target directory to install the module to 
    """
    args = ['"%s"' % MOBU_PYTHON_EXECUTABLE]

    # Make sure pip is installed
    if not is_pip_installed():
        print("Pip is not installed, installing pip module")
        pip_module_path = install_pip()
        if not pip_module_path:
            print("Failed to install pip")
            return False

        args.extend([pip_module_path])
    else:
        args.extend(("-m", "pip"))

    if sys.version_info.major == 2:
        package = "debugpy==1.5.1"
    else:
        package = "debugpy"

    args.extend(("install", package))
    if target:
        args.append('--target="%s"' % target)

    print("installing debugpy")

    process = subprocess.Popen(" ".join(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print(stdout.decode())
    print(stderr.decode())

    return process.returncode == 0


def main():
    ext_packages_dir = globals().get("ext_packages_dir")
    install_dir = os.path.join(ext_packages_dir, "Python%s%s" % (sys.version_info.major, sys.version_info.minor))

    if install_debugpy(install_dir):
        return globals().get("vsc_suceess_id")

    return False


print(main())  # Output is read by the VS Code extension
