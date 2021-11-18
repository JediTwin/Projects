# Relaxing Snowscape
# Noel Rebiffe
# 18 November 2021

import pygame
import random

pygame.init()

WHITE =(255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH  = 980
SCREEN_HEIGHT = 540
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "Relaxing Snowscape"

class Snowflake:
    """Snowflake on the screen

    Attributes:
        size: radius of snowflace in px
        coords: {x: int, y: int}
        velocity: falling velocity in px/sec
        colour: (r, g, b)
    """
    def __init__(self):
        self.size = 2
        # randomly place the snow on the screen
        self.coords = [
            random.randrange(0, SCREEN_WIDTH),
            random.randrange(0, SCREEN_HEIGHT),
        ]

        self.y_vel = 2
        self.colour = WHITE


    def update(self):
        """Updates the position of the Snow"""
        self.coords[1] += self.y_vel


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()

    snow = Snowflake()

    # ------------- MAIN LOOP
    while not done:
        # --------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # --------- CHANGE ENVIRONMENT
        snow.update()

        # --------- DRAW THE ENVIRONMENT
        screen.fill(BLACK)

        # Draw the snowflake
        pygame.draw.circle(screen, snow.colour, snow.coords, snow.size)

        # Update screen
        pygame.display.flip()

        # --------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
