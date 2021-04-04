# encoding=utf-8
from time import  sleep
import os,shutil
usb_path = "/Volumes"
content = os.listdir(usb_path) # os.listdir(路径)返回路径下所有文件以及文件夹的名称

while True:
    new_content = os.listdir(usb_path) # 每次间隔3秒扫描一次 优盘目录
    if new_content != content:
        break
    sleep(3)
x = [item for item in new_content if item not in content]

# 找到那个新文件夹，返回包括新文件夹string类型名称的列表，这个表达方法很pythonic
shutil.copytree(os.path.join(usb_path, x[0]), '/Users/home/')
# shutil.copytree 把目录下所有东西一股脑复制进/Users/home/usb_copy,
# 放进了自己的home目录下