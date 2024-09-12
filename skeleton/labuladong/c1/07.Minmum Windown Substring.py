class Solution:
    """
    Example 1:

    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
    Example 2:

    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.
    Example 3:

    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.
    """

    def minWindow(self, s, t):
        hash_p = {}
        for tc in list(t):
            hash_p[tc] = hash_p.get(tc, 0) + 1

        min_len = float('inf')
        result = ""

        l, r = 0, 0
        window = {}
        count = 0
        while r < len(s):
            while r < len(s) and count != len(hash_p):
                print(s[l:r])
                c = s[r]
                window[c] = window.get(c, 0) + 1
                if c in hash_p and window[c] == hash_p[c]:
                    count += 1
                r += 1

            # match
            if r - l < min_len:
                min_len = r - l
                result = s[l: r]

            while l < len(s) and l < r and count == len(hash_p):
                print("收缩",s[l:r])
                if r - l < min_len:
                    min_len = r - l
                    result = s[l:r]
                c = s[l]
                window[c] = window[c] - 1
                if c in hash_p and window[c] == 0:
                    count -= 1
                l += 1

        return result


if __name__ == '__main__':
    ans = Solution().minWindow("ADOBECODEBANC", "ABC")
    print(ans)
