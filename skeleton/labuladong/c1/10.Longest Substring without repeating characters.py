class Solution:
    """
    Given a string s, find the length of the longest
    substring
     without repeating characters.



    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


    Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
    """

    def lengthOfLongestSubstring(self, s):
        """
        :param s:
        :return: int
        """
        def check_repeat(_window):
            for k, v in _window.items():
                if v > 1:
                    return True
            return False

        result = 0
        l, r = 0, -1
        window = {}

        while r < len(s) - 1:
            r += 1

            c = s[r]
            window[c] = window.get(c, 0) + 1

            while l <= r and check_repeat(window) > 0:
                c = s[l]
                window[c] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result


if __name__ == '__main__':
    ans = Solution().lengthOfLongestSubstring("abcabcbb")
    print(ans)
