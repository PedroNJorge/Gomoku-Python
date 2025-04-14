import pygame


class InputHandler:
    def __init__(self, board, game_logic):
        self.board = board
        self.game_logic = game_logic

    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return False    # used to update run in main.py
                case pygame.MOUSEMOTION | pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse(event)

        return True

    def handle_mouse(self, event):
        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
