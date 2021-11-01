# Midnight Rider

import random
import sys
import textwrap
import time
import midnight_rider_text


# A text-based game of intrigue and illusion

# CONSTANTS
MAX_TOFU = 30
MAX_FUEL = 50


class Game:
    """Represent our game engine

    Attribute:
        done: describes if the game is finished or not - boolean
        distance_travelled: describes the distance that we've travelled so far
        amount_of_tofu: how much tofu we have left in our inventory
        agents_distance: describes the distance between the player and the agents
        fuel: describes the amount of fuel remaining, starts at 50
    """

    def __init__(self):
        self.done = False
        self.distance_travelled = 0
        self.amount_tofu = MAX_TOFU
        self.agents_distance = -20
        self.fuel = MAX_FUEL

    def introduction(self) -> None:
        """Print the introduction text"""
        self.typewriter_effect(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text: str):
        """Print out to console with a typewriter effect"""
        for char in textwrap.dedent(text):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    def show_choices(self) -> None:
        """Show the user their choices"""
        time.sleep(1)
        print(midnight_rider_text.CHOICES)
        time.sleep(1)

    def get_choice(self) -> None:
        """Get the user's choice and changes the environment"""
        # Get the user's response
        user_choice = input().strip(",.?!").lower()

        # Based on their choice, change the attributes of the class
        # TODO: Implement eating/hunger
        agents_distance_now = random.randrange(7, 15)
        if user_choice == "b":
            # Move the player
            player_distance_now = random.randrange(5, 11)
            self.distance_travelled += player_distance_now
            # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now
            # Burn the fuel
            self.fuel -= random.randrange(3, 9)
            # Give player feedback
            print(f"\n-------VROOOOOOM.")
            print(f"-------You travelled {player_distance_now} kms.\n")
        elif user_choice == "c":
            # Move the player
            player_distance_now = random.randrange(10, 16)
            self.distance_travelled += player_distance_now
            # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now
            # Burn the fuel
            self.fuel -= random.randrange(5, 11)
            # Give player feedback
            print(f"\n-------ZOOOOOOOOM.")
            print(f"-------You travelled {player_distance_now} kms.\n")
        elif user_choice == "d":
            # TODO: refuel or recharge
            self.fuel = MAX_FUEL

            # Decide how far the agents go
            self.agents_distance += agents_distance_now

            # Give the user feedback
            print(midnight_rider_text.REFUEL)
        elif user_choice == "e":
            print("---Status Check---")
            print(f"Distance Travelled: {self.distance_travelled} kms")
            print(f"Fuel Remaining: {self.fuel} L")
            print(f"Tofu Left: {self.amount_tofu}")
            print(f"Agent's Distance: {abs(self.agents_distance)} kms behind")
            print("------")
        elif user_choice == "q":
            self.done = True


def main() -> None:
    game = Game()  # starting a new game
    game.introduction()

    # Main Loop:
    while not game.done:
        game.show_choices()
        game.get_choice()
        # TODO: Check win/lose conditions


if __name__ == "__main__":
    main()
