""" holds score"""

class Score(object):
    """update score"""
    def __init__(self):
        self.score = 0

    def score_for_bricks(self):
        """brick"""
        self.score = self.score + 10

    def score_for_mushroom(self):
        """mushroom"""
        self.score = self.score + 20

    def score_for_turtle(self):
        """turtle"""
        self.score = self.score + 50

    def score_for_goomba(self):
        """goomba"""
        self.score = self.score + 100
