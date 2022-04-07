# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version == 1:
        return True


import math

min_n = 0
# mid_n = n//2
max_n = 1
while True:
    mid_n = math.ceil((max_n + min_n) / 2)
    if isBadVersion(mid_n):
        if isBadVersion(mid_n - 1):
            max_n = mid_n
        else:
            print(mid_n)
    else:
        min_n = mid_n
