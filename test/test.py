# pylint: disable=all
from pyfbsdk import *

cube = FBModelCube("TestCube")
cube.Show = True

print(__file__)
print(__name__)


def error():
    print("Hello World")
    print(1 / 0)
