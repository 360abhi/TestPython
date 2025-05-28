def count(n):
    for x in range(n):
        yield x


gen = count(5)
print(next(gen))
print(next(gen))
print("\nFirst ended\n")


def fibo(n):
    a,b=0,1
    count=0
    while True:
        if count == n:
            break
        else:
            count +=1

        yield a
        a,b = b,a+b

fib = fibo(8)
for fi in fib:
    print(fi)