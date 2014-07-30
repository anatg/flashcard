import random 
from colorama import Fore, Back, Style
import sys
from select import select

deck = {}
deck['a'] = 'a'
deck['b'] = 'b'
deck['c'] = 'c'

'''returns quiz_key, quiz_value'''
def random_pair(deck):
    quiz_key = random.choice(deck.keys())
    quiz_value = deck[quiz_key]
    return quiz_key, quiz_value
    
def deck_loop(deck):
    while True:
        quiz_key, quiz_value = random_pair(deck)
        print quiz_key, ": "
        rlist, _, _ = select([sys.stdin], [], [], 2)
        if rlist:
            supplied_answer = sys.stdin.readline()[:-1]
            if supplied_answer == quiz_value:
                print (Fore.GREEN + u'\u2713'.encode('utf8'))
                print(Fore.RESET + Back.RESET + Style.RESET_ALL)
            elif supplied_answer == ":q" or supplied_answer == "quit":
                print (Fore.BLUE + "good study session")
                print(Fore.RESET + Back.RESET + Style.RESET_ALL)
                sys.exit(0)
            else:
                print (Fore.RED + 'x')
                print(Fore.RESET + Back.RESET + Style.RESET_ALL)
        else:
            print (Fore.YELLOW + "Too slow. Moving on...")
            print(Fore.RESET + Back.RESET + Style.RESET_ALL)

deck_loop(deck)
        
#define a pick random function that returns the key and the value from a dictionary
#in the game loop, serve the key, take the input, check it with the value but timeout after commandline specified number of seconds.
#then work on coloring
#work on reading in a file with the appropriate flashcards -- for now start with builtin emacs


