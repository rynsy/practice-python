def match(p, s):
    dp = [[False for _ in range(len(p))] for _ in range(len(s))]
    dp[0][0] = True
    print(dp)

def test():
    assert match("A", "A") == True
    assert match("A", "B") == False
    # 65-122
    for i in range(65, 122):
        assert match(".", chr(i)) == True
    for i in range(66, 122):
        assert match("A", chr(i)) == False

#test()
match("test", "test")
