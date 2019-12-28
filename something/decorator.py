def my_decorator(foo):
    def wrapper(arg):
        if arg:
            foo(arg)
        else:
            print('Sorry, no functions on my watch')
    return wrapper

@my_decorator
def func(argument):
    print("I am a function, YaaaY")


if __name__ == '__main__':
    func(False)
