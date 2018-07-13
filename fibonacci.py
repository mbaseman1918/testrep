def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(9))

def list_fib(n):
    fib_num = [0,1]
    for i in range(n-1):
        fib_num.append(fib_num[-1] + fib_num[-2])
    return fib_num[-1]

print(list_fib(207260))
