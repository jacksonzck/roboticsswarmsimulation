import random

import pygame as pg
import sys

pg.init()
size = width, height = 1920, 1200
screen = pg.display.set_mode(size)
background = pg.image.load("background.bmp").convert()


class Particle:
    image_name = "particle.bmp"
    particles = []
    tolerance = 500

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
        for particle in Particle.particles:
            if particle is not self:
                if particle.pos.x - .1 < self.pos.x < particle.pos.x + .1 and particle.pos.y - .1 < self.pos.y < particle.pos.y + .1:
                    self.x_speed = random.randint(-50, 50)
                    self.y_speed = random.randint(-50, 50)
                    break
                if self.pos.x != particle.pos.x:
                    if self.pos.x > particle.pos.x:
                        self.x_speed = self.x_speed + (Particle.tolerance / (self.pos.x - particle.pos.x)**2)
                    else:
                        self.x_speed = self.x_speed - (Particle.tolerance / (self.pos.x - particle.pos.x) ** 2)
                if self.pos.y != particle.pos.y:
                    if self.pos.y > particle.pos.y:
                        self.y_speed = self.y_speed + (Particle.tolerance / (self.pos.y - particle.pos.y) ** 2)
                    else:
                        self.y_speed = self.y_speed - (Particle.tolerance / (self.pos.y - particle.pos.y) ** 2)

        if self.pos.x != 0:
            self.x_speed = self.x_speed + (Particle.tolerance / (self.pos.x - 0) ** 2)
        if self.pos.y != 0:
            self.y_speed = self.y_speed + (Particle.tolerance / (self.pos.y - 0) ** 2)
        if self.pos.x != width:
            self.x_speed = self.x_speed - (Particle.tolerance / (self.pos.x - width) ** 2)
        if self.pos.y != height:
            self.y_speed = self.y_speed - (Particle.tolerance / (self.pos.y - height) ** 2)

    def apply_friction(self):
        self.x_speed = self.x_speed / 1.07
        self.y_speed = self.y_speed / 1.07
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
