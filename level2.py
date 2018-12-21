"""LEVEL2 with special enemy character ..cant be killed at once"""

#!/usr/bin/env python

import turtle as t
import level1 as l1
from board import B
import goomba as g
import play as p
import mario as m
import coin_brick as cb
import mushroom as mr
import score as s

STS2 = False

if l1.STS1:#level 1 complete
    S = s.Score()
    M = m.Mario(B, 8, 4, 3)

    T = []
    T.append(t.Turtle(B, 5, 6, 9))
    T.append(t.Turtle(B, 8, 8, 9))

    CB = []
    CB.append(cb.CoinBrick(B, 3, 7, 4))
    CB.append(cb.CoinBrick(B, 6, 5, 4))

    MR = []
    MR.append(mr.Mushroom(B, 4, 17, 10))

    G = []
    G.append(g.Goomba(B, 8, 15, 8))
    G.append(g.Goomba(B, 8, 22, 8))
    STS2 = p.play(B, M, T, CB, MR, G, 2, l1.COUNTER, S)
