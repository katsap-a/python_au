import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None



class MyLinkedList:

    def __init__(self):

        self.tail = None
        self.head = None
        self.len = 0
        self.counter = 0

    def get(self, index: int) -> int:

        if index >= self.len:
            return -1

        cur = self.head
        for i in range(index):
            cur = cur.next

        return (cur.val)

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.len += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val)
        if self.tail is None:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index is self.len:
            self.addAtTail(val)
        elif index is 0:
            self.addAtHead(val)
        elif index < self.len:
            newNode = Node(val)
            prev = self.head
            cur = self.head.next
            for i in range(1, index):
                prev = prev.next
                cur = cur.next  ##
            prev.next = newNode
            newNode.next = cur
            newNode.prev = prev
            cur.prev = newNode
            self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        if index is 0 and self.len is 1:
            self.head = None
            self.tail = None
            self.len -= 1

        elif index is 0:
            a = self.head.next
            a.prev = None
            self.head = a
            self.len -= 1

        elif index is (self.len - 1):
            a = self.tail.prev
            a.next = None
            self.tail = a
            self.len -= 1

        elif index < self.len and index > 0:
            n = 0
            cur = self.head
            while n is not index:
                n += 1
                cur = cur.next
            a = cur.prev
            b = cur.next
            a.next = b
            b.prev = a
            self.len -= 1

    def printList(self):
        a = self.head
        for i in range(self.len):
            print(a.val)
            a = a.next

    def __next__(self):

        if self.counter < self.len:
            self.counter += 1
            return self.get(self.counter - 1)
        else:
            raise StopIteration

    def __iter__(self):
        return self