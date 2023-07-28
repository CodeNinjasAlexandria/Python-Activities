# Import necessary modules
from random import *
from turtle import *
from freegames import path

# Load an image for the background
car = path('car.gif')

# The game consists of 32 pairs of tiles, each denoted by a number from 0 to 31
tiles = list(range(32)) * 2

# The game state consists of a single 'marked' tile, initially none
state = {'mark': None}

# List to keep track of which tiles are hidden
hide = [True] * 64

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    # The function to draw a square at a given (x,y) position
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    # Function to convert x,y coordinates into the index of the tile in the tiles list
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    # Function to convert tile index into x,y coordinates
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    # Function to respond to a tap event. If the tapped tile matches the marked tile, both are revealed. Otherwise, the tapped tile becomes the marked tile.
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    """Draw image and tiles."""
    # Function to draw the game, including the background image and all of the tiles.
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

# Shuffle the tiles randomly
shuffle(tiles)

# Set up the window, with the car image added as a possible shape
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)

# Register the tap function to run when the screen is clicked
onscreenclick(tap)

# Run the draw function once every 100 ms
draw()
done()
