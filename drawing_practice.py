import turtle
import random


def main():
    # Create a turtle object
    screen = turtle.Screen()
    screen.colormode(255)
    michelangelo = turtle.Turtle()
    michelangelo.speed(100)
    michelangelo.color((150, 200, 162))
    michelangelo.backward(150)

    # Ask the turtle to move around the canvas
    for i in range(9999999):
        michelangelo.forward(300 + i)
        michelangelo.right(185)
        michelangelo.color((
            (50 + i) % 255,
            (50 + i) % 255,
            (150 + i) % 255
        ))

    turtle.exitonclick()


if __name__ == "__main__":
    main()