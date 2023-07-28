# Import necessary modules
from random import *
from turtle import *
from freegames import vector

# Initialize bird and balls. The bird is represented as a vector at the center of the game area.
bird = vector(0, 0)
balls = []

def tap(x, y):
    """Move bird up in response to screen tap."""
    # Create a vector representing the "up" direction
    up = vector(0, 30)
    # Move the bird upwards
    bird.move(up)

def inside(point):
    """Return True if point on screen."""
    # Check if a point is within the bounds of the game area
    return -200 < point.x < 200 and -200 < point.y < 200

def draw(alive):
    """Draw screen objects."""
    # Clear the screen
    clear()

    # Move the cursor to the bird's position
    goto(bird.x, bird.y)

    if alive:
        # If the bird is alive, draw a green dot
        dot(10, 'green')
    else:
        # If the bird is dead, draw a red dot
        dot(10, 'red')

    for ball in balls:
        # For every ball in the balls list, move the cursor to its position and draw a black dot
        goto(ball.x, ball.y)
        dot(20, 'black')

    # Update the screen with the newly drawn objects
    update()

def move():
    """Update object positions."""
    # Decrease the bird's y position (making it move downwards on the screen)
    bird.y -= 5

    for ball in balls:
        # Move each ball to the left
        ball.x -= 3

    if randrange(10) == 0:
        # Randomly (1 in 10 chance each frame) add a new ball to the right side of the screen at a random y position
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        # If there are balls and the first one is outside the screen, remove it
        balls.pop(0)

    if not inside(bird):
        # If the bird has hit the edge of the screen, it's game over, so stop moving the bird
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            # If the bird hits a ball, it's game over, so stop moving the bird
            draw(False)
            return

    # If the game isn't over, draw the next frame and schedule the next movement
    draw(True)
    ontimer(move, 50)

# Game setup
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
# Attach the tap function to the screen click event
onscreenclick(tap)
# Start the game
move()
# Start the event loop
done()
