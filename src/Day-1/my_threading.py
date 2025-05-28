import threading


def printno(n):
    for x in range(n):
        print(f" For {n}  : {x+1}")

threads = []
n = [4,6,7]
for num in n:
    t = threading.Thread(target=printno,args=(num,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
