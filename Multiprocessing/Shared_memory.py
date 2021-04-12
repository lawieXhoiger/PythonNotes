import multiprocessing as mp

# 使用Value数据存储在一个共享的内存表中。
value1 = mp.Value('i',1)
value2 = mp.Value('d',0.322)
print(value1,value2)
# 其中d和i参数用来设置数据类型的，d表示一个双精浮点类型，i表示一个带符号的整型。

# Shared Array

# 在Python的mutiprocessing中，有还有一个Array类，可以和共享内存交互，来实现在进程之间共享数据。
array = mp.Array('i',[1,1,2,3,4,4])
print(array)