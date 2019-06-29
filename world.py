from random import randint
import math

class World:

    def __init__(self, walls):

        self.walls = walls

        possible_colours = [
            (153, 51, 0),
            (153, 204, 153),
            (0, 51, 102)]

        self.wall_colours = list()
        for i in range(len(walls)):
            r = randint(0, 255)
            g = randint(0, 255-r)
            b = 255-r-g
            self.wall_colours.append((r, g, b))#possible_colours[randint(0, len(possible_colours)-1)])

    ## Sort the walls by their distance from the player
    def sort_walls(self, player):

        distance_list = list()
        for wall in self.walls:
            distance_list.append(
                distance(
                    get_middle(wall),
                    [player.x, player.y]))

        for i in range(1, len(self.walls)):
            j = i
            while j > -1 and distance_list[j-1] < distance_list[j]:
                distance_list[j], distance_list[j-1] = distance_list[j-1], distance_list[j]
                self.walls[j], self.walls[j-1] = self.walls[j-1], self.walls[j]
                self.wall_colours[j], self.wall_colours[j-1] = self.wall_colours[j-1], self.wall_colours[j]

    def parse_map(self, file_name):

        pass













## Find the middle point of a line
def get_middle(line):
    p1 = line[0]
    p2 = line[1]
    x = (p1[0] + p2[0])/2
    y = (p1[1] + p2[1])/2
    return [x, y]

## Distance between two points
def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


























