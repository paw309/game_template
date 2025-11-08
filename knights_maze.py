import random

class KnightMazeGame:
    """Demo version: Knight moves only, simple board/path."""

    def __init__(self, board_size=8):
        self.n = board_size
        self.reset()

    def reset(self):
        self.pieces = {(4, 3): "knight", (1, 1): "king"}
        self.obstacles = {(6, 2), (2, 4), (3, 5), (4, 1)}
        self.highlights = set()
        self.turn_number = 1
        self.timer_val = 210  # seconds
        self.state = "inprogress"
        self.message = ""

    def format_time(self, t):
        return f"{int(t)//60:02}:{int(t)%60:02}"

    def handle_event(self, event, board_top_left=(300,60), cell_size=50):
        import pygame
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.reset()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            x, y = ((mx - board_top_left[0]) // cell_size, (my - board_top_left[1]) // cell_size)
            if 0 <= x < self.n and 0 <= y < self.n:
                self.highlights = {(x, y)}
                if (x, y) in self.obstacles:
                    self.message = "Blocked!"
                else:
                    self.message = ""
                    self.pieces = {(x, y): "knight"}
                self.turn_number += 1

    def update(self, dt):
        self.timer_val -= dt
        if self.timer_val < 0:
            self.timer_val = 0

    def board_state(self):
        return {
            "grid": (self.n, self.n),
            "pieces": self.pieces,
            "obstacles": self.obstacles,
            "highlights": self.highlights
        }

    def menu_items(self):
        items = [
            {"type": "section", "label": "Game"},
            {"type": "field", "label": "Timer", "value": self.format_time(self.timer_val)},
            {"type": "field", "label": "Turn", "value": str(self.turn_number)},
            {"type": "section", "label": "Status"}
        ]
        if self.message:
            items.append({"type": "message", "value": self.message})
        else:
            items.append({"type": "field", "label": "Knight pos", "value": str(list(self.pieces.keys())[0])})
        return items

    def menu_buttons(self):
        import pygame
        return [
            {"label": "Restart", "rect": pygame.Rect(35, 400, 140, 36), "enabled": True, "action": "restart"},
            {"label": "Quit", "rect": pygame.Rect(35, 450, 140, 36), "enabled": True, "action": "quit"}
        ]
