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



# match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位
# 置，使用 findall() 方法去代替。

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'\d+/\d+/\d+')

if datepat.match(text1):
    print("yes")
else:
    print("no")

print(" \n datepat.findall(text)",datepat.findall(text))

# 在定义正则式的时候，通常会利用括号去捕获分组。比如：
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
m = datepat.match("11/27/2012")
print("m:{0},\nm.group(0):{1},\nm.group(1):{2},\nm.group(2):{3},\nm.group(3):{4},\nm.groups():{5}"
      .format(m,m.group(0),m.group(1),m.group(2),m.group(3),m.groups()))
month,day,year = m.groups()
print("month, day, year = m.groups():\nmonth:{0},day:{1},year:{2}"
      .format(month,day,year))

for month,day,year in datepat.findall(text):
    print("{0}--{1}--{2}".format(year,month,day))

# findall() 方法会搜索文本并以列表形式返回所有的匹配。如果你想以迭代方式返
# 回匹配，可以使用 finditer() 方法来代替，比如：

for m in datepat.finditer(text):
    print("m.group():{}===m.groups():{}".format(m.group(),m.groups()))

# 如果你想精确匹配，确保你的正则表达式以 $ 结尾，就像这么这样：
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
datepat.match('11/27/2012abcdef')

# 2.5 字符串搜索和替换

# 你想在字符串中搜索和匹配指定的文本模式
# 对于简单的字面模式，直接使用 str.replace() 方法即可，比如：

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah','yep'))

# 对于复杂的模式，请使用 re 模块中的 sub() 函数。为了说明这个，假设你想将形
# 式为 11/27/2012 的日期字符串改成 2012-11-27 。示例如下：

# sub() 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字
# 比如 \3 指向前面模式的捕获组号。

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print(re.sub(r"(\d+)/(\d+)/(\d+)",r"\3-\1-\2",text))


# 如果除了替换后的结果外，你还想知道有多少替换发生了，可以使用 re.subn()
# 来代替。比如：

newtext ,n  = datepat.subn(r"\3-\1-\2",text)
print("newtext and replace . newtext :{} \nand replace n:{}"
      .format(newtext,n))

# 2.6 字符串忽略大小写的搜索替换
# 你需要以忽略大小写的方式搜索与替换文本字符串
# 为了在文本操作时忽略大小写，你需要在使用 re 模块的时候给这些操作提供
# re.IGNORECASE 标志参数。比如：

text = 'UPPER PYTHON, lower python, Mixed Python'

print(re.findall('python',text,flags=re.IGNORECASE))
print(re.sub("python","snake",text,flags=re.IGNORECASE))
# >> UPPER snake, lower snake, Mixed snake

# 最后的那个例子揭示了一个小缺陷，替换字符串并不会自动跟被匹配字符串的大
# 小写保持一致。为了修复这个，你可能需要一个辅助函数，就像下面的这样：

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
print("original text:",text)
print(re.sub("python",matchcase('snake'),text,flags=re.IGNORECASE))


# 译者注： matchcase('snake') 返回了一个回调函数 (参数必须是 match 对象)，前
# 面一节提到过， sub() 函数除了接受替换字符串外，还能接受一个回调函数。

# 2.7 最短匹配模式
# 你正在试着用正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹
# 配。而你想修改它变成查找最短的可能匹配。
str_pat = re.compile(r"\"(.*)\"")
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

# 在这个例子中，模式 r'\"(.*)\"' 的意图是匹配被双引号包含的文本。但是在正
# 则表达式中 * 操作符是贪婪的，因此匹配操作会查找最长的可能匹配。于是在第二个
# 例子中搜索 text2 的时候返回结果并不是我们想要的。
# 为了修正这个问题，可以在模式中的 * 操作符后面加上? 修饰符，就像这样：

# 这样就使得匹配变成非贪婪模式，从而得到最短的匹配，也就是我们想要的结果。
str_pat = re.compile(r"\"(.*?)\"")

