def announce(f):
    def wrapper():
        print("about to run the fucntion")
        f()
        print("after run the function")
    return wrapper


@announce
def hello():
    print("Hello world!")


hello()  