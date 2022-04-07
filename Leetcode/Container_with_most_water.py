import time


class Solution:
    def maxArea(self, height) -> int:
        max_vol = 0
        # slow solution
        # for i in range(len(height)):
        #     for j in range(i, len(height)):
        #         if min(height[i], height[j]) * (j-i) > max_vol:
        #             max_vol = min(height[i], height[j]) * (j-i)
        # return max_vol

        i = 0
        j = len(height)-1
        while True:
            if i == j:
                break
            elif min(height[i], height[j]) * (j-i) > max_vol:
                max_vol = min(height[i], height[j]) * (j - i)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_vol


if __name__ == '__main__':
    inputs_list = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1],
        [2, 2, 5, 1, 3]
    ]
    for lst in inputs_list:
        start_time = time.time()
        print(Solution().maxArea(lst))
        print("--- %s seconds ---" % (time.time() - start_time))