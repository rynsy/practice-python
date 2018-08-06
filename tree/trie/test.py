from trie import *

words =  ["fundamental", "fun", "final", "financial", "rotund", "rotunda", "rotten", "word", "a", "apple", "applicable"]

def run_all_tests():
    test_construct()
    test_only_terminated_words()
    test_captalization()

def test_construct():
    global words
    t = Trie()
    for w in words:
        t.insert(w)
    for w in words:
        assert t.find(w) == True

def test_only_terminated_words():
    t = Trie()
    t.insert("fundip")
    assert t.find("fun") == False

def test_captalization():
    t = Trie()
    t.insert("Fun")
    assert t.find("fun") == False
