import sys
import random
from enum import Enum

def play_rsp():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3  
             
    print('')
    playerchoice = input('Enter \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n')
    
    if playerchoice not in ['1','2','3']:
        print('You must enter 1, 2 or 3')
        return play_rsp()
    
    player = int(playerchoice)
    computercoice = random.choice('123')
    computer = int(computercoice)

    print('')
    print('You chose ' + playerchoice)
    print('Python chose ' + computercoice)
    print('')

    if player == 1 and computer == 3:
        print('🎉 You win!')
    elif player == 2 and computer == 1:
        print('🎉 You win!')
    elif player == 3 and computer == 2:
        print('🎉 You win!')
    elif player == computer:
        print('😉 Tie game')
    else:
        print('🐍 Python wins!')
        
    print('\nPlay again?')
    
    while True:
        playagain = input('\nY for Yes or \nQ to Quit\n')
        if playagain.lower() not in ['y','q']:
            continue
        else:
            break
    
    if playagain.lower() == 'y':
        return play_rsp()
    else:
        print('\n🎉🎉🎉💕')
        sys.exit('Bye! 🙋‍♀️')
        
play_rsp()