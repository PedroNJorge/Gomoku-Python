import sys
from game import Board
from game import GameLogic
from game import InputHandler
# from game import Renderer


def main():
    board = Board()
    game_logic = GameLogic(board)
    input_handler = InputHandler(board, game_logic)
    """
    renderer = Renderer(board, game_logic, input_handler)

    renderer.run()
    sys.exit()
    """
    dic = {"WHITE": "BLACK", "BLACK": "WHITE"}
    player = "WHITE"
    run = True
    print(board)
    while run:
        print(player)
        pos = tuple(map(int, input("Place Stone: ").split()))
        if board.place_stone(pos, player):
            break
        player = dic[player]
        print(board)

    sys.exit()


if __name__ == "__main__":
    main()
