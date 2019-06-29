import pygame
import math
import sys
#import time

class RayTracerEngine:

    def __init__(self, width, height):

        self.width = width
        self.height = height

    ## Rendering uses raycasting
    def draw(self, screen, player, world, screen_width, screen_height):

        ## Sort the walls by the distance between the player and their midpoints
        world.sort_walls(player)

        ## Iterate over the rays emmitted from the player, one for each pixel
        for ray_num in range(self.width):
            ## Calculate the angle of the ray
            ray_angle = player.angle + (player.fov / self.width) * (ray_num - self.width/2)

            ## Calculate the x y coordinates of the ray, extended far enough to stop the non-rendering of far walls
            ray = [
                [player.x, player.y],
                [player.x + 10000 * math.cos(math.radians(ray_angle)),
                 player.y + 10000 * math.sin(math.radians(ray_angle))]]

            for i, wall in enumerate(world.walls):

                intersection = get_line_intersection(ray, wall)
                ## No intersection
                if intersection == 0:
                    continue

                distance = (math.sqrt(
                    (intersection[0] - player.x)**2 + (intersection[1] - player.y)**2))
                wall_height = min(20000 / (distance if distance != 0 else 1/sys.maxsize), screen_height)

                column_x = int(ray_num * (screen_width / self.width))
                column_y = round_up(int(screen_height / 2 - wall_height / 2), screen_height / self.height)
                column_width = round_up(int(screen_width / self.width), screen_height / self.height)
                column_height = round_up(int(wall_height), screen_height / self.height)

                ## Draw wall section
                pygame.draw.rect(
                    screen,
                    world.wall_colours[i],
                    (column_x, column_y, column_width, column_height))

## http://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
## Line-line intersection
def get_line_intersection(l1, l2):
    p1 = l1[0]
    p2 = l1[1]
    p3 = l2[0]
    p4 = l2[1]

    s1_x = p2[0] - p1[0]
    s1_y = p2[1] - p1[1]
    s2_x = p4[0] - p3[0]
    s2_y = p4[1] - p3[1]

    ## If-else statements prevent division by 0 error
    s = (-s1_y * (p1[0] - p3[0]) + s1_x * (p1[1] - p3[1])) / ((-s2_x * s1_y + s1_x * s2_y) if (-s2_x * s1_y + s1_x * s2_y) != 0 else 1/sys.maxsize)
    t = (s2_x * (p1[1] - p3[1]) - s2_y * (p1[0] - p3[0])) / ((-s2_x * s1_y + s1_x * s2_y) if (-s2_x * s1_y + s1_x * s2_y) != 0 else 1/sys.maxsize)

    if s >= 0 and s <= 1 and t >= 0 and t <= 1:
        ## Collision detected
        i_x = p1[0] + (t * s1_x)
        i_y = p1[1] + (t * s1_y)
        return [i_x, i_y]

    return 0 ## No collision

## Round number to the nearest multiple of the other number
def round_up(num_to_round, multiple):
    if multiple == 0:
        return num_to_round

    remainder = num_to_round % multiple
    if remainder == 0:
        return num_to_round

    return num_to_round + multiple - remainder



























