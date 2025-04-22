import pyfbsdk

def version():
    return int(pyfbsdk.FBSystem().Version) // 1000 + 2000
