# 3.1 数字的四舍五入
# 你想对浮点数执行指定精度的舍入运算。
# 对于简单的舍入运算，使用内置的 round(value, ndigits) 函数即可。比如：
print(round(1.23,1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361,3))
# 传给 round() 函数的 ndigits 参数可以是负数，这种情况下，舍入运算会作用在
# 十位、百位、千位等上面。比如：
a = 1627731
print(round(a))
print(round(a,-1))
print(round(a,-2))
print(round(a,-3))
# 不要将舍入和格式化输出搞混淆了。如果你的目的只是简单的输出一定宽度的数，
# 你不需要使用 round() 函数。而仅仅只需要在格式化的时候指定精度即可。比如：
x = 1.23456
print(format(x,'0.2f'))
print(format(x,'0.3f'))
print("value is {:0.3f}".format(x))

# 3.2 执行精确的浮点数运算
# 你需要对浮点数执行精确的计算操作，并且不希望有任何小误差的出现。
a = 4.2
b = 2.1
print(a + b)
print("(a + b) == 6.3\n",(a + b) == 6.3)

# 使用 decimal 模块：

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print("="*20,a+b)
print((a+b)==Decimal('6.3'))

# decimal 模块的一个主要特征是允许你控制计算的每一方面，包括数字位数和四
# 舍五入运算。为了这样做，你先得创建一个本地上下文并更改它的设置，比如：

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)

with localcontext() as ctx:
    ctx.prec = 10
    print(a/b)

# 即便如此，你却不能完全忽略误差。数学家花了大量时间去研究各类算法，有些处
# 理误差会比其他方法更好。你也得注意下减法删除以及大数和小数的加分运算所带来
# 的影响。比如：
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))
# 上面的错误可以利用 math.fsum() 所提供的更精确计算能力来解决：

import math
print("nums:{},\nsum:{}\nmath.fsum:{}"
      .format(nums,sum(nums),math.fsum(nums)))

# 3.3 数字的格式化输出

x = 1234.56789
print(format(x,'0.2f'))
print(format(x,">10.2f"))
print(format(x,"<10.2f"))
print(format(x,"^10.2f"))

print(format(x,","))
# 如果你想使用指数记法，将 f 改成 e 或者 E(取决于指数输出的大小写形式)。比如：
print(format(x,"e"))
print(format(x,".2e"))

# 同时指定宽度和精度的一般形式是 '[<>^]?width[,]?(.digits)?' ，其中 width
# 和 digits 为整数，？代表可选部分。同样的格式也被用在字符串的 format() 方法中。
# 比如：
print("The value is {"
      ":0,.2f}".format(x))

# 3.4 二八十六进制整数
# 你需要转换或者输出使用二进制，八进制或十六进制表示的整数。
# 为了将整数转换为二进制、八进制或十六进制的文本串，可以分别使用 bin() ,
# oct() 或 hex() 函数：
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

# 另外，如果你不想输出 0b , 0o 或者 0x 的前缀的话，可以使用 format() 函数。比
# 如：

print(format(x,'b'))
print(format(x,'o'))
print(format(x,'x'))

# Python 指定八进制数的语法跟其
# 他语言稍有不同。比如，如果你像下面这样指定八进制，会出现语法错误：
import os
# os.chmod('xf1o.txt',0755) 会报错

print(os.chmod('xf1o.txt',0o755))

# 3.5 字节到大整数的打包与解包
# 你有一个字节字符串并想将它解压成一个整数。或者，你需要将一个大整数转换为
# 一个字节字符串。
# 假设你的程序需要处理一个拥有 128 位长的 16 个元素的字节字符串。比如：

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
# 为了将 bytes 解析为整数，使用 int.from_bytes() 方法，并像下面这样指定字节
# 顺序：
print(int.from_bytes(data,'little'))

print(int.from_bytes(data,'big'))

# 为了将一个大整数转换为一个字节字符串，使用 int.to_bytes() 方法，并像下面
# 这样指定字节数和字节顺序：

x = 94522842520747284487117727783387188

print(x.to_bytes(16,'little'))
print(x.to_bytes(16,'big'))

# 大整数和字节字符串之间的转换操作并不常见。然而，在一些应用领域有时候也会
# 出现，比如密码学或者网络。例如， IPv6 网络地址使用一个 128 位的整数表示。如果
# 你要从一个数据记录中提取这样的值的时候，你就会面对这样的问题

