#!/usr/bin/env python3
#Creation of a Craps gambling game#
from random import randint

#CLASSES:
#Gambler class for players
class Gambler(object):
	def __init__(self,name,cash):
		self.name = str(name)
		self.cash = float(cash)
		self.bets = {"COME LINE":0.00,"PASS LINE":0.00,"4":0.00,"5":0.00,"6":0.00,"8":0.00,"9":0.00,"10":0.00}
	
	#When Gambler requested, output: PLAYER has $CASH
	def __repr__(self):
		return '%s has $%.2f' % (self.name, self.cash)
	
	#Method to get simulate dice roll and provide the sum of the two dice
	def rollDice(self):
		dice = randint(1,6) + randint(1,6)
		return dice
	
	#Method to allow player to place a bet, if they try to place a bet for more than they have, returns a statement letting them know
	#and letting them know how much cash they have. Does not place any bet if attempted bet higher than cash.
	def placeBet(self,bet,amount):
		if self.cash < amount:
			print("You don't have enough cash for that bet, you have $%.2f" %(self.cash))
			return
		else:
			self.cash -= amount
			self.bets[bet] += amount
			return
	#Method to allow player to remove bet. If the requested amount to close is greater than the bet, bet is closed out for however much
	#was placed.
	def removeBet(self,bet,amount):
		if amount > self.bets[bet]:
			print("You didn't bet that much. Closing out your bet worth $%.2f" %(self.bets[bet]))
			self.cash += self.bets[bet]
			self.bets[bet] = 0.00
			return
		else:
			self.cash += amount
			self.bets[bet] -= amount
			return
		
#Table class for play
class CrapsTable(object):
	payout = {"COME LINE":2,"PASS LINE":2,"4":2.8,"5":2.4,"6":2.16,"8":2.16,"9":2.4,"10":2.8}
	bet_names = ["COME LINE","PASS LINE","4","5","6","8","9","10"]
	last_roll = 0
	def __init__(self,players):
		self.players = players
		self.player_count = len(self.players)
		self.roller = self.players[0]
		self.roll_count = 0
	
	def requestRoll(self):
		answer = input(self.roller.name + ", are you ready to roll?! Yes or No: ")
		if answer.upper() == "YES":
			self.last_roll = self.roller.rollDice()
			print("You rolled " + str(self.last_roll))
			self.roll_count += 1
			return
		elif answer.upper() == "NO":
			print("Come on! We have a game to play!")
			self.requestRoll()
			return
		else:
			self.requestRoll()
			return
	
	def placeBets(self):
		#allow players to place bets
		
		return
	
	def resolveBets(self,type):
		#resolve bets here
		if type == "First Roll Win":
			#payout if you need to payout
			for player in self.players:
				player.cash += player.bets["COME LINE"] * self.payout["COME LINE"]
				player.bets["COME LINE"] = 0
				player.bets["PASS LINE"] = 0
		elif type == "First Roll Loss":
			#payout if you need to payout
			for player in self.players:
				player.cash += player.bets["PASS LINE"] * self.payout["PASS LINE"]
				player.bets["COME LINE"] = 0
				player.bets["PASS LINE"] = 0
		else:
			roll = str(self.last_roll).upper()
			if roll in self.payout.keys():
				for player in self.players:
					player.cash += player.bets[roll] * self.payout[roll]
		return
	
	def removePlayer(self,player_name):
		#remove player
		return
	
	def addPlayer(self,player_name,cash):
		#add player
		return
		
	def resolveRoll(self):
		dice = self.last_roll
		count = self.roll_count
		if count < 2:
			#This is the first roll and is handled uniquely
			if dice == 7 or dice == 11:
				print("WINNER!")
				self.resolveBets("First Roll Win")
			elif dice == 2 or dice == 12:
				print("Sorry, craps!")
				self.resolveBets("First Roll Loss")
			else:
				print("Here we go! Waiting for a " + str(dice) + "!")
			return
		else:
			if dice == 7:
				print ("Sorry! There's always next time. New roller!")
				self.roll_count = 0
				self.roller = self.players[(self.players.index(self.roller)+1)%self.player_count]
				for player in self.players:
					for bet in player.bets.values():
						bet = 0
			else:
				print("Let's keep it going! Payouts!")
			self.resolveBets("Standard")
			return

		
		
#************TESTS*************#
testGambler = Gambler('Mariana',2000)
testGambler1 = Gambler('Henton',1000)
testGambler2 = Gambler('Sawyer',100000)
testTable = CrapsTable([testGambler,testGambler1,testGambler2])
#print(testGambler)
#print(testGambler.rollDice())
#print(testGambler.bets["Come Line"])
#testGambler.placeBet("Come Line", 100)
#print(testGambler.bets["Come Line"])
#testGambler.removeBet("Come Line", 240)
#print(testGambler.bets["Come Line"])
#print(testGambler)
testTable.requestRoll()
testTable.placeBets()
print(testGambler.bets)
print(testGambler1.bets)
print(testGambler2.bets)
print(testGambler)
print(testGambler1)
print(testGambler2)
