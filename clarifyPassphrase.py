#!/usr/bin/env python

"""This will parse whatever phrase is pasted in and explain what 
   character it is and whether it is upper or lowercase for better 
   clarity.
"""

import os

__author__ = "Johnathan Viruet"
__copyright__ = "Copyright 2019"
__credits__ = "Johnathan Viruet"

__license__ = "GPL"
__version__ = "1.0.3"
__maintainer__ = "Johnathan Viruet"
__email__ = "johnathanv@gmail.com"
__status__ = "Production"

print("") # For spacing
def parsePass():
	os.system('cls') # Clear the commandline terminal
	print("") # For spacing
	passphrase = input("Copy and paste your password here then press enter: ")
	print("") # For spacing
	for a in passphrase:
		if a.isdigit():
			print(a + " is a number")
		elif a.isalpha():
			if a.islower():
				print(a + " is lowercase")
			elif a.isupper():
				print(a + " is uppercase")
		elif a.isspace():
			print(a + " is space")
		else:
			print(a + " is a symnbol")

	print("") # For spacing
	repeat = input("Would you like to exit (Y/n)? ")
		
	if repeat.upper() == "N":
		parsePass()
	else:
		print("")
		input("Press any key to exit...")
		exit()

parsePass()