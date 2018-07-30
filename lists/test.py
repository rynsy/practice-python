from lists import *

def run_all_tests():
    single_linked_construct_test()


def single_linked_construct_test():
    l = SinglyLinkedList()
    for i in range(10):
        l.push_back(i)
    assert l.toString() == "[0,1,2,3,4,5,6,7,8,9]"

run_all_tests()
