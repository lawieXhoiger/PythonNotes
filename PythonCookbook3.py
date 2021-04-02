from operator import itemgetter
from itertools import groupby

rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows.sort(key=itemgetter('date'))
for data,item in groupby(rows,key=itemgetter('date')):
    print(data)
    for i in item :
        print(i)

# 1/16 过滤序列元素

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
filterval = list(filter(is_int,values))
print("origin values",values,"\nfilter",filterval)


# 当你需要用另外一个相关联的序列来过滤某个序列的时候，
# 这个函数是非常有用的。
addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK',
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
# 现在你想将那些对应 count 值大于 5 的地址全部输出，那么你可以这样做：
#
from itertools import  compress

more5 = [n > 5 for n in counts]
# 这里的关键点在于先创建一个 Boolean 序列，指示哪些元素符合条件。然后
# compress() 函数根据这个序列去选择输出对应位置为 True 的元素。
print(more5)
print("\n",list(compress(addresses,more5)))

# 和 filter() 函数类似， compress() 也是返回的一个迭代器。因此，如果你需要得
# 到一个列表，那么你需要使用 list() 来将结果转换为列表类型。


#1/17 从字典中提取子集
# 你想构造一个字典，它是另外一个字典的子集。

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
# Make a dictionary of all prices over 200
p1 = {key: values for key,values in prices.items() if values > 200}

print(
    "\n p1 ",p1
)
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
# Make a dictionary of tech stocks
p2 = {key: values for key,values in prices.items() if key in tech_names}
print(
    "\n p2",p2
)
# 字典推导方式表意更清晰，并且实际上也会运行的更快些（在这个例子中，
# 实际测试几乎比 dcit() 函数方式快整整一倍）。
# 如下所说
# p1 = dict((key, value) for key, value in prices.items() if value > 200)

# 1.18 映射名称到序列元素
# 你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的
# 代码难以阅读，于是你想通过名称来访问元素。

# collections.namedtuple() 函数通过使用一个普通的元组对象来帮你解决这个问
# 题。这个函数实际上是一个返回 Python 中标准元组类型子类的一个工厂方法。你需要
# 传递一个类型名和你需要的字段给它，然后它就会返回一个类，你可以初始化这个类，
# 为你定义的字段传递值等。

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
Subscriber(addr='jonesy@example.com', joined='2012-10-19')
print("*"*50)
print('\n 1/18 \n',
    sub
)
print(
   "\n sub.addr:", sub.addr
)
print("\n sub.joined:",sub.joined)
print(len(sub))


# 尽管 namedtuple 的实例看起来像一个普通的类实例，但是它跟元组类型是可交换
# 的，支持所有的普通元组操作，比如索引和解压。比如：

addr, joined = sub
print('addr:',addr)
print('joined:',joined)


# 命名元组的一个主要用途是将你的代码从下标操作中解脱出来。因此，如果你从数
# 据库调用中返回了一个很大的元组列表，通过下标去操作其中的元素，当你在表中添加
# 了新的列的时候你的代码可能就会出错了。但是如果你使用了命名元组，那么就不会有
# 这样的顾虑。

# def compute_cost(records):
#     total = 0.0
#     for rec in records:
#         total += rec[1] * rec[2]
#     return total
#

# 和上面 对比 增加了 可读性

from collections import namedtuple

Stock = namedtuple('Stock',['name','shares','price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

# 命名元组另一个用途就是作为字典的替代，因为字典存储需要更多的内存空间。如
# 果你需要构建一个非常大的包含字典的数据结构，那么使用命名元组会更加高效。但是
# 需要注意的是，不像字典那样，一个命名元组是不可更改的。比如：

s = Stock('ACME',100,123.45)
print('\n',s,'\ns.price',s.price)

# 如果你真的需要改变属性的值，那么可以使用命名元组实例的 _replace() 方法，
# 它会创建一个全新的命名元组并将对应的字段用新的值取代。比如：

s = s._replace(shares=76)
print('\n',s)

# _replace() 方法还有一个很有用的特性就是当你的命名元组拥有可选或者缺失字
# 段时候，它是一个非常方便的填充数据的方法。你可以先创建一个包含缺省值的原型元
# 组，然后使用 _replace() 方法创建新的值被更新过的实例。比如：

from collections import  namedtuple

Stock = namedtuple('Stock',['name','shares','price','date','time'])
# create a prototype instance
stock_prototype = Stock('',0,0.0,None,None)
#Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print('\n dict a',a,'\n dict_to_stock a',dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print('\n dict b',b,'\n dict_to_stock b',dict_to_stock(b))

# 1.19 转换并同时计算数据

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

import os
files = os.listdir('/Users/chen/PythonNotes')
if any(name.endswith('.py') for name in files):
    print("=="*10,"\nThere be python.")
else:
    print('Sorry, no python.')
#Output a tuple as CSV
s = ('ACME',50,123.45)
print(','.join(str(x) for x in s))
#Data reduction across fields of a data structure
portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
# min_shares = min(portfolio, key=lambda s: s['shares'])
min_shares = min(portfolio,key=lambda s:s['shares'])
print("min_shares:",min_shares)

# 1.20 合并多个字典或映射
# 现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某
# 些操作，比如查找值或者检查某些键是否存在。


from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

c = ChainMap(a,b)
print('==='*10,'\nChainMap c:{0},len(c):{1},\n '
               'list(c.keys()):{2},list(c.values():{3}'.format(c,len(c),list(c.keys()),list(c.values())))

# 2.1 使用多个界定符分割字符串

# 你需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定
# 的。

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
string_split = re.split(r'(;|,|\s)\s*', line)
print("string_split:",string_split)
print('re.split():',re.split('[;,\s]\s*',line))

# 2.2 字符串开头或结尾匹配
# 你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀， URL
# Scheme 等等。
filename = 'spam.txt'
url = 'http://www.python.org'
print("filename.endswith('.txt'):{},filename.startswith('file:')".format(filename.endswith('.txt'),
                                             filename.startswith('file:'),url.startswith('http:')))
# 如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传
# 给 startswith() 或者 endswith() 方法：
import os
filename = os.listdir('.')
print('filename',filename)
print("match .py .git",
      [name for name in filename if name.endswith(('.py','.git'))])
print("any .py files",any(name.endswith(".py") for name in filename))

from urllib.request import urlopen
def read_data(name):
    if name.startswith('http:','https:','ftp'):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

import re
url = 'http://www.python.org'
print(re.match('http:|https:|ftp:',url))

# 2.4 字符串匹配和搜索
# 你想匹配或者搜索特定模式的文本
# 如果你想匹配的是字面字符串，那么你通常只需要调用基本字符串方法就行，比如
# str.find() , str.endswith() , str.startswith() 或者类似的方法：
text = 'yeah, but no, but yeah, but no, but yeah'
print("text == 'yeah':{0}\n,text.startswith('yeah'):{1},\ntext.endswith('no')"
      .format(text == 'yeah',text.startswith('yeah'),text.endswith('no')))

# 对于复杂的匹配需要使用正则表达式和 re 模块。为了解释正则表达式的基本原理，
# 假设你想匹配数字格式的日期字符串比如 11/27/2012 ，你可以这样做

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

if re.match(r"\d+/\d+/\d+",text1):
    print("yes")
else:
    print("no")
