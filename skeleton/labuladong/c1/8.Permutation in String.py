class Solution:
    """
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of s2.



    Example 1:

    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").
    Example 2:

    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false


    Constraints:

    1 <= s1.length, s2.length <= 104
    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters
    """

    def checkInclusion(self, s1, s2):
        if len(s2) < len(s1):
            return False

        hash_c = {}
        for s in s1:
            hash_c[s] = hash_c.get(s, 0) + 1

        count = 0
        window_count = {}
        l, r = 0, -1
        while r < len(s2) - 1:
            r += 1

            r_c = s2[r]
            window_count[r_c] = window_count.get(r_c, 0) + 1

            if r_c in hash_c and window_count[r_c] == hash_c[r_c]:
                count += 1

            print(window_count)

            if count == len(hash_c):
                return True

            l_c = s2[l]
            if r - l + 1 == len(s1):
                window_count[l_c] -= 1
                if l_c in hash_c and window_count[l_c] != hash_c[l_c]:
                    count -= 1

                l += 1

        return False


if __name__ == '__main__':
    ans = Solution().checkInclusion("ab", "eidbaooo")
    print(ans)

    ans = Solution().checkInclusion("ab", "eidboaoo")
    print(ans)
