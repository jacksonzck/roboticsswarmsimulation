import random

import pygame as pg
import sys
import math

pg.init()
size = width, height = 1920, 1200
screen = pg.display.set_mode(size)
background = pg.image.load("background.bmp").convert()


class Particle:
    image_name = "particle.bmp"
    particles = []
    tolerance = 500
    clumping_potency = 500

    def __init__(self, x_speed, y_speed, x, y):
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.image = pg.image.load(Particle.image_name).convert()
        self.pos = self.image.get_rect().move(x, y)

    def move(self):
        self.pos = self.pos.move(self.x_speed, self.y_speed)
        if 0 > self.pos.x:
            self.x_speed = -self.x_speed
            self.pos.x = 0
        if width < self.pos.x:
            self.x_speed = -self.x_speed
            self.pos.x = width
        if 0 > self.pos.y:
            self.y_speed = -self.y_speed
            self.pos.y = 0
        if height < self.pos.y:
            self.y_speed = -self.y_speed
            self.pos.y = height

    def apply_rules(self):
        self.apply_spacing()
        self.apply_friction()
        pass

    def apply_spacing(self):
        pass

    def apply_movement(self, x, y, potency):

        pass

    def apply_clumping(self):
        center_x, center_y = Particle.find_center()
        self.x_speed = self.x_speed
        # movement

    def apply_alignment(self):
        pass

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
        total_x = 0.0
        total_y = 0.0
        for particle in Particle.particles:
            total_x = total_x + particle.pos.x
            total_y = total_y + particle.pos.y
            pass
        return total_x / len(Particle.particles), total_y / len(Particle.particles)
        pass
    def apply_friction(self):
        self.x_speed = self.x_speed / 1.1
        self.y_speed = self.y_speed / 1.1
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
            Particle.particles.append(Particle(2, 2, width / 2, height / 2))




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
