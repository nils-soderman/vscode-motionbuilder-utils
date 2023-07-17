import sys
import os


VSCODE_DEBUG_SERVER_ENV_VAR = "vscode_debugpy_server_port"
MOBU_PYTHON_EXECUTABLE = os.path.join(os.path.dirname(sys.executable), "mobupy.exe")


def start_debug_server(port, debugpy_install_dir=""):
    try:
        import debugpy
    except ModuleNotFoundError:
        # Retry with the debugpy_install_dir added to sys.path
        if debugpy_install_dir:
            sys.path.append(debugpy_install_dir)
            try:
                import debugpy
            except ModuleNotFoundError:
                return False

    debugpy.configure(python=MOBU_PYTHON_EXECUTABLE)
    debugpy.listen(port)

    os.environ[VSCODE_DEBUG_SERVER_ENV_VAR] = str(port)

    return True


def main():
    port = globals().get("port")

    ext_packages_dir = globals().get("ext_packages_dir")
    debugpy_install_dir = os.path.join(ext_packages_dir, "Python%s%s" %
                                       (sys.version_info.major, sys.version_info.minor))

    is_server_running = start_debug_server(port, debugpy_install_dir)

    return is_server_running


print(main())  # output is read by the VSCode extension
