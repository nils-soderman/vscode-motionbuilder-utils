import pyfbsdk

def version() -> int:
    return int(pyfbsdk.FBSystem().Version) // 1000 + 2000
