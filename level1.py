"""LEVEL 1 with enemies of different sppeds"""

import turtle as t
from board import A
import play as p
import mario as m
import coin_brick as cb
import mushroom as mr
import score as s

STS1 = False
S = s.Score()
M = m.Mario(A, 8, 3, 3)
COUNTER = 0

T = []
T.append(t.Turtle(A, 8, 7, 9))
T.append(t.Turtle(A, 8, 12, 9))
T.append(t.Turtle(A, 8, 20, 9))

CB = []
CB.append(cb.CoinBrick(A, 7, 3, 4))
CB.append(cb.CoinBrick(A, 5, 6, 4))
CB.append(cb.CoinBrick(A, 6, 19, 4))
CB.append(cb.CoinBrick(A, 6, 20, 4))

MR = []
MR.append(mr.Mushroom(A, 4, 17, 10))
MR.append(mr.Mushroom(A, 8, 18, 10))
MR.append(mr.Mushroom(A, 5, 24, 10))
MR.append(mr.Mushroom(A, 8, 28, 10))

G = []

STS1 = p.play(A, M, T, CB, MR, G, 1, COUNTER, S)
