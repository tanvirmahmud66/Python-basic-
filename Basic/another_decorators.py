def decor(f):
    def wrapper():
        print("Hello Tanvir Mahmud Fahim")
        f()
        print("after run the function argument")
    return wrapper


@decor
def fahim():
    print("This is FAHIM")


fahim()