# Import necessary modules
from turtle import *
from freegames import square, vector

# Initialize player positions and directions
# Players are represented as vectors indicating their current positions on the game area
# The direction the players are moving in is also a vector, initially moving right for player 1 and left for player 2
p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()

def inside(head):
    """Return True if head inside screen."""
    # Check if a point is within the bounds of the game area
    return -200 < head.x < 200 and -200 < head.y < 200

def draw():
    """Advance players and draw game."""
    # Move players according to their current direction
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    # Check if players have hit the edge of the screen or the other player's body. If so, game over
    if not inside(p1head) or p1head in p2body:
        print('Player blue wins!')
        return

    if not inside(p2head) or p2head in p1body:
        print('Player red wins!')
        return

    # Add the current position to the player's body
    p1body.add(p1head)
    p2body.add(p2head)

    # Draw players at their new positions
    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    ontimer(draw, 50)

# Game setup
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
# Attach the player control functions to the relevant key press events
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 'd')
onkey(lambda: p2aim.rotate(90), 'j')
onkey(lambda: p2aim.rotate(-90), 'l')
draw()
# Start the event loop
done()
