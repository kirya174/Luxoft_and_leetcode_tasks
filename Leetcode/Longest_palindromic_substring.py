class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) > 1:
            longest_str = [s[0]]
            for i in range(len(s)):
                if s[i-1] == s[i]:
                    j = i - 1
                    k = i
                    while j >= 0 and k < len(s) and s[j] == s[k]:
                        j -= 1
                        k += 1
                    if len(s[j+1:k]) > len(longest_str):
                        longest_str = s[j+1:k]

                if s[i-2] == s[i]:
                    j = i - 2
                    k = i
                    while j >= 0 and k < len(s) and s[j] == s[k]:
                        j -= 1
                        k += 1
                    if len(s[j+1:k]) > len(longest_str):
                        longest_str = s[j+1:k]
            return ''.join(longest_str)
        else:
            return s


if __name__=='__main__':
    test_data = [
        "bb",
        "babad",
        "cbbd",
        "a",
        "",
        "ccc",
        "abcda",
    ]
    for s in test_data:
        print(Solution().longestPalindrome(s))
