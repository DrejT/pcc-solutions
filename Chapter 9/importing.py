from random import randint,choice

class Die:
	def __init__(self):
		self.sides = 6
	
	def roll_die(self):
		self.sides = randint(1,6)

my_dice = Die()
print(my_dice.sides)
my_dice.roll_die()
print(my_dice.sides)
print("\n")
#lottery
class Lottery:
	def __init__(self):
		self.lotto = [1,2,3,4,5,6,7,8,9,0,"a","b","c","d"]
		self.winning_lotto = []
		self.looplotto = []
		self.tries = 1
	
	def option(self):
		while len(self.winning_lotto) < 4:
			item = choice(self.lotto)
			if item not in self.winning_lotto:
				print(item)
				self.winning_lotto.append(item)
				
	def looptowin(self):
		while len(self.looplotto)<4:
			self.tries += 1
			loop = choice(self.lotto)
			for item in self.winning_lotto:
				if item not in self.winning_lotto:
					return False
			return True

my_ticket = Lottery()
print("THE WINNING LOTTO IS")
my_ticket.option()
print(my_ticket.winning_lotto)
my_ticket.looptowin()

ontinue
				if loop == self.winning_lotto[3]:
					print(loop)
					continue

my_ticket = Lottery()
print("THE WINNING LOTTO IS")
my_ticket.option()
print(my_ticket.winning_lotto)
my_ticket.looptowin()