# 2.8 多行匹配模式
# 你正在试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配
# 这个问题很典型的出现在当你用点 (.) 去匹配任意字符的时候，忘记了点 (.) 不能
# 匹配换行符的事实。比如，假设你想试着去匹配 C 语言分割的注释：

comment = re.compile(r"/\*(.*?)\*/")
text1 = '/* this is a comment */'
text2 = '''/* this is a
... multiline comment */
... '''

print(comment.findall(text1))
print("text2",comment.findall(text2))

# 为了修正这个问题，你可以修改模式字符串，增加对换行的支持。比如：
comment = re.compile(r"/\*(.*?)\*/",re.DOTALL)
print("text2",comment.findall(text2))

# 2.9 将 Unicode 文本标准化
# 你正在处理 Unicode 字符串，需要确保所有字符串在底层有相同的表示。

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

import unicodedata

t1 = unicodedata.normalize('NFC',s1)
t2 = unicodedata.normalize("NFC",s2)

print(t1==t2)

# 标准化对于任何需要以一致的方式处理 Unicode 文本的程序都是非常重要的。当
# 处理来自用户输入的字符串而你很难去控制编码的时候尤其如此。
# 在清理和过滤文本的时候字符的标准化也是很重要的。比如，假设你想清除掉一些
# 文本上面的变音符的时候 (可能是为了搜索和匹配)：

t1 = unicodedata.normalize('NFD',s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))


# 最后一个例子展示了 unicodedata 模块的另一个重要方面，也就是测试字符类的
# 工具函数。 combining() 函数可以测试一个字符是否为和音字符。在这个模块中还有其
# 他函数用于查找字符类别，测试是否为数字字符等等。

# 2.10 在正则式中使用 Unicode
# 你正在使用正则表达式处理文本，但是关注的是 Unicode 字符处理。
# 默认情况下 re 模块已经对一些 Unicode 字符类有了基本的支持。比如， \\d 已经
# 匹配任意的 unicode 数字字符了：
import re
num = re.compile("\d+")
print(num.match('12131'))
num.match('\u0661\u0662\u0663')
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

# 当执行匹配和搜索操作的时候，最好是先标准化并且清理所有文本为标准化格式
# (参考 2.9 小节)。但是同样也应该注意一些特殊情况，比如在忽略大小写匹配和大小写
# 转换时的行为。

pat = re.compile('stra\u00dfe',re.IGNORECASE)
s = 'straße'
print(pat.match(s.upper())) #Doesn't match
print(s.upper())

# 2.11 删除字符串中不需要的字符
# 你想去掉文本字符串开头，结尾或者中间不想要的字符，比如空白。
# strip() 方法能用于删除开始或结尾的字符。 lstrip() 和 rstrip() 分别从左和
# 从右执行删除操作。默认情况下，这些方法会去除空白字符，但是你也可以指定其他字符。
# 比如：

s = ' hello world \n'
print("s.strip():{0},\ns.lstrip():{1},\ns.rstrip():{2}".format(s.strip(),s.lstrip(),s.rstrip()))

t = '-----hello====='
print(t.lstrip('-'))
print(t.rstrip('='))
print(t.strip('-='))

# 这些 strip() 方法在读取和清理数据以备后续处理的时候是经常会被用到的。比
# 如，你可以用它们来去掉空格，引号和完成其他任务。
# 但是需要注意的是去除操作不会对字符串的中间的文本产生任何影响。比如：

s = ' hello    world \n'
s = s.strip()
print(s)

# 如果你想处理中间的空格，那么你需要求助其他技术。比如使用 replace() 方法
# 或者是用正则表达式替换。示例如下：

print(s.replace(' ',''))

import re
print(re.sub('\s+',' ',s))

