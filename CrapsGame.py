#!/usr/bin/env python3
#Creation of a Craps gambling game#
from random import randint

#CLASSES:
class Gambler(object):
	def __init__(self,name,cash):
		self.name = str(name)
		self.cash = int(cash)
	def __repr__(self):
		return '%s has $%i' % (self.name, self.cash)
	
	def rollDice(self):
		dice = randint(1,6) + randint(1,6)
		return dice

		
		
#************TESTS*************#
testGambler = Gambler('Frederick',2000)
print(testGambler)
print(testGambler.rollDice())
