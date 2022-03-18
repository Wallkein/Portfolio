
from tkinter import *
import time
import random
import sys
import os

window = Tk()
window.title("Arcanoid")
window.resizable(0, 0)
window.wm_attributes("-topmost", 1)
canvas = Canvas(window, width=500, height=400)
canvas.pack()


class Ball():
    '''Класс мячика'''
    def __init__(self, canvas, platform, score, color) :
        self.canvas = canvas
        self.platform = platform
        self.score = score
        self.oval = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.oval, 240, 100)
        self.directions = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(self.directions)
        self.y = -3
        self.touch_bottom = False
 
       
        

    def touch_platform(self, ball_pos):
        platform_pos = self.canvas.coords(self.platform.rect)
        if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
            if ball_pos[3] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
                self.score.hit()
                return True 
        else:
            return False
            
    def draw(self):
        self.canvas.move(self.oval, self.x , self.y,)
        pos = self.canvas.coords(self.oval)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= 400:
            self.touch_bottom = True
            canvas.create_text(250, 120, text='Проигрыш', font=('Courier', 30), fill='red')
            window.update()
            time.sleep(2)
            os.abort()
        if self.touch_platform(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= 500:
            self.x = -3
         
            
class Platform():
    '''Класс платформы'''
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.rect, 200, 300)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    def turn_left(self, event):
        self.x = -2

    def turn_right(self, event):
        self.x = 2

    def draw(self):
        self.canvas.move(self.rect, self.x, 0)
        pos = self.canvas.coords(self.rect)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= 500:
            self.x = 0
                   
class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)
        if self.score >= 10:
            canvas.create_text(250, 120, text='Победа', font=('Courier', 30), fill='red')
            window.update()
            time.sleep(2)
            os.abort()
#--------------------------------MAIN--------------------------

score = Score(canvas, 'green')
platform = Platform(canvas, "yellow")
ball = Ball(canvas, platform, score, "blue")

        
while True:
    if ball.touch_bottom == False:
        ball.draw()
        platform.draw()
        window.update()
        time.sleep(0.01)
    
    