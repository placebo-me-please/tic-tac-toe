#import os
#os.system('clear')

def print_board(grid_selection):
	print(f'\
		   |   |   \n\
		 {grid_selection[0]} | {grid_selection[1]} | {grid_selection[2]} \n\
		___|___|___\n\
		   |   |   \n\
		 {grid_selection[3]} | {grid_selection[4]} | {grid_selection[5]} \n\
		___|___|___\n\
		   |   |   \n\
		 {grid_selection[6]} | {grid_selection[7]} | {grid_selection[8]} \n\
		   |   |   \n')

def player_input():
	player_selection = input("Enter your selection (numeric value in the range [1,9]): ")
	validate_selection(player_selection)

def validate_selection(player_selection):
	#validation statuses are assumed to be False unless proven to be true
	validation_status = [False, False]

	#checks if the value is numeric
	if player_selection.isdigit() == True:
		player_selection = int(player_selection)
		validation_status[0] = True
	elif player_selection.isdigit() == False:
		print('Error: input was not numeric you Donkey')
		validation_status[0] = False
		return

	#checks if the value is within range (only if it is numeric)
	if validation_status[0] == True and player_selection > 0  and player_selection < 10:
		validation_status[1] = True
	elif player_selection >= 0 or player_selection >= 10:
		print('Error: input was out of range you Donkey')
		validation_status[1] = False
		return

	#final validation check
	if all(validation_status) == True:
		return player_selection

#TESTING
#this should prompt the user for an input and validate it before deciding to place it on the grid
player_input()

#this should validate if the value is numeric and within range, and return an appropriate error if one or both conditions are untrue
# player_selection = ['0','5','10', 'A']
# validate_selection(player_selection[0])
# validate_selection(player_selection[1])
# validate_selection(player_selection[2])
# validate_selection(player_selection[3])

#this should validate if the input value is numeric AND is within the valid [1,9] range, and return an error if it is not
# player_selection = ['0','5','10']
# validate_selection_range(player_selection[0])
# validate_selection_range(player_selection[1])
# validate_selection_range(player_selection[2])
# def validate_selection_range(player_selection):
# 	player_selection = int(player_selection)
# 	if player_selection > 0  and player_selection < 10:
# 		print('valid entry')
# 	elif player_selection >= 0 or player_selection >= 10:
# 		print('Error: input was out of range you Donkey') 

#this should validate if the input value is numeric and convert it to an int if it is, and return an error if it is not
# player_selection = ['A', '10']
# validate_selection_int(player_selection[0])
# validate_selection_int(player_selection[1])
# def validate_selection_int(player_selection):
# 	if player_selection.isdigit() == True:
# 		player_selection = int(player_selection)
# 	elif player_selection.isdigit() == False:
# 		print('Error: input was not numeric you Donkey')

#this should prompt a player to make an input that is stored as a string
# player_input()

#this should produce a 3x3 tic-tac-toe grid with only an 'X' in the upper-left corner
#grid_selection = ['X',' ',' ',' ',' ',' ',' ',' ',' ',]
#print_board(grid_selection)

#this should produce an empty 3x3 tic-tac-toe grid
#grid_selection = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]
#print_board(grid_selection)