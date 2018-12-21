""" enemy1 can be killed by mario...move linear should generat"""
from random import randint
import living as l

class Turtle(l.Living):
    """ Turtle """
    def move_rand(self, arr, mar):
        """ movement """
        if self.alive:
            a_1, b_1 = 0, 0
            truth = False
            x_cord = randint(1, 2)
            if x_cord == 1:
                a_1, b_1 = 0, -1
            elif x_cord == 2:
                a_1, b_1 = 0, 1
            if not ((self.x_cord+a_1) > 10 and (self.y_cord+b_1) > 15):
                if arr[self.x_cord+a_1][self.y_cord+b_1] == 0:
                    arr[self.x_cord][self.y_cord] = 0
                    arr[self.x_cord+a_1][self.y_cord+b_1] = 9
                    self.x_cord = self.x_cord + a_1
                    self.y_cord = self.y_cord + b_1
                    truth = True
                elif arr[self.x_cord+a_1][self.y_cord+b_1] == 3:  # mario got killed
                    arr[self.x_cord][self.y_cord] = 0
                    mar.lives = mar.lives - 1
                    mar.check_lives(arr)
                    arr[self.x_cord+a_1][self.y_cord+b_1] = 0
                    self.x_cord = self.x_cord + a_1
                    self.y_cord = self.y_cord + b_1
                    if arr[9][1] != 0 and arr[8][1] == 0:  # set position
                        arr[8][1] = 3
                        mar.x_cord = 8
                        mar.y_cord = 1
                    else:
                        arr[8][2] = 3
                        mar.x_cord = 8
                        mar.y_cord = 2
                    truth = False

                return truth

    def clear_obj(self, arr):
        if arr[self.x_cord][self.y_cord] == 9:
            arr[self.x_cord][self.y_cord] = 0

    def kill(self, arr, sym):
        self.alive = False
        sym.score_for_turtle()
        self.clear_obj(arr)
