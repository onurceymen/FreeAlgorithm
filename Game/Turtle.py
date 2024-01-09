import turtle
import random

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")

# Define font for the game
FONT = ('Arial', 30, 'normal')

# Initialize score and game state variables
score = 0
game_over = False

# List to store turtles
turtle_list = []

# Create a turtle for displaying the score
score_turtle = turtle.Turtle()

# Create a turtle for the countdown
countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    # Set up the score turtle's properties
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    # Position the score turtle at the top center of the screen
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setpos(0, y)

    # Display initial score
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

# Size of the grid for positioning turtles
grid_size = 10

def make_turtle(x, y):
    # Create a turtle at a specified position on the grid
    t = turtle.Turtle()

    def handle_click(x, y):
        # Callback function when a turtle is clicked
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

    # Set up the turtle's click event
    t.onclick(handle_click)

    # Set up turtle properties
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("black")
    t.goto(x * grid_size, y * grid_size)

    # Add the turtle to the list
    turtle_list.append(t)

# Coordinates for placing turtles
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]

def setup_turtles():
    # Create turtles at specified positions
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    # Hide all turtles in the list
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    # Display a random turtle from the list
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        # Schedule the function to run again after a delay
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    # Set up the countdown turtle's properties
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setpos(0, y - 30)
    countdown_turtle.clear()

    if time > 0:
        # Display the remaining time and schedule the function to run again after a delay
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        # End the game when the countdown reaches zero
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)

def start_game_up():
    # Initialize the game settings
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)

# Start the game
start_game_up()
turtle.mainloop()
