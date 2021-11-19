# Collecting Blocks
# Noel Rebiffe
# 19 November 2021

import pygame

pygame.init()

WHITE     = (255, 255, 255)
BLACK     = (0, 0, 0)
RED       = (255, 0, 0)
RAD_RED   = (255, 56, 188)
GREEN     = (0, 255, 0)
ETON_BLUE = (150, 200, 162)
BLUE      = (0, 0, 255)

BG_COLOUR = WHITE


SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "Collecting Blocks"


class Block(pygame.sprite.Sprite):
    """Describes a block object
    A subclass of pygame.sprite.Sprite

    Attributes:
        image: Surface that is the visual representation of out Block
        rect: numerical representation of our Block [x, y, width, height]
    """
    def __init__(self, colour: tuple, width: int, height: int) -> None:
        """
        Arguments:
        :param colour: 3-tuple (r. g. b)
        :param width: width in pixels
        :param height: height in pixels
        """
        # Call the superclass constructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()

    # Create a group of sprites to store ALL SPRITES
    all_sprites = pygame.sprite.Group()

    # Create the Player Block
    player = Block(ETON_BLUE, 20, 15)
    # Add the Player to all_sprites group
    all_sprites.add(player)

    # ------------- MAIN LOOP
    while not done:
        # --------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # --------- CHANGE ENVIRONMENT
        # Process Player movement based on mouse pos
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0] - 10
        player.rect.y = mouse_pos[1] - 7

        # --------- DRAW THE ENVIRONMENT
        screen.fill(BG_COLOUR)

        # Draw all sprites
        all_sprites.draw(screen)

        # Update screen
        pygame.display.flip()

        # --------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
