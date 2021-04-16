import threading
from queue import Queue
import time

def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l) # 多线程调用的函数不能用return 返回值。

def multithreading(data):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t) # 把每个线程append到线程列表中
    #分别join 四个线程到主线程
    for thread in threads:
        thread.join()
    # 定义一个空的列表result，将四个线程运行后保存在队列中的结果返回到空列表result中
    res = []
    for _ in range(4):
        res.append(q.get()) # q.get()按顺序从q中拿出一个值.
    print("result :",res)

if __name__ == "__main__":
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
    multithreading(data)