# 作为一种替代方案，利用 struct 模块来解压对于整数的大小是有限制的。因此，你可
# 能想解压多个字节串并将结果合并为最终的结果，就像下面这样：
print(data)
import struct
hi,lo = struct.unpack('>QQ',data)
print((hi<<64)+lo)

# 字节顺序规则 (little 或 big) 仅仅指定了构建整数时的字节的低位高位排列方式。
# 我们从下面精心构造的 16 进制数的表示中可以很容易的看出来：
x = 0x01020304
print(x.to_bytes(4,'big'))
print(x.to_bytes(4,'little'))

# 如果你试着将一个整数打包为字节字符串，那么它就不合适了，你会得到一个错
# 误。如果需要的话，你可以使用 int.bit_length() 方法来决定需要多少字节位来存储
# 这个值。

x = 523 ** 23
print("x=",x)
# x.to_bytes(16, 'little') 会报错  因为length 不够长。

print(x.bit_length())

nbytes,rem = divmod(x.bit_length(),8)

if rem:
    nbytes+=1
print("nbytes:",nbytes)
print(x.to_bytes(nbytes,'big'))

# 3.6 复数的数学运算
# 你写的最新的网络认证方案代码遇到了一个难题，并且你唯一的解决办法就是使
# 用复数空间。再或者是你仅仅需要使用复数来执行一些计算操作。

# 复数可以用使用函数 complex(real, imag) 或者是带有后缀 j 的浮点数来指定。
# 比如：

a = complex(2, 4)
b = 3 - 5j
print(a,"and",b)
print(a.real,'and imag',a.imag)
print("a={},and a conjugate={}".format(a,a.conjugate()))

# 如果要执行其他的复数函数比如正弦、余弦或平方根，使用 cmath 模块：

import cmath

print("a sin use cmath module={}".format(cmath.sin(a)))

print("a cos use cmath modul={}".format(cmath.cos(a)))

print("a exp use cmath module={}".format(cmath.exp(a)))

import numpy as np

a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a+2)
print(np.sin(a))

# Python 的标准数学函数确实情况下并不能产生复数值，因此你的代码中不可能会
# 出现复数返回值。比如：
import math
# math.sqrt(-1) 会报错，因为python的标准函数中没有复数
# 可以使用 cmath
import cmath
print(cmath.sqrt(-1))

# 3.7 无穷大与 NaN
# 你想创建或测试正无穷、负无穷或 NaN(非数字) 的浮点数。

# Python 并没有特殊的语法来表示这些特殊的浮点值，但是可以使用 float() 来创
# 建它们。比如：
a = float('inf')
b = float('-inf')
c = float('nan')
print("a={},b={},c={}".format(a,b,c))

# 为了测试这些值的存在，使用 math.isinf() 和 math.isnan() 函数。比如：

print("math.isinf(a)={},math.isnan()={}".
      format(math.isinf(a),math.isnan(c)))
print(a+45)
print(a*10)
print(10/a)
print(a/a)
# NaN 值会在所有操作中传播，而不会产生异常。比如：
print("c =",math.sqrt(c))

# NaN 值的一个特别的地方时它们之间的比较操作总是返回 False。比如：
c = float('nan')
d = float('nan')
print("c==d =",c==d)
print("c is d ? :",(c is d))

# 由于这个原因，测试一个 NaN 值得唯一安全的方法就是使用 math.isnan() ，也
# 就是上面演示的那样。

# 3.8 分数运算
# 你进入时间机器，突然发现你正在做小学家庭作业，并涉及到分数计算问题。或者
# 你可能需要写代码去计算在你的木工工厂中的测量值

from fractions import Fraction
a = Fraction(5,4)
print(a)
b = Fraction(7,16)
print(b)
print(a,b)
c = a*b
print(c)

print(c.numerator)
print(c.denominator)

print(float(c))

print(c.limit_denominator(8))
# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)

# 3.9 大型数组运算
# 需要在大数据集 (比如数组或网格) 上面执行计算。
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x*2)
# x + 10 会报错
print(x + y)
import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax*2)
print(ax+10)
print( ax + ay)
print(np.sqrt(ax))
grid = np.zeros(shape=(10,10),dtype=float)
print(grid)
print(grid+10)

print(np.sin(grid))
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[1])
print(a[:,1])
print(a[1:3,1:3])
a[1:3,1:3]+=10

print(a)
print(np.where(a<10,a,10))

# 3.10 矩阵与线性代数运算
# 你需要执行矩阵和线性代数运算，比如矩阵乘法、寻找行列式、求解线性方程组等
# 等。

