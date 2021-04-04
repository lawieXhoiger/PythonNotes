#
# 2.20 字节字符串上的字符串操作
# 你想在字节字符串上执行普通的文本操作 (比如移除，搜索和替换)。
# 字节字符串同样也支持大部分和文本字符串一样的内置操作。比如：
data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# 这些操作同样也适用于字节数组。比如：

data = bytearray(b"Hello World")
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel')
      )
# 你可以使用正则表达式匹配字节字符串，但是正则表达式本身必须也是字节串。比
# 如：
data = b'FOO:BAR,SPAM'
import re
print(re.split(b'[:,]',data) )
# 大多数情况下，在文本字符串上的操作均可用于字节字符串。然而，这里也有一些
# 需要注意的不同点。首先，字节字符串的索引操作返回整数而不是单独字符。比如：
a = 'Hello World' # Text string
print( a[0])
b = b'Hello World' # Byte string
print(b[0])
# 这种语义上的区别会对于处理面向字节的字符数据有影响。
s = b'Hello World'
print(s)
print(s.decode('ascii'))

# 如果你想格式化字节字符串，你得先使用标准的文本字符串，然后将其编码为字节
# 字符串。比如：
print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))

# 最后需要注意的是，使用字节字符串可能会改变一些操作的语义，特别是那些跟文
# 件系统有关的操作。比如，如果你使用一个编码为字节的文件名，而不是一个普通的文
# 本字符串，会禁用文件名的编码/解码。比如：

with open('xf1o.txt','w') as f:
    f.write('spicy')
import os
print(os.listdir('.'))
print(os.listdir(b'.'))
