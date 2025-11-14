import player_Info
import invalid_Input
print ("Weclome to Lathian")
player_Name = input("What's your name?\n")
print ("Ok, ", player_Name, ".")
while True:
	yn_temp = input ("Can I ask you a few questions?")
	yn_temp = yn_temp.lower()
	if yn_temp == "yes":
		pronouns = player_Info.get_pronouns()
		break
	elif yn_temp == "no":
		while True:
			yn_temp = input ("You wish to skip charcheter custamization \nConfirm y/n") 
			yn_temp = yn_temp[0].lower()
			if yn_temp == "no":
				pronouns = player_Info.get_pronouns()
				break
			elif yn_temp == "yes":
				break
			else :
				invalid_Input
	else :
		invalid_Input