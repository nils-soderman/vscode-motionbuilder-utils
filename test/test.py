"""
Module used for tesing various features.
To test a function select the code inside it and execute it.
"""

# pylint: disable=all
from pyfbsdk import *

cube = FBModelCube("TestCube")
cube.Show = True

print(__file__)
print(__name__)


def error():
    print("Hello World")
    print(1 / 0)


def large_output():
    for x in range(1000):
        print("Hello World")