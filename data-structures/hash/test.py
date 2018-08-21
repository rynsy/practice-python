from hash_table import *
import random as r

def run_all_tests():
    test_lt_class()
    test_ct_class()

def rand_words():
    l = []
    for _ in range(10):
        w = [] 
        for _ in range(5, r.randint(10,20)):
            w.append(chr(r.randint(65,90)))
        l.append("".join(w))
    return l

def test_lt_class():
    l = LinearTable()
    items = []
    for i in range(10):
        h = HashItem(i, r.randint(1337, 6969))
        l.insert(h)
        items.append(h)
    for i in items:
        table_item = l.search(i)
        assert table_item.key == i.key
        assert table_item.data == i.data

def test_ct_class():
    c = ChainedTable()
    keys = rand_words()
    items = []
    for i in range(10):
        h = HashItem(keys[i], i)
        c.insert(h)
        items.append(h)
    for i in items:
        table_item = c.search(i)
        assert table_item.key == i.key
        assert table_item.data == i.data
        table_item = c.search(i.key)
        assert table_item.key == i.key
        assert table_item.data == i.data
run_all_tests()
