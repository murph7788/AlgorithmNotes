class Solution:
    """
    [1 , 2, 2, 3, 4, 5, 6]
    target == 2
    """

    def searchRange(self, nums, target):
        f = self.first(nums, target)
        l = self.last(nums, target)
        return [f, l]

    def first(self, nums, target):
        if not nums:
            return -1

        ans = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if target == nums[m]:
                ans = m
                r = m - 1
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        return ans

    def last(self, nums, target):
        if not nums:
            return -1

        ans = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if target == nums[m]:
                ans = m
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        return ans


if __name__ == '__main__':
    ans = Solution().searchRange([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 2)
    print(ans)
