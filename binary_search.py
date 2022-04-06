# nums = [-1,0,3,5,9,12]
# target = 12
#
# left = 0
# mid = len(nums) // 2
# while True:
#     if len(nums) <= 1 and nums[mid] != target:
#         print(-1)
#     elif nums[mid] == target:
#         print(left + mid)
#     elif nums[mid] > target:
#         nums = nums[:mid]
#         mid = len(nums) // 2
#     elif nums[mid] < target:
#         nums = nums[mid:]
#         left += mid
#         mid = len(nums) // 2
#     else:
#         print(-1)

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
