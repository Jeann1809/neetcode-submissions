class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr_len = len(s)
        max_s = 0
        temp = set()
        l, r = 0, 0

        while r < arr_len:
            if s[r] in temp:
                temp.remove(s[l])
                l += 1
            else:
                temp.add(s[r])
                length = r - l + 1
                max_s = max(max_s, length)
                r += 1
        return max_s