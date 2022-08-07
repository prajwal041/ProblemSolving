def supress_errors(func):
    try:
        print("In try block")
    except:
        print("Suppressing excpet")
        pass
    return

@supress_errors
def fn(): raise Exception("...")

