'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
>>文件: 鼠标控制.py
>>作者: liu yang
>>邮箱: liuyang0001@outlook.com
>>博客: www.cnblogs.com/liu66blog
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
import pynput
from pynput.mouse import Controller,Button
# 实例化鼠标控制
mouse = Controller()
# x坐标+100,y坐标+100
mouse.move(100,100)
# 将鼠标移动到固定位置
mouse.position=(1475, 35)
# 读取当前的鼠标位置
position=format(mouse.position)
print(position)
# 右键单击
mouse.click(Button.right,1)
# 左键双击
mouse.click(Button.left,2)

# 单击的另一种实现,先点击后释放
mouse.press(Button.right)
mouse.release(Button.right)

# 鼠标滚动(x,y)  x代表左右移动,y代表上下移动
# X:正值代表从右向左   Y:正值代表向上移动,负值代表向下移动
mouse.scroll(0,-1000)