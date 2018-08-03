"""
    I've been messing around with a couple of different classes for hashing. As of right now, I'm trying
    to get the ChainedTable to work kind of like a dictionary but the type system in Python is very frustrating.

    Putting this down for now.
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
   
    def key_to_int(self, key):
        n = 0
        for l in key:
            n += ord(l)
        n %= self.size
        return n

    def search(self, item):
        if type(item) == HashItem and type(item.key) == str:
            indx = self.key_to_int(item.key)
            ti = self.table[indx]
        elif type(item) == HashItem and type(item.key) == int:
            ti = self.table[item.key]
        elif type(item) == str:
            indx = self.key_to_int(item)
            ti = self.table[indx]
        if ti.key == item.key:
            return ti
        else:
            return None

    def insert(self, item):
        self.table[item.key] = item

    def delete(self, item):
        self.table[item.key] = None

class ChainedTable():
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def key_to_int(self, key):
        n = 0
        for l in key:
            n += ord(l)
        n %= self.size
        return n

    def search(self, item):
        print("Searching this table:", self.table)
        if type(item) == HashItem and type(item.key) == str:
            indx = self.key_to_int(item.key)
            sub_table = self.table[indx]
        elif type(item) == HashItem and type(item.key) == int:
            sub_table = self.table[item.key]
        elif type(item) == str:
            indx = self.key_to_int(item)
            sub_table = self.table[indx]
        for i in range(len(sub_table)): 
            print("looking in this subtable: ", sub_table)
            if sub_table[i] != None:
                if type(item) == str and sub_table[i].key == item:
                    return sub_table[i]
                elif type(item) == str and sub_table[i].key == item.key:
                    return sub_table[i]
        return None

    def insert(self, item):
        if type(item) == HashItem and type(item.key) == str:
            indx = self.key_to_int(item.key)
            sub_table = self.table[indx]
        elif type(item) == HashItem and type(item.key) == int:
            sub_table = self.table[item.key]
        else:
            print("Problem inserting")
            return
        for i in range(len(sub_table)): 
            if sub_table[i] != None and sub_table[i].key == item.key:
                print("Item with that key already exists!")
                return
        sub_table.append(item)

    def delete(self, item):
        indx = self.key_to_int(item)
        sub_table = self.table[indx]
        for i in range(len(sub_table)): 
            if sub_table[i] != None and sub_table[i].key == item.key:
                sub_table[i] = None
