from Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def isEmpty(self):
        if self.head_node is None:
            return True
        return False

    def insert(self, data):
        new_node = Node(data)
        new_node.next_element = self.head_node
        self.head_node = new_node

        return self.head_node

    def print(self):
        if self.isEmpty():
            return "List is empty"
            return False

        node = self.head_node
        while node.next_element:
            print(node.data, end=" -> ")
            node = node.next_element
        print(node.data, "-> None")

        return True

    def insert_at_tail(self, value):
        if self.head_node is None:
            new_node = Node(value)
            self.head_node = new_node
            return

        node = self.head_node
        new_node = Node(value)
        while node.next_element:
            node = node.next_element
        node.next_element = new_node
        return


lnList = LinkedList()
lnList.insert(2)
lnList.insert(3)
lnList.insert(5)
lnList.insert_at_tail(7)
print(lnList.isEmpty())
print(lnList.print())
