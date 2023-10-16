# this file was created on 9/19/23 Will Goodman

# import package
import turtle
from turtle import *
# create/start up OS
import os
import random 
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))


from random import randint


# setup the game folders
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height of game window
WIDTH, HEIGHT = 1000, 400
# set up dimensions for pictures
rock_w = 256
rock_h = 280

paper_w = 256
paper_h = 204

scissors_w = 256 
scissors_h = 170


# setup the Screen using turtle
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# set canvas
cv = screen.getcanvas()
# disable window resizing
cv._rootwindow.resizable(False, False)


# setup the rock image, computer's rock image, and their file paths
rock_image = os.path.join(images_folder, 'rock.gif')
rock_instance = turtle.Turtle()
screen.addshape(rock_image)
rock_instance.shape(rock_image)
rock_instance.penup()
rock_pos_x = -300
rock_pos_y = 0
rock_instance.setpos(rock_pos_x,rock_pos_y)
# set aside a different path for computer image
comp_rock = os.path.join(images_folder, 'comp rock.gif')
comp_rock_instance = turtle.Turtle
hideturtle()


# setup the paper image, computer's paper image and their file paths
paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
screen.addshape(paper_image)
paper_instance.shape(paper_image)
paper_instance.penup()
paper_pos_x = 0
paper_pos_y = 0
paper_instance.setpos(paper_pos_x,paper_pos_y)
# specifically set path for seperate computer image
comp_paper = os.path.join(images_folder, 'comp paper.gif')
comp_paper_instance = turtle.Turtle()
hideturtle()

# setup the scissors image/file path for both player and PC
scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
screen.addshape(scissors_image)
scissors_instance.shape(scissors_image)
scissors_instance.penup()
scissors_pos_x = 300
scissors_pos_y = 0
scissors_instance.setpos(scissors_pos_x,scissors_pos_y)
# this sets the path specifically for the PC image
comp_scissors = os.path.join(images_folder, 'comp scissors.gif')
comp_scissors_instance = turtle.Turtle()
hideturtle()

# set up new turtle
t = turtle.Turtle
# set up text turtle, with text color as black
text = turtle.Turtle()
text.color("black")
text.hideturtle()



# this function uses and x y value, an object. it'll determine collision
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False
# sets up the variables for the computer to choose from
choices = ["rock", "paper", "scissors"]
computerInput = choices[randint(0,2)]

'''
the following function mouse_pos, is meant to determine the user's choice based off of which option they choose

'''

def mouse_pos(x,y):
# this portion of the function "mouse_pos" will determine the user's choice, and hide all other choices 
        if collide(x,y, rock_instance, rock_h,rock_w):
            print("you chose rock")
            playerInput = "rock"
            paper_instance.hideturtle()
            scissors_instance.hideturtle()
        elif collide(x,y,paper_instance,paper_h,paper_w):
            print("you chose paper")
            rock_instance.hideturtle()
            scissors_instance.hideturtle()
            playerInput="paper"
            paper_pos_x = -300
            paper_pos_y = 0
            paper_instance.setpos(paper_pos_x, paper_pos_y)
        elif collide(x,y,scissors_instance,scissors_h,scissors_w):
            print("you chose scissors")
            playerInput = "scissors"
            rock_instance.hideturtle()
            paper_instance.hideturtle()
            scissors_pos_x = -300
            scissors_pos_y = 0
            scissors_instance.setpos(scissors_pos_x, scissors_pos_y)
        else:
            print("you chose nothing, choose something dawg")
# the following portion of the "mouse_pos" function will determine the computer's choice and display it
# this will set out the win conditions
        if computerInput == "rock":
            screen.addshape(comp_rock)
            comp_rock_instance.shape(comp_rock)
            comp_rock_instance.penup()
            # this following portion will set the position of the rock image if the computer chooses it
            comp_rock_pos_x = 300
            comp_rock_pos_y = 0
            comp_rock_instance.setpos(comp_rock_pos_x,comp_rock_pos_y)
            # this following portion will tell turtle to write out different messages based on victory or loss
            if playerInput == "scissors":
                print("you suck, Big L")
                turtle.write("you suck, Big L", align="center", font=("Arial",15))  
            elif playerInput == "paper":
                print("you won, good job")
                turtle.write("You won, good job", align="center", font=("Arial",15))  
            elif playerInput == "rock":
                print("you tied bro, get better")
                turtle.write("you tied bro, get better", align="center", font=("Arial",15))  
        elif computerInput == "paper":
            screen.addshape(comp_paper)
            comp_paper_instance.shape(comp_paper)
            comp_paper_instance.penup()
            # this following portion will set the position of the paper image if computer selects it
            comp_paper_pos_x = 300
            comp_paper_pos_y = 0
            comp_paper_instance.setpos(comp_paper_pos_x,comp_paper_pos_y)
            if playerInput == "scissors":
                print("you won, good job")
                turtle.write("You won, good job", align="center", font=("Arial",15))
            elif playerInput == "rock":
                print("you suck, Big L")
                turtle.write("you suck, Big L", align="center", font=("Arial",15))
            elif playerInput == "paper":
                print("you tied bro, get better")
                turtle.write("you tied bro, get better", align="center", font=("Arial",15)) 
        elif computerInput == "scissors":
            screen.addshape(comp_scissors)
            comp_scissors_instance.shape(comp_scissors)
            comp_scissors_instance.penup()
            # again, this will set the position of the scissors image if computer slects it
            comp_scissors_pos_x = 300
            comp_scissors_pos_y = 0 
            comp_scissors_instance.setpos(comp_scissors_pos_x,comp_scissors_pos_y)
            if playerInput == "rock":
                print("you won, good job")
                turtle.write("You won, good job", align="center", font=("Arial",15))
            elif playerInput == "paper":
                print("you suck, Big L")
                turtle.write("you suck, Big L", align="center", font=("Arial",15))
            elif playerInput == "scissors":
                print("you tied bro, get better")
                turtle.write("you tied bro, get better", align="center", font=("Arial",15))
screen.onclick(mouse_pos)
# runs mainloop for Turtle
screen.mainloop()

