SIZE = 15


class Board:
    def __init__(self):
        self.layout = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

    def check_win(self):
        return True