# 矩阵类似于 3.9 小节中数组对象，但是遵循线性代数的计算规则。下面的一个例子
# 展示了矩阵的一些基本特性：

import numpy as np

ma = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print("="*10,ma)
print("="*10,ma.T)
# Return inverse
print("="*20)
print(ma.I)
v = np.matrix([[2],[3],[4]])
print("="*10)
print(v)
print("="*10)
print(ma*v)

# 可以在 numpy.linalg 子包中找到更多的操作函数，比如：
import numpy.linalg
print(numpy.linalg.det(ma))

#eigenvalues
print(numpy.linalg.eigvals(ma))

#Solve for x in mx = v
x = numpy.linalg.solve(ma,v)
print(x)

print(ma*x)

print(v)

# 3.11 随机选择
# 你想从一个序列中随机抽取若干元素，或者想生成几个随机数。
# random 模块有大量的函数用来产生随机数和随机选择元素。比如，要想从一个序
# 列中随机的抽取一个元素，可以使用 random.choice() ：
import random
values = [1,2,3,4,5,6,7]
print("random.choice(values)\n",random.choice(values))
print(random.choice(values))
# 为了提取出 N 个不同元素的样本用来做进一步的操作，可以使用 random.sample():
print(random.sample(values,2))
print(random.sample(values,2))

# 如果你仅仅只是想打乱序列中元素的顺序，可以使用 random.shuffle() ：
random.shuffle(values)
print(values)
# \生成随机整数，请使用 random.randint() ：
print(random.randint(0,10))

print(random.randint(0,10))
# \为了生成 0 到 1 范围内均匀分布的浮点数，使用 random.random() ：
print(random.random())

print(random.random())

# 如果要获取 N 位随机位 (二进制) 的整数，使用 random.getrandbits() ：
print(random.getrandbits(128))

# random 模块使用 Mersenne Twister 算法来计算生成随机数。这是一个确定性算
# 法，但是你可以通过 random.seed() 函数修改初始化种子。比如：

random.seed() # Seed based on system time or os.urandom()
random.seed(12345) # Seed based on integer given
random.seed(b'bytedata') # Seed based on byte data

# 除了上述介绍的功能， random 模块还包含基于均匀分布、高斯分布和其他分布的
# 随机数生成函数。比如， random.uniform() 计算均匀分布随机数， random.gauss() 计
# 算正态分布随机数。对于其他的分布情况请参考在线文档。

# 3.12 基本的日期与时间转换

# 你需要执行简单的时间转换，比如天到秒，小时到分钟等的转换。

# 为了执行不同时间单位的转换和计算，请使用 datetime 模块。比如，为了表示一
# 个时间段，可以创建一个 timedelta 实例，就像下面这样：

from datetime import timedelta
a = timedelta(days=2,hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days,"c.seconds",c.seconds)
print("hours:",c.seconds/3600)
print("total seconds:",c.total_seconds()/3600)

# 如果你想表示指定的日期和时间，先创建一个 datetime 实例然后使用标准的数学
# 运算来操作它们。比如：
from datetime import datetime
a = datetime(2018,9,17)
print(a + timedelta(days=10))
b = datetime(2018,10,1)
c = b - a
print(c.days)
now = datetime.now()
print(now)
print("distance National Day:",b - now)

# 在计算的时候，需要注意的是 datetime 会自动处理闰年。比如：
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)
print((a-b).days)
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c-d).days)

# 许多类似的时间计算可以使用 dateutil.relativedelta() 函数代替。但是，有一
# 点需要注意的就是，它会在处理月份 (还有它们的天数差距) 的时候填充间隙。看例子
# 最清楚：

a = datetime(2018, 9, 17)
# a + timedelta(months=1) 会报错
from dateutil.relativedelta import relativedelta
print(a + relativedelta(months=+1))
print(a + relativedelta(months=+4))
# Time between two dates
b = datetime(2018, 12, 21)
d = b - a
print(d)

# 3.13 计算最后一个周五的日期
# 你需要查找星期中某一天最后出现的日期，比如星期五。
# Python 的 datetime 模块中有工具函数和类可以帮助你执行这样的计算。下面是
# 对类似这样的问题的一个通用解决方案：

from datetime import datetime,timedelta
weekdays = ['Monday','Tuesday','Wednesday','Thursday',
            'Friday','Saturday','Sunday']
def get_previous_byday(dayname,start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target)%7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date
print(datetime.today())
print(get_previous_byday('Monday'))
print(get_previous_byday('Tuesday'))
print(get_previous_byday('Friday'))
print(get_previous_byday('Sunday',datetime(2018,9,17)))

