import imports


def main():
    imports.pygame.init()
    
    game = imports.Game()
    game.run()

if __name__ == "__main__":
    main()