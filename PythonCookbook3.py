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