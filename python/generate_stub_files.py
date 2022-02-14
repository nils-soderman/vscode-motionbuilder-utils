import sys
import os

from importlib import reload

sys.path.append(os.path.dirname(__file__))

import pyfbsdk_stub_generator.generate_motionbuilder_stubs as mobuStubGenerator
reload(mobuStubGenerator)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "stub-files")


def main():
    # Make sure output dir exists
    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Generate the stub files
    mobuStubGenerator.GeneratePyfbsdkStub(OUTPUT_DIR)


if "builtin" in __name__:
    main()
