import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
import json
pygame.init()

from src.scenes.blocks import Block
from src.entities.player import Player
from src.entities.player import handle_move

pygame.display.set_caption("Platformer")

WIDTH, HEIGHT = 1000, 800
FPS = 60
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
def draw_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(window.get_width() // width + 1):
        for j in range(window.get_height() // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    for tile in tiles:
        window.blit(image, tile)

    pygame.display.update()
def main(window):
    clock = pygame.time.Clock()

    block_size = 96
    offset_x = 0
    scroll_area_width = 200

    player = Player(100,100,50,50)

    with open("level_one.json", "r") as file:
        map_data = json.load(file)

    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(map_data["width"])]
    floating_blocks = [Block(block["x"], block["y"], block_size)
                       for block in map_data["floating_blocks"]]

    objects = [*floor, *floating_blocks]

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        player.loop(FPS)
        handle_move(player)

        draw_background("Blue.png")
        for obj in objects:
            obj.draw(window, offset_x)
        player.draw(window, offset_x)
        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)