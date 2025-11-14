def get_pronouns():
	while True:
		player_Pronouns = input ("What would you like to be refered to by?\n1. Masculin pronouns(he/him)\n2. feminine pronouns(she/her)\n3. nuetral pronouns(they/them)\n4. other")
		if player_Pronouns == 1:
			player_Pronoun_Subjective = "he"
			player_Pronoun_Objective = "him"
			player_Pronoun_Possessive = "his"
			player_Pronoun_Reflexive = "himself"
			break
		elif player_Pronouns == 2:
			player_Pronoun_Subjective = "she"
			player_Pronoun_Objective = "her"
			player_Pronoun_Possessive = "hers"
			player_Pronoun_Reflexive = "herself"
			break
		elif player_Pronouns == 3:
			player_Pronoun_Subjective = "they"
			player_Pronoun_Objective = "them"
			player_Pronoun_Possessive = "theirs"
			player_Pronoun_Reflexive = "themself"
			break
		elif player_Pronouns == 4:
			while True:
				player_Pronouns = input ( "1. Ze/Hir\n2. Xe/Xem\n3. Ver/Vir\n4. Te/Tem\n5. Ey/Em\n6. custom\n")
				if player_Pronouns == 1:
					player_Pronoun_Subjective = "ze"
					player_Pronoun_Objective = "hir"
					player_Pronoun_Possessive = "hirs"
					player_Pronoun_Reflexive = "hirself"
					break
				elif player_Pronouns == 2:
					player_Pronoun_Subjective = "xe"
					player_Pronoun_Objective = "xem"
					player_Pronoun_Possessive = "xirs"
					player_Pronoun_Reflexive = "xemself"
					break
				elif player_Pronouns == 3:
					player_Pronoun_Subjective = "ver"
					player_Pronoun_Objective = "vir"
					player_Pronoun_Possessive = "vis"
					player_Pronoun_Reflexive = "verself"
					break
				elif player_Pronouns == 4:
					player_Pronoun_Subjective = "te"
					player_Pronoun_Objective = "tem"
					player_Pronoun_Possessive = "ter"
					player_Pronoun_Reflexive = "temself"
					break
				elif player_Pronouns == 5:
					player_Pronoun_Subjective = "ey"
					player_Pronoun_Objective = "em"
					player_Pronoun_Possessive = "eir"
					player_Pronoun_Reflexive = "emself"
					break
				elif player_Pronouns == 6:
					player_Pronoun_Subjective = input("Please input your prefered subjective pronoun (Ex. He, She, They)").lower()
					player_Pronoun_Objective = input("Please input your prefered objective pronoun (Ex. Him, Her, Them)").lower()
					player_Pronoun_Possessive = input("Please input your prefered possessive pronoun (Ex. His, Hers, Theirs)").lower()
					player_Pronoun_Reflexive = player_Pronoun_Objective + "self"
					break
				else :
		                        print ("Please input the number of your selection")
			break
		else :
			print ("Please input the number of your selection")
	pronouns = dict (subjective = player_Pronoun_Subjective, objective = player_Pronoun_objective, possessive = player_Pronoun_Possessive, reflexive = player_Pronoun_Reflexive,)
	return pronouns
