# encoding: utf-8
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
import pyautogui   #模拟鼠标键盘操作
import pyperclip
import os
import random
from pynput.mouse import Controller,Button
import schedule
import time


####################晚安语言#################
def print_goodnight():
    #基准坐标
    enter_touxiang = pyautogui.locateCenterOnScreen('./icon/touxiang.png', confidence=0.8,grayscale=True)
    touxiang_x=0.5*enter_touxiang.x
    touxiang_y=0.5*enter_touxiang.y
    print('头像坐标：')
    print(touxiang_x,touxiang_y)
    time.sleep(1)
    mapping_img('./icon/shouchang.png','') 
    mapping_img('./icon/serchbox.png','single')
    print("搜素：晚安语")
    pyperclip.copy("晚安语")
    pyautogui.hotkey('command','v')

    time.sleep(1)
    today = datetime.datetime.now().day
    if today%2==1:
        pyautogui.moveRel(xOffset=400,yOffset=110)  #鼠标向下标动80，选中联系人
    else:
        pyautogui.moveRel(xOffset=400,yOffset=250)  #鼠标向下标动80，选中联系人
        
    time.sleep(1)
    mouse = Controller()
    mouse.click(Button.left,1)
    time.sleep(1.5)
    #发第一个群
    mapping_img('./icon/33.png','') 
    pyautogui.moveRel(xOffset=10,yOffset=0)  
    time.sleep(1.5)
    mouse.click(Button.left,1)
    pyperclip.copy("西北浪")
    pyautogui.hotkey('command','v')
    keyboard = Controller()
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    mapping_img('./icon/66.png','')    #发送晚安消息
    #发第二个群
    mapping_img('./icon/33.png','') 
    pyautogui.moveRel(xOffset=10,yOffset=0)  
    time.sleep(1.5)
    mouse.click(Button.left,1)
    pyperclip.copy("glider")
    pyautogui.hotkey('command','v')
    keyboard = Controller()
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    mapping_img('./icon/66.png','')   #发送晚安消息
    pyautogui.hotkey('command','w')     #关闭晚安收藏窗口
    time.sleep(2)
    pyautogui.moveTo(touxiang_x, touxiang_y+60)
    mouse.click(Button.left,1)

def mapping_img(img,click):      #当前屏幕找到图片的中心位置,单击或双击。
    center = pyautogui.locateCenterOnScreen(img, confidence=0.8,grayscale=True)
    print('搜索坐标：')
    print(0.5*center.x,0.5*center.y)

    if click == 'double':
        pyautogui.doubleClick(0.5*center.x,0.5*center.y)
    else:
        pyautogui.leftClick(0.5*center.x,0.5*center.y)
    time.sleep(1)



def read_txt(txt):
    hellofile = open(txt,'r',encoding='utf-8')
    hellocontent = hellofile.readlines()
    print(len(hellocontent))
    number = random.randint(0,len(hellocontent)-1)
    print('line number is {}'.format(number))
    # data =hellocontent[number]
    data =hellocontent[number]
    print(data)
    pyperclip.copy(hellocontent[1])
    
    # box_location = pyautogui.locateOnScreen('/home/admins/project/other/wechat_temp/6.png', confidence=0.9,grayscale=True)
    # print(box_location)
    # center = pyautogui.center(box_location)
    # pyautogui.leftClick(center.x,center.y+10)

    center = pyautogui.locateCenterOnScreen('smiles.png', confidence=0.8,grayscale=True)
    print('文字框坐标：')
    print(0.5*center.x,0.5*center.y)
    pyautogui.doubleClick(0.5*center.x,0.5*center.y+10)
    pyautogui.hotkey('command','v')
    hellofile.close()



def main():
    os.chdir('/Users/wangyongfang/Desktop/glider/wechat_temp/')
    print(os.getcwd())
    #从程序坞点击微信
    mapping_img('./icon/1.png','')    #执行微信/登录过程需要在手机上确认一次。

    ####################文案###################

    print_goodnight()

    
    ####################定时器#################
    # while True:
    #     now = datetime.datetime.now()
    #     print(now)
    #     time.sleep(5)

    #     if now.hour == 22 and now.minute >= 3 :


    #         random_seconds = random.randint(0, 59)
    #         random_minutes = random.randint(0, 30)
    #         # 计算下一个执行时间
    #         next_run = now + datetime.timedelta(minutes=random_minutes, seconds=random_seconds)
            
    #         print("print next_run time:")
    #         print(next_run)
    #         # 等待到达下一个执行时间
    #         time.sleep((next_run - now).total_seconds())
        
            
    #         # 执行打印"晚安"到控制台
    #         print_goodnight()


if __name__ == '__main__':
    main()