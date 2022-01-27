#!/usr/bin/env python3
#Creation of a Craps gambling game#
from random import randint

#CLASSES:
#Gambler class for players
class Gambler(object):
	def __init__(self,name,cash):
		self.name = str(name)
		self.cash = float(cash)
		self.bets = {"COME LINE":0,"PASS LINE":0,"4":0,"5":0,"6":0,"8":0,"9":0,"10":0}
		
	def __repr__(self):
		return '%s has $%.2f' % (self.name, self.cash)
	
	def rollDice(self):
		dice = randint(1,6) + randint(1,6)
		return dice
	
	def placeBet(self,bet,amount):
		if self.cash < amount:
			print("You don't have enough cash for that bet")
			return
		else:
			self.cash -= amount
			self.bets[bet] += amount
			return
		
	def removeBet(self,bet,amount):
		if amount > self.bets[bet]:
			print("You didn't bet that much. You have $" + str(self.bets[bet]) + " on the " + bet)
			return
		else:
			self.cash += amount
			self.bets[bet] -= amount
			return
		
#Table class for play
class CrapsTable(object):
	payout = {"Come Line":2,"Pass Line":2,"4":2.8,"5":2.4,"6":2.16,"8":2.16,"9":2.4,"10":2.8}
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
		for player in self.players:
			print("Hello, " + player.name + "! Here are your current bets:")
			for bet in player.bets:
				print(bet + ": $" + str(player.bets[bet]))
			desire = input("Would you like to place a bet? Yes or No: ")
			if desire.upper() == "NO":
				continue
			elif desire.upper() == "YES":
				while True:
					bet_name = str(input("Which bet? Please use a name used in your current bets above: ")).upper()
					bet_amounta = input("How much?: ")
					if bet_amounta.isnumeric():
						bet_amount = float(bet_amounta)
						if bet_name in self.bet_names:
							player.placeBet(bet_name,bet_amount)
						else:
							print("That's not one of the bets!")
					else:
						print("That doesn't work!")
					keep_going = input("Would you like to place another bet? Yes or No: ")
					if keep_going.upper() == "YES":
						print("OK!")
					elif keep_going.upper() == "NO":
						print("ok\n")
						break
					else:
						print("We don't have time for this. Next player!\n")
						break
			else:
				print("I didn't get that...your bets stand! moving on!\n")				
		return
	
	def resolveBets(self,type):
		#resolve bets here
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
				self.resolveBets("First Roll")
			elif dice == 2 or dice == 12:
				print("Sorry, craps!")
				self.resolveBets("First Roll")
			else:
				print("Here we go! Waiting for a " + str(dice) + "!")
			return
		else:
			if dice == 7:
				print ("Sorry! There's always next time. New roller!")
				self.roll_count = 0
				self.roller = self.players[(self.players.index(self.roller)+1)%self.player_count]
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

