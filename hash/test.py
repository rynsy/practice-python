from hash_table import *
import random as r

def run_all_tests():
    test_lt_class()

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

run_all_tests()
