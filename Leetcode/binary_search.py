nums = [-1, 0, 3, 5, 9, 12]
target = 12

left = 0
mid = len(nums) // 2
while True:
    if len(nums) <= 1 and nums[mid] != target:
        print(-1)
    elif nums[mid] == target:
        print(left + mid)
    elif nums[mid] > target:
        nums = nums[:mid]
        mid = len(nums) // 2
    elif nums[mid] < target:
        nums = nums[mid:]
        left += mid
        mid = len(nums) // 2
    else:
        print(-1)
