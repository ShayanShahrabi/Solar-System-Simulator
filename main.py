import pygame
import math

pygame.init()

WIDTH = HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Solar System Simulation")

WHITE = (255, 255, 255)

class Planet():
    AU = 149.6e6 * 1000 # astronamical units ~ the distance from earth to sun in meters
    G = 6.67428e-11
    SCALE = 250 / AU  # 1 AU would be about 100 pixels
    TIMESTEP = 3600 * 24  # the update rate of the screen would be 1 day at a time

    def __init__(self, x:int, y:int, radius:int, color, mass:int) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass  # in kilograms

        self.orbit = []  # this list is used to keep track of all the points the planet has gone through to draw a circular orbit around them
        self.sun = False  # check if the planet is Sun of not
        self.distance_to_sun = 0

        self.x_velocity = 0
        self.y_velocity = 0  
        
    def draw(self, window):
        x = self.x * self.SCALE + (WIDTH / 2)
        y = self.y * self.SCALE + (HEIGHT / 2)
        pygame.draw.circle(window, self.color, (x, y), self.radius)


def main(): 
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)  # set the maximum number of updates in a second
        # WIN.fill(WHITE)
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

main()
