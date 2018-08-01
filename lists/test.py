from lists import *

def run_all_tests():
    single_linked_construct_test()
    single_linked_push_test()
    single_linked_insert_before_test()
    single_linked_insert_after_test()
    single_linked_remove_test()

    double_linked_construct_test()
    double_linked_push_test()
    double_linked_insert_before_test()
    double_linked_insert_after_test()
    double_linked_remove_test()

def single_linked_construct_test():
    l = SinglyLinkedList()
    for i in range(10):
        l.push_back(i)
    assert l.toString() == "[0,1,2,3,4,5,6,7,8,9]"

def single_linked_push_test():
    l = SinglyLinkedList()
    l.push_back(1)
    l.push_front(0)
    assert l.toString() == "[0,1]"
    l.push_front(2)
    assert l.toString() == "[2,0,1]"
    l.push_back(4)
    assert l.toString() == "[2,0,1,4]"

def single_linked_insert_before_test():
    l = SinglyLinkedList()
    l.push_back(0)
    l.push_back(1)
    l.push_back(2)
    l.insert_before(1,4)
    assert l.toString() == "[0,4,1,2]"
    l.insert_before(1,4)
    assert l.toString() == "[0,4,4,1,2]"
    l.insert_before(2,5)
    assert l.toString() == "[0,4,5,4,1,2]"

def single_linked_insert_after_test():
    l = SinglyLinkedList()
    l.push_back(0)
    l.push_back(1)
    l.push_back(2)
    l.insert_after(1,4)
    assert l.toString() == "[0,1,4,2]"
    l.insert_after(1,4)
    assert l.toString() == "[0,1,4,4,2]"
    l.insert_after(2,5)
    assert l.toString() == "[0,1,4,5,4,2]"

def single_linked_remove_test():
    l = SinglyLinkedList()
    for i in range(10):
        l.push_back(i)
    assert l.toString() == "[0,1,2,3,4,5,6,7,8,9]"
    l.remove(2)
    assert l.toString() == "[0,1,3,4,5,6,7,8,9]"

#Doubly linked tests
def double_linked_construct_test():
    l = DoublyLinkedList()
    for i in range(10):
        l.push_back(i)
    assert l.toString() == "[0,1,2,3,4,5,6,7,8,9]"

def double_linked_push_test():
    l = DoublyLinkedList()
    l.push_back(1)
    l.push_front(0)
    assert l.toString() == "[0,1]"
    l.push_front(2)
    assert l.toString() == "[2,0,1]"
    l.push_back(4)
    assert l.toString() == "[2,0,1,4]"

def double_linked_insert_before_test():
    l = DoublyLinkedList()
    l.push_back(0)
    l.push_back(1)
    l.push_back(2)
    l.insert_before(1,4)
    assert l.toString() == "[0,4,1,2]"
    l.insert_before(1,4)
    assert l.toString() == "[0,4,4,1,2]"
    l.insert_before(2,5)
    assert l.toString() == "[0,4,5,4,1,2]"

def double_linked_insert_after_test():
    l = DoublyLinkedList()
    l.push_back(0)
    l.push_back(1)
    l.push_back(2)
    l.insert_after(1,4)
    assert l.toString() == "[0,1,4,2]"
    l.insert_after(1,4)
    assert l.toString() == "[0,1,4,4,2]"
    l.insert_after(2,5)
    assert l.toString() == "[0,1,4,5,4,2]"

def double_linked_remove_test():
    l = DoublyLinkedList()
    for i in range(10):
        l.push_back(i)
    assert l.toString() == "[0,1,2,3,4,5,6,7,8,9]"
    l.remove(2)
    assert l.toString() == "[0,1,3,4,5,6,7,8,9]"

run_all_tests()
