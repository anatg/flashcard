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
#        print "sleeping"
#        time.sleep(1)

get_answer()



