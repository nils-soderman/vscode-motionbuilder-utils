""" 
Check if IPython is installed
"""

def main():
    print("ok")
    print("lkets go")
    try:
        import IPython
        return globals().get("vsc_suceess_id")
    except ModuleNotFoundError:
        pass

    return False


print(main())