"""" cant be killed by mario at once...has 2 lives..random movement"""

import subprocess
from random import randint
import living as l


class Goomba(l.Living):
    """goomba"""
    def __init__(self, arr, x_cord, y_cord, b):
        l.Living.__init__(self, arr, x_cord, y_cord, b)
        self.lives = 2

    def clear_obj(self, arr):
        """obj"""
        if arr[self.x_cord][self.y_cord] == 8:
            arr[self.x_cord][self.y_cord] = 0

    def kill(self, arr, sym):
        """obj"""
        if self.lives <= 1:
            subprocess.Popen(['aplay', '-q', './new_mario.wav'])
            self.alive = False
            sym.score_for_goomba()
            self.clear_obj(arr)
        else:  # whenever killed reappears at another position untill lives==0
            subprocess.Popen(['aplay', '-q', './kill.wav'])
            self.lives = self.lives-1
            self.clear_obj(arr)
            sym.score_for_turtle()
            arr[self.x_cord][self.y_cord+4] = 8
            self.x_cord = self.x_cord
            self.y_cord = self.y_cord+4

    def move_rand(self, arr, mar):
        """rand move"""
        if self.alive:
            a_1, b_1 = 0, 0
            i = randint(1, 4)
            if i == 1:
                a_1, b_1 = 0, -1
            elif i == 2:
                a_1, b_1 = 0, 1
            elif i == 3:
                a_1, b_1 = -1, 0
            elif i == 4:
                a_1, b_1 = 1, 0

            if  0 < (self.x_cord+a_1) < 9 and 0 < (self.y_cord+b_1) < 15:
                if arr[self.x_cord+a_1][self.y_cord+b_1] == 0:
                    arr[self.x_cord][self.y_cord] = 0
                    arr[self.x_cord+a_1][self.y_cord+b_1] = 8
                    self.x_cord = self.x_cord + a_1
                    self.y_cord = self.y_cord + b_1
                    return True
                if arr[self.x_cord+a_1][self.y_cord+b_1] == 3:  # mario got killed
                    arr[self.x_cord][self.y_cord] = 0
                    mar.lives = mar.lives-1
                    mar.check_lives(arr)
                    arr[self.x_cord+a_1][self.y_cord+b_1] = 8
                    self.x_cord = self.x_cord + a_1
                    self.y_cord = self.y_cord + b_1
                    return False
