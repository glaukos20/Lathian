import invalid_Input
valid_Commands = ["left", "right", "up", "down", "nort", "east", "south", "west", "straight", "forward", "back", "leave", "go", "crawl", "stay", "run", "hide", "turn", "climb", "jump", "breath", "kill", "do", "make", "beg", "say", "ask", "speak", "talk", "take", "give", "pick up", "drop", "put down", "use", "give", "throw", "hold", "open", "close", "grab", "help", "quit", "exit", "save", "load", "look", "watch", "inspect", "read", "serch", "inventory", "examine"]
def verify(Input):
 	Input = Input.lower()
	if Input in vald_Commands:
        	return Input
