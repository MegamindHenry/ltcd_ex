class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        pointer = 0
        c_set = set()
        for i in range(len(s)):
            c_set.add(s[i])
            if len(c_set) > max:
                max += 1
            else:
                pointer += 1
                c_set = set(s[pointer:pointer+max])
        return max


s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = ""

slt = Solution()
assert slt.lengthOfLongestSubstring(s1) == 3
assert slt.lengthOfLongestSubstring(s2) == 1
assert slt.lengthOfLongestSubstring(s3) == 3
assert slt.lengthOfLongestSubstring(s4) == 0