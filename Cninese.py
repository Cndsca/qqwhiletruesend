from pynput.keyboard import Controller as key_cl
from pynput.mouse import Controller,Button
import time

def keyboard_input(string):
    keyboard = key_cl()
    keyboard.type(string)

def mouse_click():
    mouse = Controller()
    mouse.press(Button.left)
    mouse.release(Button.left)

def main(number,string):
    time.sleep(1)
    for i in range(number):
        keyboard_input(string)
        mouse_click()
        time.sleep(0.1)

if __name__=='__main__':
    userNumber = input("请输入轰炸次数：")
    userDate = input("请输入内容：")
    main(int(userNumber),userDate)
                       
