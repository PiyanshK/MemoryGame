import pygame


class MemoryGameData:
       
       def square_start(self, hieght: int, width: int) -> [[int, int]]:
              
              first_x = 0
              second_x = width / 4
              third_x = width / 2
              fourth_x = second_x * 3
              first_y = hieght / 3
              second_y = first_y * 2
              return [
                  [first_x, 0],
                  [second_x, 0],
                  [third_x, 0],
                  [fourth_x, 0],
                  [first_x, first_y],
                  [second_x, first_y],
                  [third_x, first_y],
                  [fourth_x, first_y],
                  [first_x, second_y],
                  [second_x, second_y],
                  [third_x, second_y],
                  [fourth_x, second_y],
              ]
       
       def fullsquares(self, hieght: int, width: int) -> {int: pygame.Rect}:
              numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
              fullsquares = {}
              squares_start = self.square_start(hieght, width)
              for square_start in squares_start:
                     square_index = squares_start.index(square_start)
                     number = numbers[square_index]
                     fullsquares[number] = pygame.Rect(square_start[0], square_start[1], width // 4, hieght // 3)
              
              return fullsquares
       
       def prompts(self) -> {str: str}:
              return {
                  "Pencil":
                  "Click On the square where you saw the yellow Pencil.",
                  "Mountain":
                  "Click On the square where you saw the Tall White Mountain.",
                  "Numbers":
                  "Click On the square where you saw the Numbers surronded by the red circles.",
                  "Letters":
                  "Click On the square where you saw the the letters in the yellow box.",
              }
       
       def images(self) -> {str: pygame.surface}:
              images = {"Pencil": pygame.image.load("../assets/pencil.jpg"),
                        "Mountain": pygame.image.load("../assets/Mountain.jpg"),
                        "Numbers": pygame.image.load("../assets/Numbers.jpg"),
                        "Letters": pygame.image.load("../assets/Letters.jpg")}
              inv_images = {v: k for k, v in images.items()}
              
              return inv_images, images
