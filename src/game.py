import pygame
import pygame_gui
from src.scenes.menu_scene import MenuScene
from src.scenes.game_scene import GameScene
from src.utils.constants import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Archero 2")
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # Gestion des scènes
        self.current_scene = MenuScene(self)
        
    def run(self):
        while self.running:
            time_delta = self.clock.tick(FPS) / 1000.0
            
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                self.ui_manager.process_events(event)
                self.current_scene.handle_events(event)
            
            # Mise à jour
            self.current_scene.update(time_delta)
            self.ui_manager.update(time_delta)
            
            # Rendu
            self.screen.fill((0, 0, 0))
            self.current_scene.render(self.screen)
            self.ui_manager.draw_ui(self.screen)
            
            pygame.display.flip()
        
        pygame.quit()
    
    def change_scene(self, new_scene):
        self.current_scene = new_scene