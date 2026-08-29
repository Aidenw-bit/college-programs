"""
Aiden Weldon
10/24/2025
Purpose:To create a program that will simulate a replayable game of Rock-Paper-Scissors
between the user and the computer that will also keep track of the score
"""

#import random
import random

#establish wins, ties, losses
w=0
t=0
l=0
#welcome message
print('Welcome to Rock-Paper-Scissors! In this program you will select' '\n''a move to play in the game, rock, paper, or scissors.')
print('this program will repeat until the user chooses to stop playing')

#establish choices
options= ['rock', 'paper', 'scissors']

#while loop condition
running = True
while running == True:
    #determinng player and computer choices
    pc = None
    cc = random.choice(options)
   
    try:
        pc = input('Please chose an option (rock, paper, scissors):')
        if pc not in options:
            raise ValueError("Invalid choice. Please type rock, paper, or scissors.")
    except ValueError as e:
        print(e)
        continue
    
    
    #display choices
    print('You have chosen ', pc)
    print('Computer has chosen ', cc)
    
    #calculate game result
    if pc == 'rock':
        if cc == 'rock':
            print('You tied')
            t += 1
        elif cc == 'paper':
            print('Paper wraps rock, you lose')
            l += 1 
        else:
            print('rock crushes scissors, you win')
            w += 1
    elif pc == 'paper':
        if cc == 'rock':
            print('paper wraps rock, you win')
            w += 1
        elif cc == 'paper':
            print('You tied')
            t += 1
        else:
            print('scissors cut paper, you lose')
            l += 1
    else:
        if cc == 'rock':
            print('rock crushes scissors, you lose')
            l += 1
        elif cc == 'paper':
            print('scissors cut paper, you win')
            w += 1
        else:
            print('You tied')
            t += 1
    #ask user if they want to keep playing
    playing = input('Would you like to keep playing? y/n')
    if not playing == 'y':
        running = False
#display final scores
print('Your final score is ', w,'/',t,'/',l)
#display ending message
print('Thank you for playing')
print('Program ending...')
    


    