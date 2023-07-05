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
import pyautogui
import pynput.mouse
import threading

print('WWWW')

def on_click(x, y, button, pressed):
    if button == pynput.mouse.Button.left:
        print('鼠标点击坐标:', (x, y))
        global last_x 
        global last_y
        delt_x=x -last_x
        delt_y=y -last_y
        print('坐标delta:', (delt_x,delt_y))
        last_x=x
        last_y=y


def get_mouse_coordinates():
    with pynput.mouse.Listener(on_click=on_click) as listener:
        listener.join()

thread = threading.Thread(target=get_mouse_coordinates)
thread.daemon = True   # 将线程设置为分离状态
# 启动线程
thread.start()


def main():
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()