from itertools import combinations


class Solution:
    def combine(self, n: int, k: int):
        all_combinations = []
        for elem in combinations(range(1, n + 1), k):
            all_combinations.append(list(elem))
        return all_combinations


print(Solution().combine(1, 1))
