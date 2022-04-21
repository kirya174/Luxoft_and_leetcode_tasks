class MyMainException(Exception):
    pass

class SubException(MyMainException):
    pass

def make_error(x):
    if x > 5:
        raise SubException()
    return x + 2
# v1
try:
    print(make_error(4))
    print(make_error(6))
    print(make_error(2))
except MyMainException:
    print("catch MyMainException")
except SubException:
    print("catch SubException")
    
# v2
try:
    print(make_error(4))
    print(make_error(6))
    print(make_error(2))
except SubException:
    print("catch SubException")
except MyMainException:
    print("catch MyMainException")
    