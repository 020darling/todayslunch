from cgitb import text
from hashlib import new
import tkinter as gui
from tkinter import *
from tkinter import font
import tkinter
from turtle import bgcolor, color, onclick
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

def addcanteen():
    result = addlist.get()
    ff = open('config/canteen.txt' , 'a' ,encoding='utf-8')
    ff.write('\n%s' %result)
    ff.close()
    tkinter.messagebox.showinfo(message= '餐厅‘%s’添加成功!' %result)     
  
def addhomefood():
    results = addlist.get()
    ff = open('config/homefood.txt' , 'a' ,encoding='utf-8')
    ff.write('\n%s' %results)
    ff.close()
    tkinter.messagebox.showinfo(message= '食物‘%s’添加成功!' %results)

def decanteen():
    askadf = tkinter.messagebox.askyesno(message='这将删除你所有的餐厅信息，你确定吗？')
    if askadf == True:
        with open('config/canteen.txt' , 'a+' , encoding='utf-8') as dele:
            dele.truncate(0)
            tkinter.messagebox.showwarning(message='删除成功，所有餐厅信息已经被删除!')

def dehomefood():
    askadsf = tkinter.messagebox.askyesno(message='这将清楚你所有的在家煮的信息，你确定吗？')
    if askadsf == True:
        with open('config/homefood.txt' , 'a+' , encoding='utf-8') as delea:
            delea.truncate(0)
            tkinter.messagebox.showwarning(message='删除成功，所有在家煮的方案信息已经被删除!')     

def addfood():
    global addlist
    screen1 = gui.Toplevel()
    screen1.title('增加餐厅或者食品')
    screen1.geometry('300x300')
    screen1.resizable(False,False)
    addlist = gui.Entry(screen1 , width=30 )
    addlist.pack()
    add1 = Button(screen1, text='添加到餐厅列表', font=('microsoft yahei',12),width = 15 ,height = 1,bg=  'pink', command=addcanteen )
    add2 = Button(screen1, text='添加到食物列表', font=('microsoft yahei',12),width = 15 ,height = 1,bg = 'pink' , command=addhomefood)
    add3 = Button(screen1, text='清除餐厅列表', font=('microsoft yahei',12),width = 15 ,height = 1,bg = 'red' , command=decanteen)
    add4 = Button(screen1, text='清除食物列表', font=('microsoft yahei',12 ),width = 15 ,height = 1,bg = 'red' , command=dehomefood)
    add1.pack()
    add2.pack()
    add3.pack()
    add4.pack()
    screen1.mainloop
    


     
        

    



def exit():
    sys.exit(0)


main = gui.Tk()
main.title('选择困难症午餐选择器')
main.geometry('500x810')
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
b4 = gui.Button(main , text='添加餐厅/食物' , font=('micorsoft yahei' ,12), width=50 , height=2 , command=addfood )
b5 = gui.Button(main , text='退出程序' , font=('micorsoft yahei' ,12), width=50 , height=2 , command=exit )
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()



main.mainloop()
