#Cookbook chapter 4 Iterator and generator
# 4.1 手动遍历迭代器
# 你想遍历一个可迭代对象中的所有元素，但是却不想使用 for 循环。

# 为了手动的遍历可迭代对象，使用 next() 函数并在代码中捕获 StopIteration 异
# 常。比如，下面的例子手动读取一个文件中的所有行：
def manual_iter():
    with open('/etc/passed') as f:
        try:
            while True:
                line = next(f)
                print(line,end=' ')
        except StopIteration:
            pass

items = [1,2,3]
# get the iterator
it = iter(items)
# Run the iterator
print(it.__next__())
print(it.__next__())
print(it.__next__())
# print(it.__next__()) 会报错

# 4.2 代理迭代
# 你构建了一个自定义容器对象，里面包含有列表、元组或其他可迭代对象。你想直
# 接在你的这个新容器对象上执行迭代操作。

# 实际上你只需要定义一个 __iter__() 方法，将迭代操作代理到容器内部的对象上
# 去。比如：

class Node:
    def __init__(self,value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node{!r}'.format(self._value)
    def add_child(self,node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
# Example
# if __name__ == '__main__':
#     root = Node(0)
#     child1 = Node(1)
#     child2 = Node(2)
#     root.add_child(child1)
#     root.add_child(child2)
#     # Outputs Node(1),Node(2)
#     for ch in root:
#         print(ch)
# 在上面代码中， __iter__() 方法只是简单的将迭代请求传递给内部的 _children
# 属性。

# 4.3 使用生成器创建新的迭代模式
# 你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不
# 一样。

# 如果你想实现一种新的迭代模式，使用一个生成器函数来定义它。下面是一个生产
# 某个范围内浮点数的生成器：

def frange(start,stop,increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0,4,0.5):
    print(n)

print(list(frange(0,1,0.125)))

# 一个函数中需要有一个 yield 语句即可将其转换为一个生成器。跟普通函数不同
# 的是，生成器只能用于迭代操作。下面是一个实验，向你展示这样的函数底层工作机制：

def countdown(n):
    print('Staring to count from',n)
    while n > 0:
        yield n
        n -=1
    print('Done')

# Create the generator,notice no output appears
c = countdown(3)
# print(c)
#
# 4.4 实现迭代器协议
# 见 Chapter4.4.py 文件
