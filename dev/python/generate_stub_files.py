"""
This script will generate a 'pyfbsdk.py' stub file under resources/stub-files/...
Script must be executed within the MotionBuilder version that the stub file should be generated for.
"""
import shutil
import sys
import os

from importlib import reload

import pyfbsdk


CURRENT_DIRECTORY = os.path.dirname(__file__)
STUB_FILE_DIR = os.path.join(CURRENT_DIRECTORY, "..", "..", "resources", "stub-files")


def get_motionbuilder_version():
    """ Get the current version of MotionBuilder """
    return int(2000 + pyfbsdk.FBSystem().Version / 1000)


def generate_pyfbsdk_stub(output_dir: str):
    # Import the stub generator module
    import pyfbsdk_stub_generator
    reload(pyfbsdk_stub_generator)
    pyfbsdk_stub_generator.Generate(output_dir)

    # Create an empty .py file
    with open(os.path.join(output_dir, "pyfbsdk.py"), "w+", encoding="utf-8") as file:
        pass


def copy_stub_files(output_dir: str) -> None:
    stub_src_dir = os.path.join(CURRENT_DIRECTORY, "stubs")
    for src_filename in os.listdir(stub_src_dir):
        if src_filename.endswith(".pyi"):
            output_file = os.path.join(output_dir, src_filename)
            shutil.copy(os.path.join(stub_src_dir, src_filename), output_file)

            # Create an empty .py file
            with open(output_file.replace(".pyi", ".py"), "w+", encoding="utf-8") as file:
                pass

            print(f"Copied stub file: {src_filename}")


def main():
    # Add site-packages to path (must be done before importing the 'pyfbsdk_stub_generator' module)
    site_packages_folder = os.path.join(CURRENT_DIRECTORY, "site-packages")
    if not os.path.isdir(site_packages_folder):
        raise ImportError("Required site-packages has not been installed! Run the update-python-required.bat")

    if site_packages_folder not in sys.path:
        sys.path.append(site_packages_folder)

    output_dir = os.path.join(STUB_FILE_DIR, str(get_motionbuilder_version()))
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    generate_pyfbsdk_stub(output_dir)
    copy_stub_files(output_dir)


if "builtin" in __name__:
    main()
