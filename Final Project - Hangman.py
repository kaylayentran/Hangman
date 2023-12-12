import turtle
import random

def drawMan(x):
    guess = x
    if guess == 1: 
        turtle.goto(-74, 140)
        turtle.pendown()
        turtle.right(90)
        turtle.circle(15,None,100)
        turtle.penup()
    elif guess == 2:
        turtle.goto(-74, 140)
        turtle.pendown()
        turtle.left(90)
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
        turtle.forward(40)
        turtle.right(180)
        turtle.forward(30)
        turtle.penup()
    elif guess == 3:
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    elif guess == 4:
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(70)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    elif guess == 5:
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(30)
        turtle.right(30)
        turtle.forward(60)
        turtle.right(180)
        turtle.forward(60)
        turtle.penup()
    elif guess == 6:
        turtle.goto(-74, 70)
        turtle.pendown()
        turtle.right(120)
        turtle.forward(60)
        turtle.penup()

turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)

wordbank = ['lemon','stewardess','cat','mouse','chocolate',
            'monster','christmas','daiquiri','margarita','santa',
            'bjorn','light','bear','valorant','overwatch',
            'gallop','league','legends','rabbit','blanket',
            'bright','jeans','strawberry','rhubarb','toilet',
            'center','city','partake','conditioner','shampoo']

bored = False
while not bored:

    turtle.home()
    turtle.pendown()
    turtle.left(90)
    turtle.forward(175)
    turtle.left(90)
    turtle.forward(74)
    turtle.left(90)
    turtle.forward(35)
    turtle.penup()
    turtle.goto(-135,-35)
    
    word = random.choice(wordbank)

    for i in word:
        turtle.write('_ ', True, font=("Courier", 14, "normal"))

    correct = []
    wrong = 0
    terminate = False
    while wrong < 6 and not terminate:
        letter = turtle.textinput('Hangman','Guess a letter:')
        turtle.goto(-135,-35)
        if letter not in correct:
            for i in word:
                if i == letter:
                    turtle.write(letter.upper() + ' ', True, font=("Courier", 14, "normal"))
                    correct += letter
                else:
                    turtle.write('_ ', True, font=("Courier", 14, "normal"))  
        if letter not in word:
            wrong += 1
            drawMan(wrong)
        if wrong == 6:
            turtle.goto(-135,-35)
            for i in word:
                if i in correct:
                    turtle.write('_ ', True, font=("Courier", 14, "normal"))
                else:
                    turtle.write(i.upper() + ' ', True, font=("Courier", 14, "normal"))
            turtle.goto(-74, -60)
            turtle.write('Sorry, you lose!', False, align='center', font=("Courier", 14, "normal"))
        if len(correct) == len(word):
            turtle.goto(-74, -60)
            turtle.write('Congratulations!', False, align='center', font=("Courier", 14, "normal"))
            terminate = True

    response = turtle.textinput('Hangman','Would you like to play again? (y or n): ')
    while response != 'y' and response != 'n':
        response = turtle.textinput('Hangman','Please enter "y" or "n": ')
    if response == 'y':
        turtle.clear()
    elif response == 'n':
        turtle.clear()
        turtle.home()
        turtle.write('Thanks for playing!', False, align='center', font=("Courier", 25, "normal")) 
        bored = True



