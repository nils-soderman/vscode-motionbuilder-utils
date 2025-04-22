import subprocess
import tempfile
import sys
import os

VSCODE_DEBUG_SERVER_ENV_VAR = "vscode_debugpy_server_port"
MOBU_PYTHON_EXECUTABLE = os.path.join(os.path.dirname(sys.executable), "mobupy.exe")
VSCODE_MOBU_TEMPDIR = os.path.join(tempfile.gettempdir(), "VSCode-MotionBuilder-Utils")



def is_debugpy_installed() -> bool:
    """
    Tries to import debugpy to check if it is installed.
    """
    try:
        import debugpy
        return True
    except ModuleNotFoundError:
        return False
    
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

    process = subprocess.Popen([MOBU_PYTHON_EXECUTABLE, "-m", "ensurepip", "--root",
                               temp_installation_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        stdout, stderr = process.communicate()
        print(stdout.decode())
        print(stderr.decode())
    finally:
        if process.stdout:
            process.stdout.close()
        if process.stderr:
            process.stderr.close()
        process.wait()

    # Find the pip module path
    pip_module_path = ""
    for root, directory, files in os.walk(temp_installation_dir):
        if "__init__.py" in files and os.path.basename(root) == "pip":
            pip_module_path = os.path.join(root)
            break
    else:
        return None

    return pip_module_path


def install_debugpy() -> bool:
    """
    Installs debugpy using the current Unreal Python interpreter.
    """
    debugpy_install_args = [MOBU_PYTHON_EXECUTABLE]

    if not is_pip_installed():
        print("Pip is not installed, installing pip module")
        pip_module_path = install_pip()
        if not pip_module_path:
            print("Failed to install pip")
            return False

        debugpy_install_args.append(pip_module_path)
    else:
        debugpy_install_args.extend(("-m", "pip"))

    debugpy_install_args.extend(("install", "-q", "--no-warn-script-location", "debugpy"))

    try:
        result = subprocess.run(debugpy_install_args, capture_output=True, check=True, text=True)
        print(result.stdout)
        print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install debugpy: {e}")
        print(e.stdout)
        print(e.stderr)
    except Exception as e:
        print(f"Failed to install debugpy: {e}")

    # Make sure the installation was successful by trying to import debugpy
    import debugpy

    return True


def start_debugpy_server(port: int) -> bool:
    """ Starts a debugpy server on the specified port """
    import debugpy

    debugpy.configure(python=MOBU_PYTHON_EXECUTABLE)
    debugpy.listen(port)

    os.environ[VSCODE_DEBUG_SERVER_ENV_VAR] = str(port)

    return True


def get_current_debugpy_port() -> int:
    """ Returns the current debugpy server port or -1 if it is not set """
    return int(os.environ.get(VSCODE_DEBUG_SERVER_ENV_VAR, -1))