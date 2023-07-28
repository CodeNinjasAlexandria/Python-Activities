# Import necessary modules
import pygame  # Pygame module for creating video games
import time  # Time module to control the game's speed
import random  # Random module to generate random numbers

# Initialize the pygame module, this will start pygame so that we can actually run our game in it
pygame.init()

# Define colors using RGB color codes
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define the display's width and height, we need to make these as variables so they are easier to use in multiple of our other functions
dis_width = 400
dis_height = 400

# Create the game display, this will open a window using our variables from earlier
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')  # Set the window title

# Create a clock object to control the game's speed
clock = pygame.time.Clock()

# Define the size of the snake and the game speed
snake_block = 10
snake_speed = 15

# Define the style of the font for the game, we will use these for our score display and our end screen
font_style = pygame.font.SysFont("freesansbold.ttf", 25)
score_font = pygame.font.SysFont("arial", 35)

# Function to display the score
def score_display(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# The main game function, this contains all of our game logic
def gameLoop():
    # Define initial game states
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Initial change of the position (the snake is still at the beginning)
    x1_change = 0
    y1_change = 0

    # List to hold the Snake's body parts
    snake_List = []
    Length_of_snake = 1

    # Food position (randomly placed)
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # The game loop
    while not game_over:

        # When the game ends, display the "You Lost!" message
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            score_display(Length_of_snake - 1)
            pygame.display.update()

            # Event loop to detect keypresses for quitting or continuing the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event loop to control the snake and quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0

        # If the snake hits the boundary, game ends
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Draw food
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # The snake's head coordinates
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)

        # Append the head to the snake's body
        snake_List.append(snake_Head)

        # When the snake grows, remove the tail
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # If the snake hits itself, game ends
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw the snake and update the score
        our_snake(snake_block, snake_List)
        score_display(Length_of_snake - 1)

        # Update the entire display, this will make sure that what happens in the game gets displayed
        pygame.display.update()

        # If the snake eats the food, reposition the food and grow the snake
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Control the speed of the game
        clock.tick(snake_speed)

    # Quit pygame
    pygame.quit()
    quit()

# Call the main game function, we defined all of our functions but they will not start until this line is run. every line before this is getting the game set up and this is what starts it
gameLoop()
