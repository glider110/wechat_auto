import pyautogui
import pynput.mouse

last_x=0
last_y=0
def on_click(x, y, button, pressed):
    if button == pynput.mouse.Button.middle:
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

get_mouse_coordinates()
