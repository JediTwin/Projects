# Shoot em up
# Noel Rebiffe
# December 10 2021

import random
import pygame
import time

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
        hp: describes how much health the player has
    """
    def __init__(self) -> None:
        # Call the superclass constructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.image.load("./images/smb_smallmario.png")
        # Scale up player sprite
        self.image = pygame.transform.scale(self.image, (32, 40))

        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()

        # Initial health points
        self.hp = 250

    def hp_remaining(self) -> int:
        """Return the percent of health remaining"""
        return self.hp / 250


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

        self.image = pygame.image.load("./images/spaceinvaders.png")
        # Resize the image
        self.image = pygame.transform.scale(self.image, (56, 40))

        self.rect = self.image.get_rect()
        # Define the initial location
        self.rect.x, self.rect.y = (
            random.randrange(SCREEN_WIDTH),
            random.randrange(int(SCREEN_HEIGHT / 2)),
        )

        # Define initial velocity
        self.x_vel = random.choice([-3, -2, 2, 3])
        self.y_vel = random.choice([-3, -2, 2, 3])

    def update(self) -> None:
        """Calculate movement"""
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        # Constrain movement
        if self.rect.left < 0:
            self.rect.left = 0
            self.x_vel = -self.x_vel
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.x_vel = -self.x_vel
        if self.rect.top < 0:
            self.rect.top = 0
            self.y_vel = -self.y_vel
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.y_vel = -self.y_vel


class Bullet(pygame.sprite.Sprite):
    """Bullet

    Attributes:
        image: visual representation
        rect: mathematical representation
        y_vel: y velocity in px/sec
    """
    def __init__(self, coords: tuple):
        """

        Arguments:
            coords: tuple of (x, y) to represent initial location
        """
        super().__init__()

        self.image = pygame.image.load("./images/bullet.png")
        self.image = pygame.transform.scale(self.image, (18, 18))
        self.rect = self.image.get_rect()

        # Set the middle of the bullet to be at coords
        self.rect.center = coords

        self.y_vel = 6

    def update(self):
        self.rect.y -= self.y_vel


class Bomb(pygame.sprite.Sprite):
    """Bomb

    Attrubutes:
        image: visual representation
        rect: mathematical representation
        y_vel: y velocity in px/sec
    """
    def __init__(self, coords: tuple):
        """

        Arguments:
            coords: tuple of (x, y) to represent the initial location
        """
        super().__init__()

        self.image = pygame.Surface(24, 24)
        self.rect = self.image.get_rect()

        self.rect.center = coords

        self.y_vel = 3

    def update(self):
        self.rect.y -= self.y_vel


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_enemies = 15
    score = 0
    time_start = time.time()
    time_invincible = 3         # seconds
    game_state = "running"
    endgame_wait = 5        # seconds
    time_ended = 0.0
    num_bombs = 1
    round_number = 1

    with open("./data/shmup_highscore.txt") as f:
        high_score = int(f.readline().strip())

    endgame_messages = {
        "lose": "Sorry, they got you. Play again!",
    }

    font = pygame.font.Font("./data/PixeloidSans.ttf", 25)

    # Create a group of sprites to store ALL SPRITES
    all_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()

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
            if event.type == pygame.MOUSEBUTTONUP:
                # Can't create a bullet when:
                if len(bullet_sprites) < 3 and time.time() - time_start > time_invincible:
                    # Create a bullet
                    # Initial location is the top of the player
                    bullet = Bullet(player.rect.midtop)
                    bullet_sprites.add(bullet)
                    all_sprites.add(bullet)

            # TODO: bombs
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                if num_bombs > 0:
                    pass

        if player.hp <= 0:
            game_state = "lose"

            if time_ended == 0.0:
                time_ended = time.time()

            all_sprites.remove(player)

            if time.time() - time_ended >= endgame_wait:
                done = True

        # --------- CHANGE ENVIRONMENT
        # Process Player movement based on mouse pos
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0] - player.rect.width / 2
        player.rect.y = mouse_pos[1] - player.rect.height / 2

        if len(enemy_sprites) < 1:
            for i in range(num_enemies):
                # Create an enemy
                enemy = Enemy()
                # Add it to the sprites list(enemy_sprites, all_sprites)
                enemy_sprites.add(enemy)
                all_sprites.add(enemy)
            num_enemies += 5
            round_number += 1

        # Update the location of all the sprites
        all_sprites.update()

        # Check all collisions between players and the enemies
        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites, False)

        # Remove bullets that leave the screen
        for bullet in bullet_sprites:
            enemies_bullet_collided = pygame.sprite.spritecollide(bullet, enemy_sprites, True)

            if bullet.rect.y < 0:
                bullet.kill()

            if len(enemies_bullet_collided) > 0:
                bullet.kill()
                score += 1

        # Check health
        if time.time() - time_start > time_invincible:
            if game_state == "running":
                for enemy in enemies_collided:
                    player.hp -= 1

        # --------- DRAW THE ENVIRONMENT
        screen.fill(BG_COLOUR)

        # Draw all sprites
        all_sprites.draw(screen)

        # Draw the score on the screen
        screen.blit(
            font.render(f"Score: {score}", True, BLACK),
            (5, 5)
        )

        screen.blit(
            font.render(f"High-score: {high_score}", True, BLACK),
            (5, 28)
        )

        # Draw a health bar
        # Draw the background rectangle
        pygame.draw.rect(screen, GREEN, [580, 5, 215, 20])
        # Draw the foreground rectangle which is the remaining health
        life_remaining = 215 - int(215 * player.hp_remaining())
        pygame.draw.rect(screen, BLUE, [580, 5, life_remaining, 20])

        # Draw lose text
        if game_state == "lose":
            screen.blit(
                font.render(endgame_messages["lose"], True, BLACK),
                (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3)
            )

        # Update screen
        pygame.display.flip()

        # --------- CLOCK TICK
        clock.tick(75)

    # Update the high score if the current score is the highest
    with open("./data/shmup_highscore.txt", "w") as f:
        if score > high_score:
            f.write(str(score))
        else:
            f.write(str(high_score))


if __name__ == "__main__":
    main()