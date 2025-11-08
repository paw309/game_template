import pygame

class MenuPanel:
    def __init__(self, rect, font=None, colors=None):
        self.rect = rect
        self.font = font or pygame.font.SysFont("arial", 22)
        self.colors = colors or {
            "background": (255, 255, 240),
            "section": (220, 220, 250),
            "text": (0, 0, 0),
            "button": (59, 72, 195),
            "button_text": (255, 255, 255),
            "button_disabled": (180, 180, 180),
            "highlight": (0, 150, 0),
        }

    def draw(self, surface, menu_items, buttons=None):
        pygame.draw.rect(surface, self.colors["background"], self.rect)
        pygame.draw.rect(surface, (102, 51, 0), self.rect, 4)
        padding = 12
        y = self.rect.top + padding

        for entry in menu_items:
            if entry.get("type") == "section":
                section_rect = pygame.Rect(self.rect.left + 6, y, self.rect.width - 12, self.font.get_height() + 6)
                pygame.draw.rect(surface, self.colors["section"], section_rect)
                label = entry["label"].upper()
                txt = self.font.render(label, True, (40,40,80))
                surface.blit(txt, (section_rect.left + 8, y + 3))
                y += self.font.get_height() + 10
            elif entry.get("type") == "field":
                label = entry["label"]
                value = entry.get("value", "")
                line = f"{label}: {value}"
                txt = self.font.render(line, True, self.colors["text"])
                surface.blit(txt, (self.rect.left + padding, y))
                y += self.font.get_height() + 4
            elif entry.get("type") == "message":
                txt = self.font.render(entry["value"], True, (120,30,30))
                surface.blit(txt, (self.rect.left + padding, y))
                y += self.font.get_height() + 4

        if buttons:
            y += 8
            for btn in buttons:
                btn_rect = btn["rect"]
                color = self.colors["button"] if btn.get("enabled", True) else self.colors["button_disabled"]
                if btn.get("highlight", False):
                    color = self.colors["highlight"]
                pygame.draw.rect(surface, color, btn_rect)
                btn_label = self.font.render(btn["label"], True, self.colors["button_text"])
                tw, th = btn_label.get_size()
                surface.blit(btn_label, (
                    btn_rect.left + (btn_rect.width - tw) // 2,
                    btn_rect.top + (btn_rect.height - th) // 2
                ))
