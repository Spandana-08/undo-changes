def fun():
    def wrapper():
        print("Inside wrapper function")
        return wrapper
    return wrapper
fun()()