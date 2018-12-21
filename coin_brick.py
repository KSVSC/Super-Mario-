"""for class coinbrick"""

import living as l

class CoinBrick(l.Living):
    """def coinbrick"""
    def __init__(self, arr, x_cord, y_cord, b):
        l.Living.__init__(self, arr, x_cord, y_cord, b)

    def clear_obj(self, arr):
        if arr[self.x_cord][self.y_cord] == 4:
            arr[self.x_cord][self.y_cord] = 0

    def kill(self, arr, sym):
        self.alive = False
        sym.score_for_bricks()
        self.clear_obj(arr)
