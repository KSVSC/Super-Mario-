"""game play"""

from __future__ import print_function
import os
import subprocess
from time import sleep
import key_input as k
import board as b


def mushroom_movement(mr_mov, arr, n_m, counter):
    """keeping the enemies moving"""

    for i in enumerate(mr_mov):
        if counter % (i[0]+1) == 0:
            mr_mov[i[0]].move_rand(arr, n_m)
            sleep(.002)


def goomba_movement(g_mov, arr, n_m, counter):
    """keeping the enemies moving"""

    for i in enumerate(g_mov):
        if counter % (i[0]+1) == 0:
            g_mov[i[0]].move_rand(arr, n_m)


def play(arr, mar, t_c, cb_c, mr_c, g_c, level, counter, s_u):
    """play start"""
    while 1:
        os.system('clear')
        if arr[mar.x_cord][mar.y+1] == 13:  # level clear
            subprocess.Popen(['aplay', '-q', './stage_clear.wav'])
            print('CONGRATS!!LEVEL :\''+str(level)+'\'CLEARED')
            print('SCORE:'+str(s_u.score))
            return True
        if mar.alive is False:  # mario died
            subprocess.Popen(['aplay', '-q', './die.wav'])
            print('YOU LOST!!   SCORE:'+str(s_u.score))
            print('GAME OVER')
            break
        print('LEVEL:'+str(level))
        print('LIVES:'+str(mar.lives)+' '*50+'SCORE:'+str(s_u.score))
        counter += 1
        mushroom_movement(mr_c, arr, mar, counter)
        goomba_movement(g_c, arr, mar, counter)

        for i in t_c:
            i.move_rand(arr, mar)
        b.print_board(arr)
        sleep(.02)
        key = k.input_to()

        if key == 'q':
            print('SCORE:'+str(s_u.score))
            print('GAME QUIT')
            exit()

        else:
            mar.move(key, arr, cb_c, t_c, mr_c, g_c, s_u)
