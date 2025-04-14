import pygame

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BOARD_COLOR = pygame.Color("#AD6D3F")
GRID_COLOR = pygame.Color("#704D0E")
WHITE = pygame.Color("#F5F5F5")
BLACK = pygame.Color("#2A2A2A")

MAIN_MENU = 0
RULES = 1
PLAY_SELECT = 2
HUMAN_HUMAN = 3
HUMAN_AI = 4
AI_AI = 5
AI_SELECT = 6
PLAYING = 7
WINNER = 8

font_electroharmonix = pygame.font.Font("../assets/fonts/Electroharmonix.otf", 24)


class Button:
    def __init__(self, x, y, width, height, color, hover_color, text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = None
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False

    def draw(self, screen):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        pygame.draw.rect(screen, BLACK, self.rect, 2, border_radius=10)

        font = pygame.font.Font(None, 32)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


class Renderer:
    def __init__(self, board, game_logic, input_handler):
        self.board = board
        self.game_logic = game_logic
        self.input_handler = input_handler
        self.running = True
        self.game_state = MAIN_MENU
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Gomoku")
        self.clock = pygame.time.Clock()

    def init_buttons(self):
        # MAIN_MENU
        # x, y, width, height, color, hover_color, text_color=BLACK
        self.button_main_menu = Button(100, 100, 100, 100, 0, 0,)

    def draw(self):
        self.screen.fill(BOARD_COLOR)
        match self.game_state:
            case MAIN_MENU:
                self.draw_main_menu()

        pygame.display.flip()

    def draw_main_menu(self):
        self.button_main_menu.draw()

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.running = self.input_handler.handle_events()
            if self.game_logic.winner is not None:
                self.running = False
                self.game_state = WINNER

            self.draw()
            pygame.time.delay(1000)
        pygame.quit()
