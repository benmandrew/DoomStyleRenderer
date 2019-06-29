import pygame
from pygame.locals import *

import math

class Player:

    def __init__(self, x, y, angle, fov, speed):

        self.x = x
        self.y = y
        self.angle = angle
        self.fov = fov
        self.speed = speed

    def get_angle(self):
        return self.angle - 90

    def update(self, keys, sensitivity):

        ## Rotation matrix for the player's movement
        rot_matrix = [math.cos(math.radians(self.get_angle())),
                      math.sin(math.radians(self.get_angle())),
                      -math.sin(math.radians(self.get_angle())),
                      math.cos(math.radians(self.get_angle()))]

        ## Get the standard unit movement vectors
        move_vec = [0, 0]
        if keys[K_w]:   move_vec[1] = self.speed
        elif keys[K_s]: move_vec[1] = -self.speed
        if keys[K_a]:   move_vec[0] = self.speed
        elif keys[K_d]: move_vec[0] = -self.speed

        ## Makes sure diagonal speed is the same speed as lateral speed
        if move_vec[0] != 0 and move_vec[1] != 0:
            move_vec[0] *= 1/math.sqrt(2)
            move_vec[1] *= 1/math.sqrt(2)

        ## Multiply the unit movement vector by the rotation matrix to get the player's x y movement
        move_vec = [
            move_vec[0] * rot_matrix[0] + move_vec[1] * rot_matrix[2],
            move_vec[0] * rot_matrix[1] + move_vec[1] * rot_matrix[3]]

        ## Apply movement
        self.x += move_vec[0]
        self.y += move_vec[1]

        ## Get the change in x position of the mouse since last check, and change the angle by it
        x_angular_movement = pygame.mouse.get_rel()[0]
        self.angle += x_angular_movement * sensitivity ## This is how mouse sensitivity is done, right?



































