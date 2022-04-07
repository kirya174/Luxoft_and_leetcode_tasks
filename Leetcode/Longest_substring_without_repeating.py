class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        longest_substr = []
        for char in s:
            if char not in longest_substr:
                longest_substr.append(char)
                if len(longest_substr) > max_length:
                    max_length = len(longest_substr)
            else:
                index = longest_substr.index(char)
                longest_substr = longest_substr[index + 1:]
                longest_substr.append(char)
        return max_length


if __name__ == '__main__':
    s = [
        "aab",
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        
    ]
    for test_data in s:
        print(Solution().lengthOfLongestSubstring(test_data))