# 通常情况下你想将字符串 strip 操作和其他迭代操作相结合，比如从文件中读取
# 多行数据。如果是这样的话，那么生成器表达式就可以大显身手了。比如：
# with open(filename) as f:
#     lines = (line.strip() for line in f)
#     for line in lines:
#         print(line)
# 在这里，表达式 lines = (line.strip() for line in f) 执行数据转换操作。

# 2.12 审查清理文本字符串

# 一些无聊的幼稚黑客在你的网站页面表单中输入文本” pýtĥöñ”，然后你想将这些
# 字符清理掉。

# 文本清理问题会涉及到包括文本解析与数据处理等一系列问题。在非常简单的情
# 形下，你可能会选择使用字符串函数 (比如 str.upper() 和 str.lower() ) 将文本转为
# 标准格式。使用 str.replace() 或者 re.sub() 的简单替换操作能删除或者改变指定
# 的字符序列。你同样还可以使用 2.9 小节的 unicodedata.normalize() 函数将 unicode
# 文本标准化。
# 然后，有时候你可能还想在清理操作上更进一步。比如，你可能想消除整个区间上
# 的字符或者去除变音符。为了这样做，你可以使用经常会被忽视的 str.translate()
# 方法。为了演示，假设你现在有下面这个凌乱的字符串：

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
# 第一步是清理空白字符。为了这样做，先创建一个小的转换表格然后使用
# translate() 方法：

remap = {
    ord('\t'):' ',
    ord('\f'):' ',
    ord('\r'):None #delete
}
a = s.translate(remap)
print(a)
# 正如你看的那样，空白字符 \t 和 \f 已经被重新映射到一个空格。回车字符 r 直
# 接被删除。
# 你可以以这个表格为基础进一步构建更大的表格。比如，让我们删除所有的和音
# 符：


import unicodedata
import sys

# 另一种清理文本的技术涉及到 I/O 解码与编码函数。这里的思路是先对文本做一
# 些初步的清理，然后再结合 encode() 或者 decode() 操作来清除或修改它。比如：

b = unicodedata.normalize('NFD',a)
print(b.encode('ascii','ignore').decode('ascii'))

#这里的标准化操作将原来的文本分解为单独的和音符。


# 文本字符清理一个最主要的问题应该是运行的性能。一般来讲，代码越简单运行越
# 快。对于简单的替换操作， str.replace() 方法通常是最快的，甚至在你需要多次调用
# 的时候。比如，为了清理空白字符，你可以这样做：

def clean_spaces(s):
    s = s.replace('\r','')
    s = s.replace('\t','')
    s = s.replace('\f','')
    return s

# 2.13 字符串对齐
#
# 你想通过某种对齐方式来格式化字符串
# 对于基本的字符串对齐操作，可以使用字符串的 ljust() , rjust() 和 center()
# 方法。比如：
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
# 所有这些方法都能接受一个可选的填充字符。比如：
print(text.rjust(20,'='))
print(text.center(20,"*"))

# 函数 format() 同样可以用来很容易的对齐字符串。你要做的就是使用 <,> 或者 ^
# 字符后面紧跟一个指定的宽度。比如：
print(format(text,">20"))
print(format(text,"<20"))
print(format(text,"^20"))
# 如果你想指定一个非空格的填充字符，将它写到对齐字符的前面即可：
print(format(text,"=>20"))
print(format(text,"*^20"))

# 当格式化多个值的时候，这些格式代码也可以被用在 format() 方法中。比如：
print("{:>10}{:>10}".format('hello','world'))
x = 1.2345
print(format(x,'>10'))
print(format(x,'^10.2f'))

# 2.14 合并拼接字符串

# 你想将几个小的字符串合并为一个大的字符串
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(''.join(parts))
print(' '.join(parts))
print(','.join(parts))
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

# 最后谈一下，如果你准备编写构建大量小字符串的输出代码，你最好考虑下使用生
# 成器函数，利用 yield 语句产生输出片段。比如：
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago'
text = ' '.join(sample())
print(text)

