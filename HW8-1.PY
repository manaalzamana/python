class Animal:
	def __init__(self, name):
	        self.name = name
	def guess_who_am_i(self):
		print("I will give you 3 hints, guess what animal I am\n")
		if self.name == "elephant":
			self.elephant()
		elif self.name == "tiger":
			self.tiger()
		elif self.name == "bat":
			self.bat()

	def resultguess_hint(self, hint):
		print (hint)
		guess=input("Who am I?:")
		if guess.strip(',.').lower() == self.name:
			print ("You got it! I am  ",self.name, "\n\n")
			return 1
		else:
			print("Nope, try again!")
			return 0

	def guessme(self, hint1, hint2, hint3):
		status=self.resultguess_hint(hint1)
		if status == 1:
			return 0
		status=self.resultguess_hint(hint2)
		if status == 1:
			return 0
		status=self.resultguess_hint(hint3)
		if status == 1:
			return 0
		print ("I'm out of hints! The answer is: ", self.name, "\n\n")
		return 0

	def elephant(self):
		self.guessme("I have exceptional memory", "I am the largest land-living mammal in the world", "I have a very long Nose")
	def tiger(self):
		self.guessme("I am the biggest cat", "I come in black and white or orange and black", "I hunt goats")
	def bat(self):
		self.guessme("I use echo-location", "I can fly", "I see well in dark")
e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()
