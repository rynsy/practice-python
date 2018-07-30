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
        self.size += 1

    def push_back(self, data):
        current = self.head
        if current.data == None:
            current.data = data
            return
        while current.next != None:
            current = current.next
        current.next = SinglyLinkedNode(data)
        self.size += 1

    def insert_before(self, index, data):
        if self.size < index:
            return -1
        current = self.head
        for i in range(index - 1):
            current = current.next
        newNode = SinglyLinkedNode(data)
        newNode.next = current.next
        current.next = newNode

    def insert_after(self, index, data):
        if self.size < index:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        newNode = SinglyLinkedNode(data)
        newNode.next = current.next
        current.next = newNode

    def remove(self, data):
        current = self.head
        previous = self.head
        num_deleted = 0
        for i in range(self.size):
            if current.data == data:
                if self.head == current:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                num_deleted += 1
            previous = current
            current = current.next
        return num_deleted
                
    def toString(self):
        current = self.head
        l = []
        while current != None:
            l.append(str(current.data))
            current = current.next
        return "[" + ",".join(l) + "]"

class DoublyLinkedList():
    # todo make this doubly linked.
    def __init__(self):
        self.head = DoublyLinkedNode()
        self.size = 0

    def push_front(self, data):
    # todo make this doubly linked.
        old_head = self.head
        new_head = DoublyLinkedNode(data)
        new_head.next = old_head
        self.head = new_head
        self.size += 1

    def push_back(self, data):
    # todo make this doubly linked.
        current = self.head
        while current.next != None:
            current = current.next
        current.next = DoublyLinkedNode(data)
        self.size += 1

    def insert_before(self, index, data):
    # todo make this doubly linked.
        if self.size < index:
            return -1
        current = self.head
        for i in range(index - 1):
            current = current.next
        newNode = DoublyLinkedList(data)
        newNode.next = current.next
        current.next = newNode

    def insert_after(self, index, data):
    # todo make this doubly linked.
        if self.size < index:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        newNode = DoublyLinkedList(data)
        newNode.next = current.next
        current.next = newNode

    def remove(self, data):
    # todo make this doubly linked.
        current = self.head
        previous = self.head
        num_deleted = 0
        for i in range(self.size):
            if current.data == data:
                if self.head == current:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                num_deleted += 1
            previous = current
            current = current.next
        return num_deleted
                
    def toString(self):
        current = self.head
        l = []
        while current != None:
            l.append(str(current.data))
            current = current.next
        return "[" + ",".join(l) + "]"