# 你还可以写出一些结合 I/O 操作的混合方案：
def combine(source,maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size +=len(part)
        if size > maxsize:
            yield ' '.join(parts)
            parts = []
            size = 0
        yield ' '.join(parts)
# 结合文件操作
with open('filename','w') as f:
    for part in combine(sample(),32768):
        f.write(part)


# 2.15 字符串中插入变量
# 你想创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉。
# Python 并没有对在字符串中简单替换变量值提供直接的支持。但是通过使用字符
# 串的 format() 方法来解决这个问题。比如：
s = '{name} has {n} messages.'
print(s.format(name='Guido',n=37))

# 如果要被替换的变量能在变量域中找到，那么你可以结合使用 format_map()
# 和 vars() 。

name = 'Guido'
n = 37
print("=="*10)
print(s.format_map(vars()))

# vars() 还有一个有意思的特性就是它也适用于对象实例。比如：

class Info:
    def __init__(self,name,n):
        self.name = name
        self.n = n
a = Info('Guido',37)
print("vars(a)")
print(s.format_map(vars(a)))
# format 和 format_map() 的一个缺陷就是它们并不能很好的处理变量缺失的情况，
# 比如：

# 多年以来由于 Python 缺乏对变量替换的内置支持而导致了各种不同的解决方案。
# 作为本节中展示的一个可能的解决方案，你可以有时候会看到像下面这样的字符串格
# 式化代码：
import string
s = string.Template('$name has $n messages.')
print(s.substitute(vars()))

# 2.16 以指定列宽格式化字符串
# 你有一些长字符串，想以指定的列宽将它们重新格式化

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
print(textwrap.fill(s,70))

print(textwrap.fill(s,40))
print(textwrap.fill(s,70,initial_indent='    '))
print(textwrap.fill(s,70,subsequent_indent='    '))

# textwrap 模块对于字符串打印是非常有用的，特别是当你希望输出自动匹配终端
# 大小的时候。你可以使用 os.get_terminal_size() 方法来获取终端的大小尺寸。比如：

# import os
# os.get_terminal_size().columns

# 2.17 在字符串中处理 html 和 xml

# 如果你想替换文本字符串中的‘ <’或者‘ >’，使用 html.escape() 函数可以很
# 容易的完成。比如：

s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))
# Disable escaping of quotes
print(html.escape(s,quote=False))
s = 'Spicy Jalapeño'
print(s.encode('ascii',errors='xmlcharrefreplace'))

s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))

# 2.18 字符串令牌解析
# 你有一个字符串，想从左至右将其解析为一个令牌流。
text = 'foo = 23 + 42 * 10'
# 为了令牌化字符串，你不仅需要匹配模式，还得指定模式的类型。比如，你可能想
# 将字符串像下面这样转换为序列对：
tokens = [('NAME','foo'),('EQ','='),('NUM','23'),('PLUS','+'),
          ('NUM','42'),('TIMES','*'),('NUM','10')]
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
print(master_pat)

# 在上面的模式中， ?P<TOKENNAME> 用于给一个模式命名，供后面使用。

# 使用模式对象很少被人知道的 scanner() 方法。这个方法
# 会创建一个 scanner 对象，在这个对象上不断的调用 match() 方法会一步步的扫描目
# 标文本，每步一个匹配。下面是演示一个 scanner 对象如何工作的交互式例子：

scanner = master_pat.scanner('foo=20')
print(scanner.match())

