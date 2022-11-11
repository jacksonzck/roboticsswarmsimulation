import random

import pygame as pg
import sys
import math

pg.init()
size = width, height = 1920, 1200
screen = pg.display.set_mode(size)
background = pg.image.load("background.bmp").convert()
screen.blit(background, (0, 0))


class Particle:
    image_name = "particle.bmp"
    particles = []
    tolerance = 500
    clumping_potency = 500
    strength_modifier = 1

    def __init__(self, heading, magnitude, x, y):
        self.heading = heading
        self.magnitude = magnitude
        self.image = pg.image.load(Particle.image_name).convert()
        self.pos = self.image.get_rect().move(x, y)

    def move(self):
        self.pos = self.pos.move(self.magnitude / 4 * math.cos(self.heading / 100), self.magnitude / 4 * math.sin(self.heading / 100))
        if 0 > self.pos.x:
            self.pos.x = width
        if width < self.pos.x:
            self.pos.x = 0
        if 0 > self.pos.y:
            self.pos.y = height
        if height < self.pos.y:
            self.pos.y = width

    def turn_to(self, x, y, amount):
        face = math.atan2(y - self.pos.y, x - self.pos.x)
        if face > 0:
            self.heading = self.heading + amount * self.strength_modifier
        else:
            self.heading = self.heading - amount * self.strength_modifier
        pass

    def turn_away(self, x, y, amount):
        x = 2 * self.pos.x - x
        y = 2 * self.pos.y - y
        self.turn_to(x, y, amount)
        pass

    def apply_rules(self):
        self.apply_spacing()
        self.apply_clumping()
        self.apply_alignment()
        self.apply_friction()
        pass

    def apply_spacing(self):
        for particle in Particle.particles:
            self.turn_away(particle.pos.x, particle.pos.y, 1 if self.find_distance(particle) < 20 else (400 / (self.find_distance(particle))**2))
        pass

    def apply_movement(self, x, y, potency):

        pass

    def apply_clumping(self):
        center_x, center_y = Particle.find_center()
        self.turn_to(center_x, center_y, 1)

    def apply_alignment(self):
        alignment = self.find_heading()
        if self.heading > self.find_heading():
            self.heading = self.heading + 1
        else:
            self.heading = self.heading - 1

        pass

    def find_distance(self, other):
        return math.sqrt((self.pos.x - other.pos.x)**2 + (self.pos.y - other.pos.y)**2)

    @staticmethod
    def find_center():
        total_x = 0.0
        total_y = 0.0
        for particle in Particle.particles:
            total_x = total_x + particle.pos.x
            total_y = total_y + particle.pos.y
            pass
        return total_x / len(Particle.particles), total_y / len(Particle.particles)
        pass

    @staticmethod
    def find_heading():
        total_heading = 0
        for particle in Particle.particles:
            total_heading = total_heading + particle.heading
        return total_heading / len(Particle.particles)
        pass

    def apply_friction(self):
        #self.magnitude = self.magnitude / 1.01
        #if 0 < self.x_speed < 1:
        #    self.x_speed = 1
        #elif 0 > self.x_speed > -1:
        #    self.x_speed = -1
        #if 0 < self.y_speed < 1:
        #    self.y_speed = 1
        #elif 0 > self.y_speed > -1:
        #    self.y_speed = -1
        pass

    @staticmethod
    def create_amount(n: int):
        for _ in range(n):
            Particle.particles.append(Particle(2, 5, width / 2, height / 2))




    pass


def main():
    Particle.create_amount(10)

    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        for particle in Particle.particles:
            screen.blit(background, particle.pos, particle.pos)
        for particle in Particle.particles:
            particle.move()
            particle.apply_rules()
            screen.blit(particle.image, particle.pos)
        pg.display.flip()
    pass


if __name__ == '__main__':
    main()
