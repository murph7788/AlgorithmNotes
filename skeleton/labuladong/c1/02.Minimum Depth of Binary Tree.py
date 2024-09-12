# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        l = self.minDepth(root.left)
        r = self.minDepth(root.right)

        if not root.left:
            return r + 1
        if not root.right:
            return l + 1

        return 1 + min(l, r)


class Solution2(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        layer = 0
        que = [root]
        while len(que):
            layer += 1
            for n in range(len(que)):
                c = que.pop(0)

                if not c.left and not c.right:
                    return layer
                if c.left:
                    que.append(c.left)
                if c.right:
                    que.append(c.right)

        return layer

