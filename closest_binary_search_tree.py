from binary_tree import Node


def closest_binary_search_tree(node: Node, target):
    """
        4
       / \
      2   5
     / \
    1   3
    :return:
    """
    # rounded_target = round(target)
    closest = node.value

    while node:
        closest = min(node.value, closest, key=lambda x: abs(target - x))
        node = node.left if target < node.value else node.right
    return closest


root = Node(4)
root.insert(2)
root.insert(5)
root.insert(1)
root.insert(3)

print(closest_binary_search_tree(root, 3.414286))
