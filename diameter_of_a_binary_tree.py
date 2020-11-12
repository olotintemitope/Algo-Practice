from binary_tree import Node


class Solution:
    def diameterOfBinaryTree(self, root: Node) -> int:
        node = root
        self.diameter = 0

        def depth(node):
            if not node:
                return 0

            left_height = depth(node.left)
            right_height = depth(node.right)
            # path
            self.diameter = max(self.diameter,  left_height + right_height)
            # depth
            return max(right_height, left_height) + 1

        depth(node)

        return self.diameter


root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)

sol = Solution()
print(sol.diameterOfBinaryTree(root))