def generate_tokens(pat,text):
    Token = namedtuple('Token',['type','value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match,None):
        yield Token(m.lastgroup,m.group())
for tok in generate_tokens(master_pat,'foo=40'):
    print(tok)

# 如果你想过滤令牌流，你可以定义更多的生成器函数或者使用一个生成器表达式。
# 比如，下面演示怎样过滤所有的空白令牌：
tokens = (tok for tok in generate_tokens(master_pat,text)
          if tok.type != 'WS')
for i in tokens:
    print("tok:",i)


# 通常来讲令牌化是很多高级文本解析与处理的第一步。为了使用上面的扫描方法，
# 你需要记住这里一些重要的几点。第一点就是你必须确认你使用正则表达式指定了所
# 有输入中可能出现的文本序列。如果有任何不可匹配的文本出现了，扫描就会直接停
# 止。这也是为什么上面例子中必须指定空白字符令牌的原因。
# 令牌的顺序也是有影响的。 re 模块会按照指定好的顺序去做匹配。因此，如果一
# 个模式恰好是另一个更长模式的子字符串，那么你需要确定长模式写在前面。

LT = r"(?P<LT><)"
LE = "(?P<LE><=)"
EQ = "(?P<EQ>=)"

# master_pat = re.compile('|'.join(LE,LT,EQ)) # corrcect
# master_pat = re.compile('|'.join([LT, LE, EQ])) # Incorrect
# 第二个模式是错的，因为它会将文本 <= 匹配为令牌 LT 紧跟着 EQ，而不是单独
# 的令牌 LE，这个并不是我们想要的结果。

PRINT = "(?P<PRINT>print)"
NAME = "(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)"

master_pat = re.compile('|'.join([PRINT,NAME]))

for tok in generate_tokens(master_pat,'printer'):
    print(tok)

# 2.19 实现一个简单的递归下降分析器
# 你想根据一组语法规则解析文本并执行命令，或者构造一个代表输入的抽象语法
# 树。如果语法非常简单，你可以自己写这个解析器，而不是使用一些框架。

# 在这个问题中，我们集中讨论根据特殊语法去解析文本的问题。为了这样做，你首
# 先要以 BNF 或者 EBNF 形式指定一个标准语法。比如，一个简单数学表达式语法可能
# 像下面这样：

# expr ::= expr + term
# | expr - term
# | term
# term ::= term * factor
# | term / factor
# | factor
# factor ::= ( expr )
# | NUM

# 或者，以 EBNF 形式：

# expr ::= term { (+|-) term }*
# term ::= factor { (*|/) factor }*
# factor ::= ( expr )
# | NUM

# 在 EBNF 中，被包含在 {...}* 中的规则是可选的。 *代表 0 次或多次重复 (跟正
# 则表达式中意义是一样的)。
# NUM + NUM * NUM
# 在此基础上，解析动作会试着去通过替换操作匹配语法到输入令牌：
# expr
# expr ::= term { (+|-) term }*
# expr ::= factor { (*|/) factor }* { (+|-) term }*
# expr ::= NUM { (*|/) factor }* { (+|-) term }*
# expr ::= NUM { (+|-) term }*
# expr ::= NUM + term { (+|-) term }*
# expr ::= NUM + factor { (*|/) factor }* { (+|-) term }*
# expr ::= NUM + NUM { (*|/) factor}* { (+|-) term }*
# expr ::= NUM + NUM * factor { (*|/) factor }* { (+|-) term }*
# expr ::= NUM + NUM * NUM { (*|/) factor }* { (+|-) term }*
# expr ::= NUM + NUM * NUM { (+|-) term }*
# expr ::= NUM + NUM * NUM

# 下面所有的解析步骤可能需要花点时间弄明白，但是它们原理都是查找输入并试
# 着去匹配语法规则。第一个输入令牌是 NUM，因此替换首先会匹配那个部分。一旦匹
# 配成功，就会进入下一个令牌 +，以此类推。当已经确定不能匹配下一个令牌的时候，
# 右边的部分 (比如 { (*/) factor }* ) 就会被清理掉。在一个成功的解析中，整个右
# 边部分会完全展开来匹配输入令牌流。

# 有了前面的知识背景，下面我们举一个简单示例来展示如何构建一个递归下降表
# 达式求值程序：