# 上面的算法原理是这样的：先将开始日期和目标日期映射到星期数组的位置上 (星
# 期一索引为 0)，然后通过模运算计算出目标日期要经过多少天才能到达开始日期。然
# 后用开始日期减去那个时间差即得到结果日期。


# 如果你要像这样执行大量的日期计算的话，你最好安装第三方包 python-dateutil
# 来代替。比如，下面是是使用 dateutil 模块中的 relativedelta() 函数执行同样的计
# 算：

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
d = datetime.now()
print(d)
# new Friday
print(d+relativedelta(weekday=FR))
print(d+relativedelta(weekday=SA))
# last Friday
print(d + relativedelta(weekday=FR(-1)))

# 3.14 计算当前月份的日期范围
# 你的代码需要在当前月份中循环每一天，想找到一个计算这个日期范围的高效方
# 法。
# 在这样的日期上循环并需要事先构造一个包含所有日期的列表。你可以先计算出
# 开始日期和结束日期，然后在你步进的时候使用 datetime.timedelta 对象递增这个日
# 期变量即可。
# 下面是一个接受任意 datetime 对象并返回一个由当前月份开始日和下个月开始日
# 组成的元组对象。

from datetime import datetime,date,timedelta
import calendar

def get_month_range(start_date=None):
    if start_date == None:
        start_date = date.today().replace(day=1)
    _,day_in_month = calendar.monthrange(start_date.year,start_date.month)
    end_date = start_date + timedelta(days=day_in_month)
    return (start_date,end_date)
# 有了这个就可以很容易的在返回的日期范围上面做循环操作了：
a_day = timedelta(days=1)
first_day,last_day = get_month_range(datetime(2018,9,17))
print("=="*30)
while first_day < last_day:
    print(first_day)
    first_day += a_day

# 3.15 字符串转换为日期
# 你的应用程序接受字符串格式的输入，但是你想将它们转换为 datetime 对象以便
# 在上面执行非字符串操作。
from datetime import datetime
text = '2018-09-15'
y = datetime.strptime(text,"%Y-%m-%d")
z = datetime.now()
diff = z - y
print("text = '2012-09-20':\n",y)
print(diff)

# strptime()的性能比你想象中的差很多，因为它是使用纯Python实现，并且必须处理所有系统本地设置
# 如果需要大量处理此类问题可以使用split()进行切割，性能是strptime()的7倍
from datetime import datetime
def parse_ymd(s):
    year_s,mon_s,day_s = s.split('-')
    return datetime(int(year_s),int(mon_s),int(day_s))


# 3.16 结合时区的日期操作

# 你有一个安排在 2018 年 12 月 21 日早上 9:30 的电话会议，地点在芝加哥。而你
# 的朋友在印度的班加罗尔，那么他应该在当地时间几点参加这个会议呢？

# 对几乎所有涉及到时区的问题，你都应该使用 pytz 模块。这个包提供了 Olson 时
# 区数据库，它是时区信息的事实上的标准，在很多语言和操作系统里面都可以找到。
# pytz 模块一个主要用途是将 datetime 库创建的简单日期对象本地化。比如，下
# 面如何表示一个芝加哥时间的示例：

from datetime import datetime
from pytz import timezone

d = datetime(2018,12,21,9,30,0)
print("India/Bangalore",d)
# localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print("US/Chicago:",loc_d)

# 一旦日期被本地化了，它就可以转换为其他时区的时间了。为了得到班加罗尔对应
# 的时间，你可以这样做：

# convert to Bangalore time
bang_d = loc_d.astimezone(timezone("Asia/Kolkata"))
print("bang_d time : ",bang_d)

# 为了不让你被这些东东弄的晕头转向，处理本地化日期的通常的策略先将所有日
# 期转换为 UTC 时间，并用它来执行所有的中间存储和操作。比如：
import  pytz
loc_d = datetime.now()
central = timezone('US/Central')
loc_d = central.localize(d)
print("loc_d:",loc_d)
utc_d = loc_d.astimezone(pytz.utc)
print("utc_d:",utc_d)

# 当涉及到时区操作的时候，有个问题就是我们如何得到时区的名称。比如，在这个
# 例子中，我们如何知道“ Asia/Kolkata”就是印度对应的时区名呢？为了查找，可以使
# 用 ISO 3166 国家代码作为关键字去查阅字典 pytz.country_timezones 。比如：
print(pytz.country_timezones['IN'])
