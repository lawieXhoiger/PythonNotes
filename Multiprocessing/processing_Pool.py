import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    '默认Pool中的 processes 是None 全部开启,使用map函数迭代，apply_async()只能单次传递。'
    pool = mp.Pool(processes=3)
    res = pool.map(job,range(10))
    print(res)
    #Pool 除了map() 以外还可以使用 apply_async()
    #其中apply_async()中只能传递一个值，只会放入一个进程运算。
    res = pool.apply_async(job,(2,))
    # 使用get 获得结果
    print(res.get())
    # 使用apply_async()输出多个结果
    multi_res = [pool.apply_async(job,(i,))for i in range(10)]
    print([res.get() for res in multi_res])
if __name__ == "__main__":
    multicore()