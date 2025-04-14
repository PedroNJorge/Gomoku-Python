class GameLogic:
    def __init__(self, board):
        self.board = board
        self.winner = None

    def check_win(self, board):
        return self.board.check_win()

    def update(self):
        if self.winner is not None:
            print("win", self.winner)
