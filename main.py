from os import system
from time import sleep
from sympy import *
import screen


class Golf_ball:
    def __init__(self, xcordinate=0, ycordinate=0, xforce=0, yforce=0, gravity=1):
        x, y, t = symbols('x y t')

        self.y_by_time = -1 * y + yforce * t + gravity * t ** 2 / 2 + ycordinate
        self.x_by_time = -1 * t + x / xforce + xcordinate
        self.tragectory = self.y_by_time.subs(t, self.x_by_time)

def showframes(ball):
    x, y, t = symbols('x y t')
    seconds = 0
    while seconds < 10:
        ball_position = [tuple(solveset(ball.x_by_time.subs(t, seconds)))[0],
                         tuple(solveset(ball.y_by_time.subs(t, seconds)))[0]]
        screen.show(ball_position)
        #sleep(200)
        #system("cls")
        seconds = seconds + 0.2


bola = Golf_ball(0, 1, 7, 3)
showframes(bola)