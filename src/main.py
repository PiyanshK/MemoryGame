from game import Game
import pygame
import time


def main() -> pygame.display:
       screen = pygame.display.set_mode((1000, 700))
       pygame.display.set_caption('MemoryGame')
       MainGame = Game(screen)
       MainGame.drawscreen(difficulty = int(input("What difficulty would you like to play on: ")), sleeptimer = float(input("How much time would you like between each image: ")))
       time.sleep(5)

if __name__ == '__main__':
       main()
