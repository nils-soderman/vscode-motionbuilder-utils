"""
This script will generate a 'pyfbsdk.py' stub file under resources/stub-files/...
Script must be executed within the MotionBuilder version that the stub file should be generated for.
"""
import pyfbsdk

import sys
import os

from importlib import reload


CURRENT_DIRECTORY = os.path.dirname(__file__)
STUB_FILE_DIR = os.path.join(CURRENT_DIRECTORY, "..", "..", "resources", "stub-files")


def GetMotionBuilderVersion():
    """ Get the current version of MotionBuilder """
    return int(2000 + pyfbsdk.FBSystem().Version / 1000)


def main():
    # Add site-packages to path (must be done before importing the 'pyfbsdk_stub_generator' module)
    SitePackagesFolder = os.path.join(CURRENT_DIRECTORY, "site-packages")
    if not os.path.isdir(SitePackagesFolder):
        raise Exception(f"Required site-packages has not been installed! Run the update-python-required.bat")

    if SitePackagesFolder not in sys.path:
        sys.path.append(SitePackagesFolder)

    # Import the stub generator module
    import pyfbsdk_stub_generator as mobuStubGenerator
    reload(mobuStubGenerator)

    # Generate the stub file
    OutputDir = os.path.join(STUB_FILE_DIR, GetMotionBuilderVersion())
    mobuStubGenerator.Generate(OutputDir, FileExtension = "py")


if "builtin" in __name__:
    main()
