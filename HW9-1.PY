from random import randrange

print("Hi enter an integer : ")

try:
	play= "yes"
	while (play == "yes"):
		x = randrange(15)
		y = randrange(15)
		ans = x // y 
		print ( str(x)+"/" + str(y))
		guess = input ("")
		if ans == int(guess):
			print ("\n correct!")
			
		else:
			print("\n correct!")
		play = input("Do you want to claculate again?: ")
	else:
		print("Good bye!")
		

except ValueError:
    print(" Please enter an integer!")
    

except ZeroDivisionError:
    print("You cannot devide by zero")
