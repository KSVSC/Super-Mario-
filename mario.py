"""init mario"""

from time import sleep
import subprocess
import living as l
import board as b1

class Mario(l.Living):
    """mario"""
    def __init__(self, arr, x_cord, y_cord, b):
        l.Living.__init__(self, arr, x_cord, y_cord, b)
        self.lives = 5

    def check_lives(self, arr):
        """alive"""
        subprocess.Popen(['aplay', '-q', './touch.wav'])
        if self.lives > 0:
            arr[self.x_cord][self.y_cord] = 0
            self.x_cord = 8
            self.y_cord = 3
            return True
        self.alive = False
        self.clear_obj(arr)
        return False

    def move(self, inp, arr, cb_c, t_c, mr_c, g_c, sym):
        """move"""
        def srceen_shift(arr, a_1, b_1):  # screen shift left only
            """screen_shift"""
            if arr[self.x_cord][self.y_cord+1] == 0:
                for i_1 in range(11):
                    for i_2 in range(45):
                        if(arr[i_1][i_2] != 2 and arr[i_1][i_2] != 3):
                            if(arr[i_1+a_1][i_2+b_1] != 2 and arr[i_1+a_1][i_2+b_1] != 3):
                                arr[i_1+a_1][i_2+b_1] = arr[i_1][i_2]
                        else:
                            if arr[i_1+a_1][i_2+b_1] != 2:
                                arr[i_1+a_1][i_2+b_1] = 0
                for g_1 in g_c:
                    g_1.y_cord = g_1.y_cord-1
                for cb_1 in cb_c:
                    cb_1.y_cord = cb_1.y_cord-1
                for mr1 in mr_c:
                    mr1.y_cord = mr1.y_cord-1
                for t_1 in t_c:
                    t_1.y_cord = t_1.y_cord-1
            elif arr[self.x_cord][self.y_cord+1] == 8 or arr[self.x_cord][self.y_cord+1] == 9 or arr[self.x_cord][self.y_cord+1] == 10:  # mario got killed
                for i_1 in range(11):
                    for i_2 in range(45):
                        if(arr[i_1][i_2] != 2 and arr[i_1][i_2] != 3):
                            if(arr[i_1+a_1][i_2+b_1] != 2 and arr[i_1+a_1][i_2+b_1] != 3):
                                arr[i_1+a_1][i_2+b_1] = arr[i_1][i_2]
                        else:
                            if arr[i_1+a_1][i_2+b_1] != 2:
                                arr[i_1+a_1][i_2+b_1] = 0
                for g_1 in g_c:
                    g_1.y_cord = g_1.y_cord-1
                for cb_1 in cb_c:
                    cb_1.y_cord = cb_1.y_cord-1
                for mr1 in mr_c:
                    mr1.y_cord = mr1.y_cord-1
                for t_1 in t_c:
                    t_1.y_cord = t_1.y_cord-1
                self.lives = self.lives-1  # mario lost live
                self.check_lives(arr)
                if(arr[9][1] != 0 and arr[8][1] == 0):  # set mario's position
                    arr[8][1] = 3
                    self.x_cord = 8
                    self.y_cord = 1
                elif(arr[9][1] != 0 and arr[8][1] == 0):
                    arr[8][2] = 3
                    self.x_cord = 8
                    self.y_cord = 2

        def mario_move(arr, a_1, b_1):  # mario left and right
            """mario move"""
            if arr[self.x_cord+a_1][self.y_cord+b_1] == 0:
                arr[self.x_cord][self.y_cord] = 0
                arr[self.x_cord+a_1][self.y_cord+b_1] = 3
                self.x_cord = self.x_cord+a_1
                self.y_cord = self.y_cord+b_1
            elif arr[self.x_cord+a_1][self.y_cord+b_1] == 8 or arr[self.x_cord+a_1][self.y_cord+b_1] == 9 or arr[self.x_cord+a_1][self.y_cord+b_1] == 10:  # mario got killed
                arr[self.x_cord][self.y_cord] = 0
                arr[self.x_cord+a_1][self.y_cord+b_1] = 0
                self.lives = self.lives-1
                self.check_lives(arr)  # lost life
                if(arr[9][1] != 0 and arr[8][1] == 0):  # set position
                    arr[8][1] = 3
                    self.x_cord = 8
                    self.y_cord = 1
                elif(arr[9][1] != 0 and arr[8][1] == 0):
                    arr[8][2] = 3
                    self.x_cord = 8
                    self.y_cord = 2

        def mario_up(arr, a_1, b_1):  # mario vertical movement
            """marip_up"""
            if arr[self.x_cord+a_1][self.y_cord+b_1] == 0:
                arr[self.x_cord][self.y_cord] = 0
                arr[self.x_cord+a_1][self.y_cord+b_1] = 3
                self.x_cord = self.x_cord+a_1
                self.y_cord = self.y_cord+b_1
            elif a_1 == -1:
                if arr[self.x_cord+a_1][self.y_cord+b_1] == 4:  # collected coin
                    for cb1 in cb_c:
                        if cb1.x_cord == self.x_cord+a_1 and cb1.y_cord == self.y_cord+b_1:
                            subprocess.Popen(['aplay', '-q', './coin.wav'])
                            cb1.kill(arr, sym)
                arr[self.x_cord][self.y_cord] = 0
                arr[self.x_cord+a_1][self.y_cord+b_1] = 3
                self.x_cord = self.x_cord+a_1
                self.y_cord = self.y_cord+b_1
            elif a_1 == 1:
                if arr[self.x_cord+a_1][self.y_cord+b_1] == 8:  # goomba got killed
                    for g_1 in g_c:
                        if g_1.x_cord == self.x_cord+a_1 and g_1.y_cord == self.y_cord+b_1:
                            g_1.kill(arr, sym)

                elif arr[self.x_cord+a_1][self.y_cord+b_1] == 10:  # mushroom got killed
                    for mr1 in mr_c:
                        if mr1.x_cord == self.x_cord+a_1 and mr1.y_cord == self.y_cord+b_1:
                            subprocess.Popen(['aplay', '-q', './kill.wav'])
                            mr1.kill(arr, sym)

                elif arr[self.x_cord+a_1][self.y_cord+b_1] == 9:  # turtle got killed
                    for t_1 in t_c:
                        if t_1.x_cord == self.x_cord+a_1 and t_1.y_cord == self.y_cord+b_1:
                            subprocess.Popen(['aplay', '-q', './kill.wav'])
                            t_1.kill(arr, sym)

                arr[self.x_cord][self.y_cord] = 0
                arr[self.x_cord+a_1][self.y_cord+b_1] = 3
                self.x_cord = self.x_cord+a_1
                self.y_cord = self.y_cord+b_1
            if self.x_cord == 9:  # mario fallen into pit
                self.lives = self.lives-1
                self.check_lives(arr)  # update lives and position
                if arr[9][1] != 0 and arr[8][1] == 0:
                    arr[8][1] = 3
                    self.x_cord = 8
                    self.y_cord = 1
                else:
                    arr[8][2] = 3
                    self.x_cord = 8
                    self.y_cord = 2
        if inp == 'a':  # left
            mario_move(arr, 0, -1)
        elif inp == 'd':  # right
            if self.y_cord < 3:
                mario_move(arr, 0, 1)
            else:
                srceen_shift(arr, 0, -1)
        elif inp == 'w':  # jump
            if arr[self.x_cord-1][self.y_cord] != 7:
                subprocess.Popen(['aplay', '-q', './jump.wav'])
                mario_up(arr, -1, 0)  # mario up
                srceen_shift(arr, 0, -1)  # screen left
                b1.print_board(arr)
                sleep(.2)
                if arr[self.x_cord+1][self.y_cord] == 0 and arr[self.x_cord-1][self.y_cord] != 7:
                    mario_up(arr, -1, 0)  # mario up
                    srceen_shift(arr, 0, -1)  # screen left
                    b1.print_board(arr)
                    sleep(.2)
                    if arr[self.x_cord+1][self.y_cord] == 0 and arr[self.x_cord+1][self.y_cord+1] == 0:
                        srceen_shift(arr, 0, -1)  # screen left
                        mario_up(arr, 1, 0)  # mario down
                        b1.print_board(arr)
                        sleep(.2)
                        if arr[self.x_cord+1][self.y_cord] == 0 and arr[self.x_cord+1][self.y_cord+1] == 0:
                            srceen_shift(arr, 0, -1)  # screen left
                            mario_up(arr, 1, 0)  # mario down
                            b1.print_board(arr)
                            sleep(.2)

        # move down till it rearrches a platform
        while arr[self.x_cord+1][self.y_cord] == 0 or arr[self.x_cord+1][self.y_cord] == 8 or arr[self.x_cord+1][self.y_cord] == 9 or arr[self.x_cord+1][self.y_cord] == 10:
            mario_up(arr, 1, 0)
            b1.print_board(arr)
            sleep(.2)
