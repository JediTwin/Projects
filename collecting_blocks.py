# Collecting Blocks
# Noel Rebiffe
# 19 November 2021

import random
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


class Player(pygame.sprite.Sprite):
    """Describes the player object
    A subclass of pygame.sprite.Sprite

    Attributes:
        image: Surface that is the visual representation of out Block
        rect: numerical representation of our Block [x, y, width, height]
    """
    def __init__(self) -> None:
        """
        Arguments:
        :param colour: 3-tuple (r. g. b)
        :param width: width in pixels
        :param height: height in pixels
        """
        # Call the superclass constructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.image.load("./images/smb_smallmario.png")

        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()


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


class Enemy(pygame.sprite.Sprite):
    """The enemy sprites

    Attributes:
        image: Surface that is the visual representation of the sprite
        rect: Rect (x, y, width, height)
        x_vel: x velocity
        y_vel: y velocity
    """
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/smb_goomba.png")
        # Resize the image
        self.image = pygame.transform.scale(self.image, (91, 109))

        self.rect = self.image.get_rect()
        # Define the initial location
        self.rect.x, self.rect.y = (
            random.randrange(SCREEN_WIDTH),
            random.randrange(SCREEN_HEIGHT),
        )

        # Define initial velocity
        self.x_vel = random.choice([-4, -3, 3, 4])
        self.y_vel = random.choice([-4, -3, 3, 4])


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_blocks = 100
    num_enemies = 10
    score = 0

    # Create a group of sprites to store ALL SPRITES
    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()

    # Create all the block sprites and add to block_sprites
    for i in range(num_blocks):
        # Create a block (set its parameters)
        block = Block(BLACK, 20, 15)

        # Set a random location for the block inside the screen
        block.rect.x = random.randrange(SCREEN_WIDTH-block.rect.width)
        block.rect.y = random.randrange(SCREEN_HEIGHT-block.rect.height)

        # Add the block to the block_sprite Group
        # Add the block to the all_sprites Group
        block_sprites.add(block)
        all_sprites.add(block)

    # Create enemy sprites
    for i in range(num_enemies):
        # Create an enemy
        enemy = Enemy()

        # Add it to the sprites list(enemy_sprites, all_sprites)
        enemy_sprites.add(enemy)
        all_sprites.add(enemy)

    # Create the Player Block
    player = Player()
    # Add the Player to all_sprites group
    all_sprites.add(player)

    pygame.mouse.set_visible(False)

    # ------------- MAIN LOOP
    while not done:
        # --------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # --------- CHANGE ENVIRONMENT
        # Process Player movement based on mouse pos
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0] - 6
        player.rect.y = mouse_pos[1] - 8

        # Check all collisions between players and the blocks
        blocks_collided = pygame.sprite.spritecollide(player, block_sprites, True)
        for block in blocks_collided:
            score += 1
            print(f"Score: {score}")

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
