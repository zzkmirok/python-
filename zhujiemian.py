# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:45:38 2018

@author: Administrator
"""

import tkinter
import random
import time



class Ball():
    def __init__(self,canvas,paddle,color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25, fill='red')
        self.canvas.move(self. id ,245,100)   
        starts=[-3,-2,-1,1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]#从list里面随机取一个
        self.y=-3#-3表示y轴运动的速度
        self.hit_bottom = False
        
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
        return False
    
    
    
    def draw(self):
        self.canvas.move(self. id,self. x,self. y)
        pos = self.canvas.coords(self. id)
        if pos[1]<=0:
            self.y=3     
        if pos[2]<=0:
            self.x=3
        if pos[0]>=self.canvas.winfo_reqwidth(): #此处需要修改
           self.x=-3
        if self.hit_paddle(pos) == True:
            self.y = -3
            
        if pos[3]>=self.canvas.winfo_reqheight(): #此处需要修改
            self.hit_bottom = True
             
class Paddle:
    def turn_left(self, evt):
        self.x = -2
           

    def turn_right(self, evt):
        self.x = 2
        
        
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,80,8,fill=color)
        self.canvas.move(self. id,200,350)
        self.x = 0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        
    
       
    def draw(self):
        self.canvas.move(self. id,self.x,0)
        pos=self.canvas.coords(self. id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2]>=canvas.winfo_reqwidth():
            self.x = 0
            
        

           
    
if __name__ == '__main__':
    tk = tkinter.Tk()
    tk.title("Game")
    tk.resizable(0,0)
    tk.wm_attributes("-topmost",1)
    canvas = tkinter.Canvas(tk, width=500, height=400, bd=0,highlightthickness=0)
    quit = tkinter.Button(tk, text="QUIT", command=tk.destroy)
    canvas.pack()
    quit.pack()
    tk.update()
    paddle = Paddle(canvas,'blue')
    ball = Ball(canvas,paddle,'red')
    time.sleep(2)
    while 1:
        if ball.hit_bottom==False:
            paddle.draw()
            ball.draw()
            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)
        else:
            tk.destroy()
            tk = tkinter.Tk()
            tk.title("Game")
            tk.resizable(0,0)
            tk.wm_attributes("-topmost",1)
            canvas = tkinter.Canvas(tk, width=500, height=400, bd=0,highlightthickness=0)
            quit = tkinter.Button(tk, text="QUIT", command=tk.destroy)
            canvas.pack()
            quit.pack()
            tk.update()
            paddle = Paddle(canvas,'blue')
            ball = Ball(canvas,paddle,'red')
            time.sleep(2)
    



    
