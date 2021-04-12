import multiprocessing as mp
import threading as td
import time

def job(q):
    res = 0
    for i in range(10):
        res += i + i**2 + i**3
    q.put(res)

def multicore():
    '多进程程'
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:',res1,res2)
def multiThreading():
    '多线程'
    q = mp.Queue()
    t1 = td.Thread(target=job,args=(q,))
    t2 = td.Thread(target=job,args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print("multi threading:",res1,res2)

def normal():
    '多进程和多线程 分别开了 两个进程或者两个线程，所以如果正常程序如下：'
    res = 0
    for _ in range(2):
        for i in range(10):
            res += i + i**2 + i**3
    print("nomal:",res)

if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    multicore()
    st2 = time.time()
    multiThreading()
    st3 = time.time()
    # 多进程 普通 多线程 运行时间对比
    print("multi processing execution time:",(st2-st1))
    print("normal execution time:",(st1-st))
    print("multi threading execution time:",(st3-st2))