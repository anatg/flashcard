import random 
from colorama import Fore, Back, Style
import sys
from select import select

deck = {}
deck['undo'] = 24,95

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
            if is_correct(supplied_answer,quiz_value):
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

def is_correct(input,char_codes):
    if len(input) == len(char_codes):
        for index,input_char in enumerate(input):
            if input_char != chr(char_codes[index]):
                return False
        return True
    else:
        return False

deck_loop(deck)


