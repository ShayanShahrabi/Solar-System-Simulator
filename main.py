import pygame
import math
#-----------------------------------------------------------------------------
# define colors used to draw the planets
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GRAY = (80, 78, 81)
#-----------------------------------------------------------------------------
pygame.init()
WIDTH = HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#-----------------------------------------------------------------------------
pygame.display.set_caption("Solar System Simulation")
#-----------------------------------------------------------------------------
class Planet():
    AU = 149.6e6 * 1000 # astronamical units ~ the distance from earth to sun in meters
    G = 6.67428e-11
    SCALE = 200 / AU  # 1 AU would be about 100 pixels
    TIMESTEP = 3600 * 24  # the update rate of the screen would be 1 day at a time
    #-------------------------------------------------------------------------
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
    #-------------------------------------------------------------------------
    def draw(self, window):
        x = self.x * self.SCALE + (WIDTH / 2)
        y = self.y * self.SCALE + (HEIGHT / 2)
        pygame.draw.circle(window, self.color, (x, y), self.radius)

#-----------------------------------------------------------------------------
def main(): 
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1* Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10 **23)

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GRAY, 0.330 * 10**23)

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 7.8685 * 10**24)

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60)  # set the maximum number of updates in a second
        # WIN.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        for planet in planets:
            planet.draw(WIN)
        
        pygame.display.update()

    pygame.quit()
#-----------------------------------------------------------------------------
main()
