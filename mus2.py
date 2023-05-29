from playsound import playsound
from time import sleep
import easygui
import threading

def job():
    easygui.msgbox('', '桐谷和人','摸豆害鴨哭','im.jpg')
    
while(1):
    t = threading.Thread(target = job)
    t.start()    
    playsound('star.wav')
    sleep(1)
    print('yes')

