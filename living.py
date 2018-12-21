"""commonn class"""

class Living(object):
    """living"""
    def __init__(self, arr, x_cord, y_cord, b_s):
        """init"""
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.alive = True
        self.symbol = b_s
        self.position(arr, x_cord, y_cord)

    def position(self, arr, x_cord, y_cord):
        """pos"""
        self.x_cord = x_cord
        self.y_cord = y_cord
        arr[self.x_cord][self.y_cord] = self.symbol

    def clear_obj(self, arr):
        """clear_obj"""
        if arr[self.x_cord][self.y_cord] == self.symbol:
            arr[self.x_cord][self.y_cord] = 0

    def kill(self, arr, sym):
        """kill"""
        self.symbol = sym
        self.alive = False
        self.clear_obj(arr)
