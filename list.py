#Shopping list app
shopping_list = []

# Help Function to show the user commands for the script.
def help_user():
	print("The list of features are:")
	print("Type \"ADD\" to add to your shopping list")
	print("Type \"HELP\" for bringing up the help menu/options")
	print("Type \"LIST\" to see the current list")
	print("Type \"DONE\" to quit the list.")

# a list function to list out the items in the list.
def show_user_their_list():
	if len(shopping_list) >= 1:
		print("-" * 20)
		print("Your list contains:\n")
		for item in shopping_list:
			print("- " + item)
		print("-" * 20)
	else:
		print("Your list is empty!")


#First thing's first, print the help
help_user()

# main script, while loop.
while True:
	askUser = input("> ").upper()

	if askUser == "ADD":
		print("Add as many items as you like and type \"FINISHED\" when you're done adding!")
		while True:
			userItem = input("> ").upper()
			if userItem == "FINISHED":

				break
			elif userItem == "DONE":
				print("You should type \"FINISHED\" if you want to stop adding items to your list")
			else:
				shopping_list.append(userItem)
				print(userItem.title() + " has been added to the list.")
	elif askUser == "HELP":
		help_user()
	elif askUser == "LIST":
		show_user_their_list()
	elif askUser == "DONE":
		break

#Print the list:
show_user_their_list()