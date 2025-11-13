
def bio()
	while pronouns_Selected:
		player_Pronouns = input ("What would you like to be refered to by?\n1. Masculin pronouns(he/him)\n2. feminine pronouns(she/her)\n3. nuetral pronouns(they/them)\n4. other")
		if player_Pronouns == 1:
			player_Pronoun_Subjective = "he"
			player_Pronoun_Objective = "him"
			player_Pronoun_Possessive = "his"
			player_Pronoun_Reflexive = "himself"
			pronouns_Selected = True
		elif player_Pronouns == 2:
			player_Pronoun_Subjective = "she"
			player_Pronoun_Objective = "her"
			player_Pronoun_Possessive = "hers"
			player_Pronoun_Reflexive = "herself"
			pronouns_Selected = True
		elif player_Pronouns == 3:
			player_Pronoun_Subjective = "they"
			player_Pronoun_Objective = "them"
			player_Pronoun_Possessive = "theirs"
			player_Pronoun_Reflexive = "themself"
			pronouns_Selected = True
		elif player_Pronouns == 4:
			player_Pronouns = input ( "1. Ze/Hir\n2. Xe/Xem\n3. Ver/Vir\n4. Te/Tem\n5. Ey/Em\n")
			if player_Pronouns == 1:
				player_Pronoun_Subjective = "Ze"
				player_Pronoun_Objective = "Hir"
				player_Pronoun_Possessive = "Hirs"
				player_Pronoun_Reflexive = "Hirself"
				proboun_Selected = True

		else :
			print ("Please input the number of your selection")
	bio = (player_Pronoun_Subjective, player_Pronoun_objective, player_Pronoun_Possessive, player_Pronoun_Reflexive,)
print ("Weclome to Lathian")
player_Name = input("What's your name?")
print ("Ok, ", player_Name, ".")
y/n_temp = print ("Do you mind if i ask you a few questions?\nY/N")
if y/n_temp == y:
	bio()
