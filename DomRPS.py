import easygui
import random

easygui.msgbox("Let's play rock paper scissors?")
play = "Yes" # get into while loop

while (play == "Yes"):
    play = easygui.buttonbox("Do you want to play?",choices = ["Yes","No"])
    if (play == "No"):
        break
    # player picks rock paper or scissor as a string
    yourChoice = easygui.buttonbox("Pick One: ", choices = ["Rock", "Paper",
                                                           "Scissors"])
    # computer picks a random choice of rock paper schissors
    computerChoice = random.choice(["Rock", "Paper", "Scissors"])
    easygui.msgbox(computerChoice)
    if (yourChoice == "Rock"):
        if (computerChoice == "Rock"):
            easygui.msgbox("It's a tie!!")
            continue
        elif (computerChoice == "Paper"):
            easygui.msgbox("You lose!!")
            continue
        elif easygui.msgbox("You win!"):
            continue 
    if (yourChoice == "Paper"):
        if (computerChoice == "Paper"):
            easygui.msgbox("It's a tie!!")
            continue
        elif (computerChoice == "Rock"):
            easygui.msgbox("You win!")
        elif easygui.msgbox("You lose!"):
            continue
    if (yourChoice == "Scissors"):
        if (computerChoice == "Scissors"):
            easygui.msgbox("It's a tie!!")
            continue
        elif (computerChoice == "Rock"):
            easygui.msgbox("You lose!")
        elif easygui.msgbox("You win!"):
            continue   
        
"""

        and computerChoice == "Paper"):
        easygui.messagebox("You Lose!! Looooo heeeeseeer!")
        continue
    elif (yourChoice == computerChoice):
        easygui.messagebox("It's a tie!!")
        continue
    elif (yourChoice == "Rock" and computerChoice == "Scissors"):
        easygui.messagebox("You win!"
        continue
    elif (yourChoice == "Paper" and computerChoice == "Rock"):
        easygui.messagebox("You win!"
        continue 
    # play = easygui.buttonbox("Do you want to play?",choices = ["Yes","No"])
"""
