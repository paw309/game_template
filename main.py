import pygame
from ui.board_renderer import BoardRenderer
from ui.menu_panel import MenuPanel
from assets import AssetLoader
from games.knight_maze_game import KnightMazeGame

def main():
    pygame.init()
    clock = pygame.time.Clock()
    size = (900, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Knight's Maze Modular Example")

    # UI layout config
    board_top_left = (300, 60)
    cell_size = 50
    menu_panel_rect = pygame.Rect(30, 30, 220, 500)

    # Asset and UI loader
    assets = AssetLoader(asset_dir="assets", cell_size=cell_size)
    piece_images = assets.get_piece_images(["knight", "king"])
    board_renderer = BoardRenderer(cell_size=cell_size)
    menu_panel = MenuPanel(rect=menu_panel_rect)
    game = KnightMazeGame(board_size=8)

    running = True
    while running:
        dt = clock.tick(30) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                game.handle_event(event, board_top_left=board_top_left, cell_size=cell_size)
                # Check menu buttons here
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    for btn in game.menu_buttons():
                        if btn['rect'].collidepoint(mx, my):
                            if btn['action'] == 'restart':
                                game.reset()
                            elif btn['action'] == 'quit':
                                running = False

        game.update(dt)

        screen.fill((220, 255, 220))  # Soft green bg
        board_renderer.draw(
            screen, **game.board_state(), piece_images=piece_images, top_left=board_top_left
        )
        menu_panel.draw(screen, game.menu_items(), buttons=game.menu_buttons())
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
