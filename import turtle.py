import turtle

def render_word(word):
    # Create a Turtle object
    pen = turtle.Turtle()
    
    # Set the speed of the turtle
    pen.speed(1)
    
    # Move the turtle to the starting position
    pen.penup()
    pen.goto(-100, 0)
    pen.pendown()
    
    # Iterate over each character in the word
    for char in word:
        # Move the turtle forward
        pen.forward(50)
        
        # Rotate the turtle by 90 degrees
        pen.right(90)
        
        # Move the turtle forward again
        pen.forward(50)
        
        # Rotate the turtle by 90 degrees
        pen.right(90)
        
        # Move the turtle forward to create space between characters
        pen.forward(10)
        
    # Hide the turtle
    pen.hideturtle()

# Prompt the user to enter a word
word = input("Enter a word: ")

# Call the function to render the word
render_word(word)

# Keep the turtle window open until it is closed by the user
turtle.done()