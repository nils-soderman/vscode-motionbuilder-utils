"""
Start a debugpy server on the given port.
"""
import sys
import os


VSCODE_DEBUG_SERVER_ENV_VAR = "vscode_debugpy_server_port"
MOBU_PYTHON_EXECUTABLE = os.path.join(os.path.dirname(sys.executable), "mobupy.exe")


def start_debug_server(port, debugpy_install_dir=""):
    try:
        import debugpy  # type: ignore
    except ModuleNotFoundError:
        # Retry with the debugpy_install_dir added to sys.path
        if debugpy_install_dir:
            # Add an extra forwardslash to the path to make it a "new" directory.
            # Otherwise because we may have added this dir in is_debugpy_installed.py,
            # it won't be re-scannedand debugpy won't be found.
            debugpy_install_dir = debugpy_install_dir + "/"
            sys.path.append(debugpy_install_dir)
            try:
                import debugpy  # type: ignore
            except ModuleNotFoundError:
                return False

    debugpy.configure(python=MOBU_PYTHON_EXECUTABLE)
    debugpy.listen(port)

    os.environ[VSCODE_DEBUG_SERVER_ENV_VAR] = str(port)

    return True


def main():
    port = globals().get("vsc_port")

    vsc_target = globals().get("vsc_target")
    debugpy_install_dir = os.path.join(vsc_target, "Python%s%s" %
                                       (sys.version_info.major, sys.version_info.minor))

    is_server_running = start_debug_server(port, debugpy_install_dir)
    if not is_server_running:
        return "Failed to start debugpy server"

    return globals().get("vsc_suceess_id")


print(main())  # output is read by the VSCode extension
