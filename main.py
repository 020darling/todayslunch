from cgitb import text
from hashlib import new
import tkinter as gui
from tkinter import *
from tkinter import font
import tkinter
from turtle import onclick
import random
from PIL import Image
from PIL import ImageTk
import sys
import tkinter.messagebox
import webbrowser


def outside():
    shop = []
    with open('config/canteen.txt' , 'r' ,encoding='utf-8') as fillin:
        for line in fillin:
            shop.append(list(line.strip().split(',')))
    while True:
        todaylunch = random.choice(shop)
        aks22 = tkinter.messagebox.askyesno(message='今天去%s吃可以吗？'%todaylunch)
        
        if aks22 == True:
            tkinter.messagebox.showinfo(message='那今天就吃%s吧，不吃祝你被警察开罚单，祝您干饭愉快!' %todaylunch)
            sys.exit(0)



def jueshi():
    tkinter.messagebox.showinfo(message='我明白了你想绝食,但在绝食前我希望您熟读以下信息:\n香港紧急报警电话:999\n香港警察热线:+852 25277177\n消费者委员会热线:+852 29292222\n香港殡仪馆服务热线:+852 25615226\n红磡世界殡仪馆服务热线:+852 23624331\n死因裁判法庭服务热线:+852 39166204\n生死登记总处服务热线:+852 28246111\n')
    asd = tkinter.messagebox.askyesno(message='希望您在去世前将您的银行卡密码发送至2096314156@qq.com,专业团队为您管理遗产，您打算现在发送邮件吗?')
    if asd == True:
        webbrowser.open('mailto:?to=2096314156@qq.com&subject=我的银行卡密码',new=1)
        tkinter.messagebox.showinfo(message='请在您本地邮箱客户端进行哦！')
        sys.exit(0)
    else:
        tkinter.messagebox.showinfo(message='那好吧，祝您英年早逝，生活愉快！')
        sys.exit(0)


def homecook():
    home = []
    with open('config/homefood.txt' ,'r', encoding='utf-8')as homefood:
        for line in homefood:
            home.append(list(line.strip('\n').split(',')))
    while True:
        todayhomecook = random.choice(home)
        aks11 = tkinter.messagebox.askyesno(message='今天整个%s吃可以吗？'%todayhomecook)
        
        if aks11 == True:
            tkinter.messagebox.showinfo(message='那今天就吃%s吧，不吃削了你，祝您干饭愉快!' %todayhomecook)
            sys.exit(0)
        

        


def exit():
    sys.exit(0)


main = gui.Tk()
main.title('选择困难症午餐选择器')
main.geometry('500x765')
main.resizable(False,False)
bkg = Image.open('config/background.jpg')
bkgl = ImageTk.PhotoImage(bkg)
backgrond = tkinter.Label(main , image=bkgl)
backgrond.image = bkgl
llable = gui.Label(main , text='欢迎使用选择困难症午餐选择器！', bg='pink' , font=('microsoft yahei' , 12),width=70 ,height=2)    
llable.pack()
backgrond.pack()



b1 = gui.Button(main , text='去外面吃饭' , font=('micorsoft yahei' ,12), width=50 , height=2 , command= outside )
b2 = gui.Button(main , text='在家煮饭吃' , font=('micorsoft yahei' ,12), width=50 , height=2  , command= homecook)
b3 = gui.Button(main , text='我打算绝食！' , font=('micorsoft yahei' ,12), width=50 , height=2 , command=jueshi )
b4 = gui.Button(main , text='退出程序' , font=('micorsoft yahei' ,12), width=50 , height=2 , command=exit )
b1.pack()
b2.pack()
b3.pack()
b4.pack()




main.mainloop()