import pygame
from pygame.locals import *

import ray_tracer
import world
import player

pygame.init()

WIDTH = 640#1280
HEIGHT = 480#720
TICK_RATE = 60

MOUSE_SENSITIVITY = 0.15

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 15)
tick = 0

def keys_check(player):
    keys = pygame.key.get_pressed()
    player.update(keys, MOUSE_SENSITIVITY)

## -------------------------------------------------------------------------------

player = player.Player(150, 150, 0, 110, 2)

walls = [
    [[0, 0], [200, 0]],
    [[0, 200], [0, 0]],
    [[200, 0], [400, 200]],
    [[400, 200], [400, 400]],
    [[400, 400], [200, 400]],
    [[200, 400], [0, 400]],
    [[0, 400], [0, 200]]]

world = world.World(walls)

rte = ray_tracer.RayTracerEngine(160, 120)

## -------------------------------------------------------------------------------

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

mouse_previous_state = True
running = True
while running:
    screen.fill((100, 100, 100))

    events = pygame.event.get()
    for event in events:

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_r:
                mouse_previous_state = pygame.mouse.set_visible(mouse_previous_state)
                pygame.event.set_grab(mouse_previous_state)

        if event.type == VIDEORESIZE: # Window resize event
            WIDTH = event.w
            HEIGHT = event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    keys_check(player)

    rte.draw(screen, player, world, WIDTH, HEIGHT)



    fps_text = font.render("FPS: " + str(round(clock.get_fps(), 1)), 1, (255, 255, 255))
    screen.blit(fps_text, (10, 5))

    pygame.display.flip()
    clock.tick(TICK_RATE)
    tick += 1
