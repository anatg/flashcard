import random 
import colorama
import sys
import time
from select import select

#timeout = 10
'''this file was merely to trest the select library'''
def get_answer():
	while True:
		print "Enter something:"
		rlist, _, _ = select([sys.stdin], [], [], 2)
		if rlist:
			s = sys.stdin.readline()
			print s
		else:
			print "No input. Moving on..."

def test_input():
	input = raw_input("type something: ")
	for i in range(0,33):
		if input == chr(i):
			print i
			print input


test_input()


