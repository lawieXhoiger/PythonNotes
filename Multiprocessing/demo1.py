import multiprocessing as mp
import threading as td

def job(a,b):
    print("="*10,a,b)

if __name__ == "__main__":
    p1 = mp.Process(target=job,args=('multiprocessing start',2))
    p1.start()
    p1.join()
    t1 = td.Thread(target=job,args=('Threading start ',2))
    t1.start()
    t1.join()
