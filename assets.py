import pygame
import os

class AssetLoader:
    """Load and cache images (and other assets) for reuse across the app."""
    def __init__(self, asset_dir="assets", cell_size=50):
        self.asset_dir = asset_dir
        self.cell_size = cell_size
        self.cache = {}

    def load_piece_image(self, piece_name):
        """Returns a pygame.Surface for a piece type, scaled to cell size."""
        if piece_name in self.cache:
            return self.cache[piece_name]
        filename = f"{piece_name}.png"
        path = os.path.join(self.asset_dir, filename)
        try:
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.smoothscale(img, (self.cell_size, self.cell_size))
            self.cache[piece_name] = img
            return img
        except Exception:
            # Fallback: a circle with letter
            surface = pygame.Surface((self.cell_size, self.cell_size), pygame.SRCALPHA)
            pygame.draw.circle(surface, (180, 180, 220), (self.cell_size//2, self.cell_size//2), self.cell_size//2-4)
            font = pygame.font.SysFont("arial", self.cell_size//2)
            letter = piece_name[0].upper()
            text = font.render(letter, True, (0,0,0))
            tw, th = text.get_size()
            surface.blit(text, ((self.cell_size-tw)//2, (self.cell_size-th)//2))
            self.cache[piece_name] = surface
            return surface

    def get_piece_images(self, piece_names):
        """Bulk loads and returns a dict: {piece_name: image}."""
        return {name: self.load_piece_image(name) for name in piece_names}
