import threading
import queue
import time

def main():
    que = queue.Queue()
    que1 = queue.Queue()
    thread1 = threading.Thread(target = lambda q, arg : que.put(sum(arg)), args = (que, [5, 2]))
    thread2 = threading.Thread(target = lambda q, arg : que1.put(minus(arg)), args = (que1, [5, 2]))

    test = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(time.time()-test)
    print(que.get())
    print(que1.get())

def sum(a):
    ans = a[0] + a[1]
    time.sleep(3)
    return [ans, ans-1]

def minus(b):
    ans1 = b[0] - b[1]
    time.sleep(2)
    return [ans1, ans1-1]

main()
