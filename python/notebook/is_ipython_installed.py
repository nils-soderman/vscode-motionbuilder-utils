""" 
Check if IPython is installed
"""

def main():
    try:
        import IPython
        return globals().get("vsc_suceess_id")
    except ModuleNotFoundError:
        pass

    return False


print(main())