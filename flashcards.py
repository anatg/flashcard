import random 
import colorama

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
        else:
            print "another time"            

game_loop()
  
