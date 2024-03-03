class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        cur = self.head
        i = 0

        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next

        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            return

        tempNode = self.head
        while tempNode.next:
            tempNode = tempNode.next
        tempNode.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        count = 0
        node = Node(val)
        tempNode = self.head

        while tempNode:
            if count == index - 1:
                node.next = tempNode.next
                tempNode.next = node
                break
            tempNode = tempNode.next
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
            return

        count = 0
        tempNode = self.head

        while tempNode:
            if count == index - 1 and tempNode.next:
                tempNode.next = tempNode.next.next
                break
            tempNode = tempNode.next
            count += 1