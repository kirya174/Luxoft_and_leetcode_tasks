from io import UnsupportedOperation

class Time:
    def __init__(self,t):
        self.__time = t
    def __format__(self,spec):
        if spec == 'h':
            return f"{self.__time / 60 / 60}h"
        elif spec == 's':
            return f"{self.__time}s"
        elif spec == 'min':
            return f"{self.__time / 60}m"
        else:
            raise UnsupportedOperation("unsupported flag format")
    def __str__(self):
        return f"time is {self.__time} second(s)"

hour = Time(3600)
minute = Time(60)
second = Time(20)

print(f" time is {hour:h}")
print(f" time is {minute:min}")
print(f" time is {second:s}")
print(hour)