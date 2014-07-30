import random 
import colorama
import sys
import time

deck = {}
deck['a'] = 'a'
deck['b'] = 'b'
deck['c'] = 'c'


def game_loop():
    while True:
        quiz_key = random.choice(deck.keys())
        supplied_answer = raw_input(quiz_key + ": ")
        if quiz_key == supplied_answer:
            print "great job!"
        elif supplied_answer == ":q" or supplied_answer == "quit":
            #print statistical break down of answers
            print "good study session"
            sys.exit(0)
        else:
            print "another time"            
        time.sleep(5)
print "environment variable: ", (sys.argv[1])
game_loop()


  
