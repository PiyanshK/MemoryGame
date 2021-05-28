import pygame
import random
import sys
from data import MemoryGameData
import time


class Game(MemoryGameData):
       
       def __init__(self, screen: pygame.display, width: int = 1000, height: int = 700) -> None:
              
              self.screen = screen
              self.Width, self.Height = pygame.display.get_surface().get_size()
              self.squares = super().square_start(hieght=self.Height, width=self.Width)
              self.fullsquares = super().fullsquares(self.Height, self.Width)
              self.Images, self.InvImages = super().images()
              self.imagesize = (self.Width // 4, self.Height // 3)
              self.prompts = super().prompts()
              self.clock = pygame.time.Clock()
              self.correct_square = None
       
       def drawlines(self, linecolor: str = "#0320fc", LineWidth: int = 10) -> pygame.display:
              
              width = self.Width
              height = self.Height
              # Width
              
              first_line_y = height / 3
              second_line_y = first_line_y * 2
              
              Widthlines = [first_line_y, second_line_y]
              
              for i in Widthlines:
                     pygame.draw.line(self.screen, linecolor, (0, i), (width, i), LineWidth)
              
              # Hieght
              
              second_line_x = width // 4
              third_line_x = width // 2
              fourth_line_x = second_line_x * 3
              HieghtLines = [second_line_x, third_line_x, fourth_line_x]
              
              for i in HieghtLines:
                     pygame.draw.line(self.screen, linecolor, (i, 0), (i, height), LineWidth)
              
              pygame.display.flip()
       
       def draw_random_image(self, random_image_choice: str = "Mountain", sleeptime: int = 1) -> str:
              
              correct_square = None
              random_image_and_name = random.choice(list(self.Images.items()))
              random_image = random_image_and_name[0]
              name = random_image_and_name[1]
              random_square = random.choice(self.squares)
              random_image = pygame.transform.scale(random_image, self.imagesize)
              self.screen.blit(random_image, tuple(random_square))
              pygame.display.update()
              time.sleep(sleeptime)
              self.screen.fill((0, 0, 0))
              self.drawlines()
              if name == random_image_choice:
                     correct_square = None
                     invimage = self.InvImages[random_image_choice]
                     del self.Images[invimage]
                     self.correct_square = self.squares.index(random_square)
                     self.correct_square += 1
              
              prompt = self.prompts[random_image_choice]
              
              return prompt
       
       def drawscreen(self, difficulty: int = 5, sleeptimer: int = 1) -> pygame.display:
              
              prompt = ""
              current_difficulty = 0
              amount_of_guesses = 1
              
              while current_difficulty != difficulty:
                     event = pygame.event.poll()
                     if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                            current_difficulty = difficulty
                     if event.type == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                     self.drawlines()
                     prompt = self.draw_random_image(sleeptime=sleeptimer)
                     current_difficulty += 1
              
              if self.correct_square == None:
                     print("Game Bug Image did not show up.")
                     print("Restarting...")
                     self.screen.fill((0, 0, 0))
                     pygame.display.update()
                     time.sleep(5)
                     pygame.quit()
                     self.drawscreen(difficulty, sleeptimer)
              else:
                     print(prompt)
                     
                     while True:
                            event = pygame.event.poll()
                            self.screen.fill((0, 0, 0))
                            self.drawlines()
                            if event.type == pygame.QUIT:
                                   pygame.quit()
                                   sys.exit()
                            if event.type == pygame.K_ESCAPE:
                                   pygame.quit()
                                   sys.exit()
                            
                            if event.type == pygame.MOUSEBUTTONUP:
                                   
                                   correct_rect = self.fullsquares[self.correct_square]
                                   if event.button == 1:
                                          if correct_rect.collidepoint(event.pos):
                                                 print("guess : " + str(amount_of_guesses))
                                                 print("Correct!")
                                                 print("You got it right in " + str(amount_of_guesses) + " guess/ess")
                                                 sys.exit()
                                          
                                          else:
                                                 print("guess : " + str(amount_of_guesses))
                                                 amount_of_guesses += 1
                                                 print("That is not the correct square")
