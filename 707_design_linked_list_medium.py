class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node


class MyLinkedList:
    """
    Description:
        Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
        Implement these functions in your linked list class:
            get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
            addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
            addAtTail(val) : Append a node of value val to the last element of the linked list.
            addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
            deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        cur_node = self.head
        for i in range(index):
            cur_node = cur_node.next_node
        return cur_node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next_node = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next_node is not None:
                cur_node = cur_node.next_node
            cur_node.next_node = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            cur_node = self.head
            for i in range(index - 1):
                cur_node = cur_node.next_node
            new_node = Node(val)
            new_node.next_node = cur_node.next_node
            cur_node.next_node = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        cur_node = self.head
        if index == 0:
            self.head = cur_node.next_node
        else:
            for i in range(index - 1):
                cur_node = cur_node.next_node
            cur_node.next_node = cur_node.next_node.next_node
        self.size -= 1
