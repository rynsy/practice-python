"""
    This structure was taken from: http://www.cs.rmit.edu.au/online/blackboard/chapter/05/documents/contribute/chapter/05/intro.html
"""
import math

class HashItem():
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.deleted = False

    def setDeleted(self):
        self.deleted = True

    def isDeleted(self):
        return self.deleted

    def getKey(self):
        return self.key

    def getData(self):
        return self.data

class LinearTable():
    def __init__(self):
        self.size = 7
        self.table = []

    def code(self, key):
        return math.abs(self.hashCode(key) % self.size)

    def hashCode(self, key):
        pass
