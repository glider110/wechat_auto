'''
Author: glider
Date: 2023-07-03 11:47:24
LastEditTime: 2023-07-03 11:54:30
FilePath: /wechat_temp/demo2.py
Version:  v0.01
Description: 
************************************************************************
Copyright (c) 2023 by  ${git_email}, All Rights Reserved. 
************************************************************************
'''
import pyautogui

import datetime
import pyautogui   #模拟鼠标键盘操作
import pyperclip
import os
import random
# pyautogui.screenshot('/Users/wangyongfang/Desktop/glider/wechat_temp/my_screenshot.png') # 截全屏并设置保存图片的位置和名称
# im = pyautogui.screenshot('/Users/wangyongfang/Desktop/glider/wechat_temp/my_screenshot.png') # 截全屏并设置保存图片的位置和名称
# print(im) # 打印图片的属性
 
# # 不截全屏，截取区域图片。截取区域region参数为：左上角XY坐标值、宽度和高度
# pyautogui.screenshot('/Users/wangyongfang/Desktop/glider/wechat_temp/region_screenshot.png', region=(0, 0, 300, 400))
 
# pix = pyautogui.screenshot().getpixel((220, 200)) # 获取坐标(220,200)所在屏幕点的RGB颜色
# positionStr = ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(3) + ')'
# print(positionStr) # 打印结果为RGB:( 60, 63, 65)
# pix = pyautogui.pixel(220, 200) # 获取坐标(220,200)所在屏幕点的RGB颜色与上面三行代码作用一样
# positionStr = ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(3) + ')'
# # print(positionStr) # 打印结果为RGB:( 60, 63, 65)
 
# # 如果你只是要检验一下指定位置的像素值，可以用pixelMatchesColor(x,y,RGB)函数，把X、Y和RGB元组值穿入即可
# # 如果所在屏幕中(x,y)点的实际RGB三色与函数中的RGB一样就会返回True，否则返回False
# # tolerance参数可以指定红、绿、蓝3种颜色误差范围
# pyautogui.pixelMatchesColor(100, 200, (255, 255, 255))
# pyautogui.pixelMatchesColor(100, 200, (255, 255, 245), tolerance=10)
 
# # 获得文件图片在现在的屏幕上面的坐标，返回的是一个元组(top, left, width, height)
# # 如果截图没找到，pyautogui.locateOnScreen()函数返回None
# a = pyautogui.locateOnScreen(r'/Users/wangyongfang/Desktop/glider/wechat_temp/region_screenshot.png')
# print(a) # 打印结果为Box(left=0, top=0, width=300, height=400)
# x, y = pyautogui.center(a) # 获得文件图片在现在的屏幕上面的中心坐标
# print(x, y) # 打印结果为150 200
# # x, y = pyautogui.locateCenterOnScreen(r'/Users/wangyongfang/Desktop/glider/wechat_temp/region_screenshot.png') # 这步与上面的四行代码作用一样
# x, y = pyautogui.locateCenterOnScreen(r'/Users/wangyongfang/Desktop/glider/wechat_temp/1.png') # 这步与上面的四行代码作用一样
# print(x, y) # 打印结果为150 200
 
# # 匹配屏幕所有与目标图片的对象，可以用for循环和list()输出
# pyautogui.locateAllOnScreen(r'/Users/wangyongfang/Desktop/glider/wechat_temp/region_screenshot.png')
# for pos in pyautogui.locateAllOnScreen(r'/Users/wangyongfang/Desktop/glider/wechat_temp/region_screenshot.png'):
#   print(pos)
# # 打印结果为Box(left=0, top=0, width=300, height=400)
# a = list(pyautogui.locateAllOnScreen(r'/Users/wangyongfang/Desktop/glider/wechat_temp/region_screenshot.png'))
# print(a) # 打印结果为[Box(left=0, top=0, width=300, height=400)]




# print(pyautogui.position()) 
# print(pyautogui.size())


# center = pyautogui.locateCenterOnScreen('/Users/wangyongfang/Desktop/glider/wechat_temp/1.png',confidence=0.1,grayscale=True) 
# pyautogui.click(center)


center = pyautogui.locateCenterOnScreen('55.png', confidence=0.5,grayscale=True)
print('发送框坐标：')
print(0.5*center.x, 0.5*center.y)
