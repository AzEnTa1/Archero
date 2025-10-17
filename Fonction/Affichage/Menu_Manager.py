# Importation des modules nécessaires
from pygame.locals import *

# Importation des composants personnalisés
from .Home_Menu import *
from .Settings_Menu import *
from .Codex_Menu import *
from .Game_Menu import *


class AppStateManager:

    def __init__(self):
        self.states = {}
        self.active_state = None


    def register_state(self, state):
        if state.name not in self.states:
            self.states[state.name] = state
            

    def run(self, surface, time_delta):
        if self.active_state is not None:
            self.active_state.run(surface, time_delta)

            if self.active_state.quit_game:
                return False

        return True
    
    def set_initial_state(self, name):
        if name in self.states:
            self.active_state = self.states[name]
            self.active_state.start()
