import player_Info
import invalid_Input
print ("\033[4;36m hello world \033[0m")
print ("Weclome to Lathian")
player_Name = input("What's your name?\n")
print ("Ok, ", player_Name, ".")
while True:
	yn_temp = input ("Do you mind if I ask you a few questions?")
	yn_temp = yn_temp[0].lower()
	if yn_temp == "y":
		pronouns = player_Info.get_pronouns()
		break
	elif yn_temp == "n":
		while True:
			yn_temp = input ("You wish to skip charcheter custamization \nConfirm y/n") 
			yn_temp = yn_temp[0].lower()
			if yn_temp == "n":
				pronouns = player_Info.get_pronouns()
				break
			elif yn_temp == "y":
				break
			else :
				invalid_Input
	else :
		invalid_Input