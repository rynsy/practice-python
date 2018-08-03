"""
    This structure was taken from: http://www.cs.rmit.edu.au/online/blackboard/chapter/05/documents/contribute/chapter/05/intro.html
"""
import math
import random as r

class HashItem():
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.deleted = False

    def setDeleted(self):
        self.deleted = True

    def isDeleted(self):
        return self.deleted

class LinearTable():
    def __init__(self):
        self.size = 10
        self.table = [None for _ in range(self.size)]
    
    def search(self, item):
        return self.table[item.key]

    def insert(self, item):
        self.table[item.key] = item

    def delete(self, item):
        self.table[item.key] = None

class ChainedTable():
    def __init__(self):
        self.size = 10
        self.last_insert = 0
        self.table = [[] for _ in range(self.size)]

    def search(self, item):
        return self.table[item.key]

    def insert(self, item):
        self.last_insert += 1
        self.last_insert %= self.size
        if self.table[self.last_insert] != None
            self.table[self.last_insert] = item
        else:
            print("Collision!")

    def delete(self, item):
        self.table[item.key] = None
