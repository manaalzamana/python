continueit=1
name = input ("Hi, what is your Name? ")
while continueit == 1:
    print ("Hello "+name+"! Let's play a game!")
    print ("Think of random number from 1 to 100, and I'll try to guess it!")
    tries=0
    isguessed=0
    upparlimit=100
    lowerlimit=1
    number=int((upparlimit+lowerlimit)/2)
    while(isguessed!=1):
        number=int((upparlimit+lowerlimit)/2)
        guess=input ("Is it "+str(number)+"? (yes/no)")
        tries=tries+1
        if guess == "no":
            order=input ("Is the number larger than "+str(number)+"? (yes/no)")
            if order == "yes":
                lowerlimit = number
            if order == "no":
                upparlimit = number
        elif guess== "yes":
            print ("Yeey! I got it in "+str(tries)+" tries!")
            isguessed=1
    more=input ("Do you want to play more?")
    if more=="yes":
        continueit=1
    else:
        continueit=0
