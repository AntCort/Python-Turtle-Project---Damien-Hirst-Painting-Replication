from turtle import Turtle, Screen
import random
from color_extraction import ColorExtractor

class TurtlePainter:
    def __init__(self):
        # Initialize the turtle
        self.timmy_the_turtle = Turtle()
        self.timmy_the_turtle.speed(10)
        
        # Set up the screen
        self.screen = Screen()
        self.color_extractor = ColorExtractor()
    # Creating the function that will re-create painting
    def create_painting(self, amount_of_rows, amount_of_dots): # Parameters for the amount of rows and dots per row
        # Extract colors from the image
        colors = self.color_extractor.extract_colors()
        x = 0
        y = 0
        # Takes the amount of rows from Parameter 'amount_of_rows'  
        for i in range(amount_of_rows):
            self.timmy_the_turtle.penup()
            self.timmy_the_turtle.goto(x, y)
            # Takes the amount of dots from Parameter 'amount_of_dots'
            for j in range(amount_of_dots):
                # Chooses random color from list and assigns it to the 
                # dot being marked on the canvas
                rand_pen = random.choice(colors)
                self.timmy_the_turtle.dot(25, rand_pen)
                self.timmy_the_turtle.forward(50)
                # Updating the position for the Turtle   
            y += 50

        # Close the turtle graphics window when clicked
        self.screen.exitonclick()
