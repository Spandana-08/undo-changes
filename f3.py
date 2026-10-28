def decorator(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper
@decorator
def display():
    print("Hello, World!")
display()