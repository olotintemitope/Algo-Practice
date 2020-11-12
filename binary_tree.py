class Node(object):
    summation = []

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)

            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)

        else:
            self.value = value

    def get_node_values(self):
        if self.left:
            self.left.get_node_values()
        self.summation.append(self.value)
        if self.right:
            self.right.get_node_values()

        return self.summation

    def find_a_value(self, value):
        if value < self.value:
            if self.left is None:
                return print("{} not found".format(value))
            return self.left.find_a_value(value)

        elif value > self.value:
            if self.right is None:
                return print("{} not found".format(value))
            return self.right.find_a_value(value)

        else:
            print(str(self.value) + ' is found')

    """ 
        Inorder traversal, you visit the left first, then
        the root and finally,
        the right
    """
    def in_order_traversal(self, root):
        sum_up = []
        if root:
            sum_up = self.in_order_traversal(root.left)
            sum_up.append(root.value)
            sum_up += self.in_order_traversal(root.right)

        return sum_up

    """ 
        Preorder traversal, you visit the root first, then
        the left and finally,
        the right
    """
    def pre_order_traversal(self, root):
        sum_up = []
        if root:
            sum_up.append(root.value)
            sum_up += self.in_order_traversal(root.left)
            sum_up += self.in_order_traversal(root.right)

        return sum_up

    """ 
        Postorder traversal, you visit the left first, then
        the right and finally,
        the root
    """
    def post_order_traversal(self, root):
        sum_up = []
        if root:
            sum_up = self.in_order_traversal(root.left)
            sum_up += self.in_order_traversal(root.right)
            sum_up.append(root.value)

        return sum_up


# root = Node(21)
# root.insert(4)
# root.insert(1)
# root.insert(4)
# root.insert(9)
# root.insert(3)
# root.insert(20)
# root.insert(25)
# root.insert(6)
# root.insert(21)
# root.insert(14)
#
# # values = root.get_node_values()
# # print(values)
#
# print(root.in_order_traversal(root))
# print(root.pre_order_traversal(root))
# print(root.post_order_traversal(root))
#
# # root.find_a_value(31)
