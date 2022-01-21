#!/usr/bin/env python3
#Creation of a Craps gambling game#
from random import randint

#CLASSES:
class Gambler(object):
	bets = {"ComeLine":0,"PassLine":0,"4":0,"5":0,"6":0,"8":0,"9":0,"10":0}
	def __init__(self,name,cash):
		self.name = str(name)
		self.cash = float(cash)
		
	def __repr__(self):
		return '%s has $%.2f' % (self.name, self.cash)
	
	def rollDice(self):
		dice = randint(1,6) + randint(1,6)
		return dice

class CrapsTable(object):
	payout = {"ComeLine":2,"PassLine":2,"4":2.8,"5":2.4,"6":2.16,"8":2.16,"9":2.4,"10":2.8}
	def __init__(self,players):
		self.players = players
		self.roller = self.players[0]
	
	
		
		
#************TESTS*************#
testGambler = Gambler('Frederick',2000)
print(testGambler)
print(testGambler.rollDice())
