# Sert a tout importer



# Fichier src/__init__.py
from .game import Game
from .scenes.menu import MenuScene
from .scenes.game_scene import GameScene

# Fichier src/entities/__init__.py  
from .player import Player
from .enemy import Enemy
from .projectile import Projectile

# Fichier src/scenes/__init__.py
from .menu import MenuScene
from .game_scene import GameScene
from .pause import PauseScene