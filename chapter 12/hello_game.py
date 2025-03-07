# # --------------- 12-1
# import sys
# import pygame
# # --------------- 12-2
# from character import Character
#
#
# class BlueBg:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((1200, 800))
#         pygame.display.set_caption("Blue bg")
#         # --------------- 12-1
#
#         self.bg_color = (0, 0, 255)
#         self.character = Character(self)
#
#     def run_game(self):
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()
#             pygame.display.flip()
#             self.screen.fill(self.bg_color)
#             self.character.blitme()
#
#
# if __name__ == '__main__':
#     ai = BlueBg()
#     ai.run_game()
#
# # --------------- 12-3
# do it!!!
#
# # --------------- 12-4
# # Rocket folder
#
# # --------------- 12-5
# # key folder
# # --------------- 12-6
#
