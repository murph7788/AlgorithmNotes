class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        res = float('inf')
        for c in coins:
            sub = self.coinChange(coins, amount - c)

            if sub == -1:
                continue

            res = min(res, 1 + sub)

        return res if res != float('inf') else -1


class Solution2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        mem = [-6666] * (amount + 1)
        return self.helper(coins, amount, mem)

    def helper(self, coins, amount, mem):
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        if mem[amount] != -6666:
            return mem[amount]

        res = float('inf')
        for c in coins:
            sub = self.helper(coins, amount - c, mem)

            if sub == -1:
                continue

            res = min(res, 1 + sub)
            mem[amount] = min(mem[amount], res)

        mem[amount] = res if res != float('inf') else -1

        return mem[amount]


class Solution3(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(len(dp)):
            for c in coins:
                if i - c < 0:
                    continue

                dp[i] = min(dp[i], 1 + dp[i - c])

        return dp[amount] if dp[amount] != amount + 1 else -1

