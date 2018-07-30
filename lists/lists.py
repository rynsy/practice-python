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
    def __init__(self):
        self.head = DoublyLinkedNode()
        self.head.next = self.head
        self.head.prev = self.head
        self.size = 0

    def push_front(self, data):
        if self.head.data == None:
            self.head.data = data
            return
        old_head = self.head
        new_head = DoublyLinkedNode(data)
        new_head.next = old_head
        new_head.prev = old_head.prev
        old_head.prev = new_head
        self.head = new_head
        self.size += 1

    def push_back(self, data):
        if self.head.data == None:
            self.head.data = data
            return
        back = self.head.prev
        newNode = DoublyLinkedNode(data)
        newNode.prev = back
        newNode.next = self.head
        back.next = newNode
        self.size += 1

    def insert_before(self, index, data):
        if self.size < index:
            return -1
        current = self.head
        for i in range(index - 1):
            current = current.next
        newNode = DoublyLinkedList(data)
        newNode.prev = current.prev
        current.prev = newNode
        newNode.next = current
        self.size += 1

    def insert_after(self, index, data):
        if self.size < index:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        newNode = DoublyLinkedList(data)
        newNode.prev = current.prev
        current.prev = newNode
        newNode.next = current
        self.size += 1

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
        l = [str(self.head.data)]
        current = self.head.next
        while current != self.head:
            l.append(str(current.data))
            current = current.next
        return "[" + ",".join(l) + "]"
