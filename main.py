# Import the Pygame Zero Library
import pgzrun
from random import randint
import time

# Pygame Standard for deciding the title of your game window
TITLE = "Spaceship Chase"
# Pygame Standard for deciding the width and height for your game window in pixels
WIDTH = 500
HEIGHT = 500

# Variable to store the message displayed on your screen
message = ""
score = 0

# Actor is built-in object in pgzero
spaceship = Actor('spaceship')  # Replace 'spaceship' with the name of the spaceship image file
spaceship.pos = (WIDTH // 2, HEIGHT // 2)  # Initial position at the center

# Default function to update the screen
def draw():
    # Clear the screen and set a background color
    screen.clear()
    screen.fill(color=(0, 0, 128))  # Dark blue background
    # Draw the spaceship and the message
    spaceship.draw()
    screen.draw.text(f"Score: {score}", topleft=(10, 10), fontsize=30, color="white")
    screen.draw.text(message, center=(WIDTH // 2, HEIGHT - 20), fontsize=30, color="yellow")

def move_spaceship():
    """Randomly move the spaceship to a new position on the screen."""
    spaceship.x = randint(50, WIDTH - 50)
    spaceship.y = randint(50, HEIGHT - 50)

def on_mouse_down(pos):
    """Check if the spaceship is clicked."""
    global message, score
    if spaceship.collidepoint(pos):
        message = "Great hit!"
        score += 1
        move_spaceship()  # Move spaceship after a successful click
    else:
        message = "Oops, you missed!"

# Make the spaceship move every second
def update():
    """Update the game state every frame."""
    if time.time() % 1 < 0.02:  # Approximately every 1 second
        move_spaceship()

# Initialize the game with a random position
move_spaceship()

# Start the game
pgzrun.go()
