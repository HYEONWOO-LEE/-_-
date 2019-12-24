#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *

window = Tk()
window.title('애니메이션')

def stop():
    global dx
    dx = 0
    
    
def start():
    global dx
    dx = 3
    
    
def re():
    global x,y
    canvas.delete('catch')
    canvas.create_text(x,y,text=owl, tags= 'catch')
    
def fast():
    global speed
    speed -= 3
    
def slow():
    global speed
    speed += 10

canvas = Canvas(window, bg = 'white', width = 250, height=100)
canvas.grid(row =0, column = 0, columnspan = 5)
owl = '''
<<M_M>>
　| |
　- -
   '''
canvas.create_text(30,40, text=owl, tags='catch')


btn_1 = Button(window, text = '▶', width = 5, command = start)
btn_2 = Button(window, text = '||', width = 5, command = stop)
btn_3 = Button(window, text = '■', width = 5, command = re)
btn_4 = Button(window, text = '빠르게', width = 5, command = fast)
btn_5 = Button(window, text = '느리게', width = 5, command = slow)
btn_1.grid(row =1 , column = 0)
btn_2.grid(row =1 , column = 1)
btn_3.grid(row =1 , column = 2)
btn_4.grid(row =1 , column = 3)
btn_5.grid(row =1 , column = 4)

dx = 3
x = 30
y = 50
speed = 40
mv = 30
while True:
    canvas.move('catch',dx,0) # 3만큼 x축으로 이동
    canvas.after(speed)
    canvas.update() #화면을 업데이트
    # 만약 스탑을 눌러서 mv가 0이라면
    # mv를 계속 0으로 유지한다.
    # 스타트를 누르면 mv를 다시 와일문으로 돌린다.
    mv += dx
    if mv > 250:
        mv = 30
        canvas.delete('catch')
        canvas.create_text(x,y,text=owl, tags= 'catch')


window.mainloop()

