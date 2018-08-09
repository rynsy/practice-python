import time

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


mem = {1:1, 2:1}

def fib_memo(n):
    global mem
    if n in mem.keys():
        return mem[n]
    for i in range(2,n+1):
        if i not in mem.keys():
            if (i-1) in mem.keys() and (i-2) in mem.keys():
                mem[i] = mem[i-1] + mem[i-2]
    return mem[n]

def time_func(f, i):
    start = time.time()
    f(i)
    end = time.time()
    return end - start

if __name__ == "__main__":
    num = 30
    print("Recursive Fibonacci (first call) (n={}): {}".format(num,time_func(fib,num)))
    print("Recursive Fibonacci (second call) (n={}): {}".format(num,time_func(fib,num)))
    num = 50000
    print("Memoized Fibonacci (first call) (n={}): {}".format(num,time_func(fib_memo,num)))
    print("Memoized Fibonacci (second call) (n={}): {}".format(num,time_func(fib_memo,num)))

