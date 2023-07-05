
# encoding=utf-8
import pyautogui
import pyperclip as pc
import time
import pyautogui
def C(pic):
    box = pyautogui.locateOnScreen(pic)
    if not(box is None):
        center = pyautogui.center(box)
        pyautogui.click(center)
    else:
        time.sleep(2)
        print("未发现图片，2秒后将继续查找")
        C(pic)
         
def Cxy(pic,a,b):
    box = pyautogui.locateOnScreen(pic,)
    if not(box is None):
        center = pyautogui.center(box)
        center1=(center.x+a,center.y+b)
        pyautogui.click(center1)
    else:
        time.sleep(2)
        print("未发现图片，2秒后将继续查找")
        C(pic)
 
def A():   
    print("请切换到要处理的界面")
    time.sleep(3)
    Cxy("1.png",-30,5)
    # C("2.png")
    # pc.copy("无脑点击")
    # pc.paste()
    # pyautogui.hotkey('ctrl', 'v')
    # C("3.png")
    # C("4.png")
     
for i in range(0,10):
    A()
print("程序结束")



help_pos = pyautogui.locateOnScreen("/home/admins/project/other/wechat_temp/1.png",confidence=0.7, grayscale=True)
print(list(help_pos))
# goto_pos = pyautogui.center(help_pos)#找到传回图片的中心点,并传回坐标

print("dddd")


import pyperclip  # 导入pyperclip模块
 
name = 'hello'  # 定一个字符串
 
pyperclip.copy(name)  # 使用pyperclip模块的copy()把字符串拷贝到粘贴版
 
pyperclip.paste()  # 粘贴版的内容


import pyperclip as pc
# text = "Hello,world"
# pc.copy(text)



# pyautogui.screenshot(r'/Users/wangyongfang/Desktop/glider/wechat_temp/my_screenshot.png') # 截全屏并设置保存图片的位置和名称
# im = pyautogui.screenshot(r'/Users/wangyongfang/Desktop/glider/wechat_temp/my_screenshot.png') # 截全屏并设置保存图片的位置和名称
# print(im) # 打印图片的属性
# import pyperclip
# a = pyperclip.waitForPaste(5)
# print(a)