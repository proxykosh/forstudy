from functools import wraps

def func_dec(func):
    a = 1
    b = 1
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal a
        a += 1
        nonlocal b
        b += 2
        print("Begin")
        func(*args, **kwargs)
        print("Finish")
        return a,b
    return wrapper

@func_dec
def func(title):
    print("hello" + title)



print(func(" username"), func.__name__)

