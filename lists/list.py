class SinglyLinkedNode():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class DoublyLinkedNode():
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = SinglyLinkedNode()
        self.size = 0

    def push_front(self, data):
        old_head = self.head
        new_head = SinglyLinkedNode(data)
        new_head.next = old_head
        self.head = new_head

    def push_back(self, data):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = SinglyLinkedNode(data)

    def insert_before(self, index):
        pass

    def insert_after(self, index):
        pass

    def remove(self, data):
        pass

class DoublyLinkedList():
    def __init__(self):
        self.head = DoublyLinkedNode()
        self.size = 0

    def push_front(self, data):
        pass

    def push_back(self, data):
        pass

    def insert_before(self, index):
        pass

    def insert_after(self, index):
        pass

    def remove(self, data):
        pass

