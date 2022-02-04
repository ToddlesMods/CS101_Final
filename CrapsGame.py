#!/usr/bin/env python3
#Creation of a Craps gambling game#
from random import randint
import time

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
	def placeBet(self,InBet,amount):
		bet = InBet.upper()
		if self.cash < amount:
			print("You don't have enough cash for that bet, you have $%.2f" %(self.cash))
			return
		else:
			self.cash -= amount
			self.bets[bet] += amount
			return
	#Method to allow player to remove bet. If the requested amount to close is greater than the bet, bet is closed out for however much
	#was placed.
	def removeBet(self,InBet,amount):
		bet = InBet.upper()
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

	def __init__(self,players):
		self.players = players
		self.player_count = len(self.players)
		self.roller = self.players[0]
		self.roll_count = 0
		self.payout = {"COME LINE":2,"PASS LINE":2,"4":1.8,"5":1.4,"6":1.16,"8":1.16,"9":1.4,"10":1.8}
		self.bet_names = ["COME LINE","PASS LINE","4","5","6","8","9","10"]
		self.last_roll = 0
		self.come_line_win = 0
	
	#Requests roll from player, forces player to roll really, no way to leave until you roll
	def requestRoll(self):
		answer = input(self.roller.name + ", are you ready to roll?! Yes or No: ")
		if answer.upper() in ["YES","Y"]:
			self.last_roll = self.roller.rollDice()
			print("ROLLING!!!")
			time.sleep(3)
			print("You rolled a " + str(self.last_roll))
			self.roll_count += 1
			return
		elif answer.upper() in ["NO","N"]:
			print("Come on! We have a game to play!")
			self.requestRoll()
			return
		else:
			self.requestRoll()
			return
	
	def placeBets(self):
		#allow players to place bets
		for player in self.players:
			print("Hello, %s. You currently have $%.2f. Here are your current bets:" %(player.name,player.cash))
			for bet in player.bets:
				print("%s: $%.2f" %(bet,player.bets[bet]))
			desire = input("Would you like to place a bet? Yes or No?: ")
			while True:
				if desire.upper() not in ["YES","Y"]:
					print("Ok...NEXT!\n")
					break
				else:
					newBet = input("What bet would you like to place? (Use the names from the list): ").upper()
					if newBet not in self.bet_names:
						print("Er...that's not a bet")
					else:
						while True:	
							newAmountTxt = input("How much would you like to bet?: ")
							if newAmountTxt.isnumeric():
								newAmount = float(newAmountTxt)
								player.placeBet(newBet,newAmount)
								break
					print("Bet added on %s for $%s" %(newBet,newAmountTxt))
					newBet = ""
					newAmountTxt = ""
					newAmount = 0.0
					time.sleep(1)
					desire = input("Would you like place another bet? Yes or No?: ")
				time.sleep(2)
		return
	
	def resolveBets(self,type):
		#resolve bets here
		if type == "First Roll Win":
			#payout if you need to payout
			for player in self.players:
				player.cash += (player.bets["COME LINE"] * self.payout["COME LINE"])
				player.bets["COME LINE"] = 0
				player.bets["PASS LINE"] = 0
		elif type == "First Roll Loss":
			#payout if you need to payout
			for player in self.players:
				player.cash += (player.bets["PASS LINE"] * self.payout["PASS LINE"])
				player.bets["COME LINE"] = 0
				player.bets["PASS LINE"] = 0
		else:
			roll = str(self.last_roll).upper()
			if roll in self.payout.keys():
				for player in self.players:
					player.cash += (player.bets[roll] * self.payout[roll])
		return
	
	def removePlayer(self,player_name):
		print("So long, %s" %(player_name))
		if self.players[self.roller] is self.players[player_name]:
			self.roller = self.players[(self.players.index(self.roller)+1)%self.player_count]
		self.players.pop(player_name,None)
		return
	
	def addPlayer(self,player_name,cash):
		print("Welcome, %s!" %(player_name))
		if not cash.isnumeric():
			while True:
				print("That's not an amount of cash!")
				cash = input("Give us a real amount: ")
				if cash.isnumeric():
					break
		gamblerNew = Gambler(player_name, int(cash))
		self.players.append()
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
				self.come_line_win = dice
				self.resolveBets("Standard")
			return
		else:
			if dice == 7:
				print ("Sorry! There's always next time. New roller!")
				self.roll_count = 0
				self.roller = self.players[(self.players.index(self.roller)+1)%self.player_count]
				for player in self.players:
					for bet in player.bets:
						bet = 0
			else:
				print("Let's keep it going! Payouts!")
				if dice == self.come_line_win:
					print("Big win! Let's start again")
					self.resolveBets("Standard")
					self.resolveBets("First Roll Win")
					self.roll_count = 0
			self.resolveBets("Standard")
			return
		
#Game Class to get the game rolling
class Game(object):
	player_list = []
	player_count = 0
	
	def __init__(self):
		self.gather_players()
		self.start_game()
		
	def gather_players(self):
		print("Welcome to the Casino! Let's play craps!!!")
		firstPlayer = input("Let's get started!\nWho is our first player?: ")
		firstAmounttxt = input("How much money are you starting with?: ")
		while True:
			if firstAmounttxt.isnumeric():
				break
			firstAmounttxt = input("That's doesn't work!\nHow much money are you starting with?: ")
		self.player_list.append(Gambler(firstPlayer,float(firstAmounttxt)))
		self.player_count += 1
		keepRolling = input("Any more players? Yes or No: ")
		while True:
			if keepRolling.upper() not in ["YES","Y"]:
				break
			else:
				playerName = input("Name: ")
				playerCash = input("Starting Money: ")
				while True:
					if playerCash.isnumeric():
						break
					playerCash = input("That's not right! Starting Money: ")
				self.player_list.append(Gambler(playerName,float(playerCash)))
				self.player_count += 1
			keepRolling = input("Any more players? Yes or No: ")
	
	def start_game(self):
		print("Here we go!")
		table = CrapsTable(self.player_list)
		while True:
			table.placeBets()
			table.requestRoll()
			table.resolveRoll()
			addPlayers = input("Any new players? Yes or No: ")
			if addPlayers.upper() in ["YES","Y"]:
				pName = input("Who is the new player?: ")
				pCash = input("How much cash are they starting with?: ")
				table.addPlayer(pName,pCash)
				self.player_count += 1
			removePlayers = input ("Any players leaving? Yes or No: ")
			if removePlayers.upper() in ["YES","Y"]:
				pName = input("Who is leaving?: ")
				table.removePlayer(pName)
				self.player_count -= 1
				if self.player_count <= 0:
					print("No more players. Good bye!")
					return
			keepGoing = input("How are we feeling now? Keep going? Yes or No: ").upper()
			if keepGoing in ["NO","N"]:
				print("So long! The Casino is closed!")
				break
			else:
				print("Let's keep going!!!")
			
		

		
	

		
		
#*************GAME START*********************************
crapsGame = Game()
