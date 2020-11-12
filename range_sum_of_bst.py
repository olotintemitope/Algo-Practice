from binary_tree import Node


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum_up = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.value <= R:
                    sum_up += node.value
                if L < node.value:
                    stack.append(node.left)
                if node.value < R:
                    stack.append(node.right)

        return sum_up


root = Node(10)
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(7)
root.insert(0)
root.insert(18)

sol = Solution()
print(sol.rangeSumBST(root, 7, 15))
