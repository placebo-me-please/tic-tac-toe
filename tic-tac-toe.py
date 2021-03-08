#import os
#os.system('clear')

def print_board(grid_selection):
	print(f'\
		   |   |   \n\
		 {grid_selection[6]} | {grid_selection[7]} | {grid_selection[8]} \n\
		___|___|___\n\
		   |   |   \n\
		 {grid_selection[3]} | {grid_selection[4]} | {grid_selection[5]} \n\
		___|___|___\n\
		   |   |   \n\
		 {grid_selection[0]} | {grid_selection[1]} | {grid_selection[2]} \n\
		   |   |   \n')

def place_symbol(grid_selection):
	player_selection = player_input()
	grid_selection[player_selection - 1] = "X"
	print_board(grid_selection)

def player_input():
	#selection status is assumed to be false unless the validation function passes the user selection
	selection_status = False
	while selection_status == False:
		#this loop executes until the selection is recognized as valid
		player_selection = input("Enter your selection (numeric value in the range [1,9]): ")
		selection_status = validate_selection(player_selection)

		#if the input is valid then this function returns the input an integer
		if selection_status == True:
			return int(player_selection)
		#otherwise it ignores the input an the while loop starts again	
		elif selection_status == False:
			pass

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
		return False

	#checks if the value is within range (only if it is numeric)
	if validation_status[0] == True and player_selection > 0  and player_selection < 10:
		validation_status[1] = True
	elif player_selection >= 0 or player_selection >= 10:
		print('Error: input was out of range you Donkey')
		validation_status[1] = False
		return False

	#final validation check
	if all(validation_status) == True:
		return True

#TESTING
#this test should exercise the ability of the code to assess whether or not the board is fully populated
#expected output here is False
grid_selection = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
check_empty(grid_selection)
#expected output here is True
grid_selection = ['X','X','X','X','X','X','X','X','X']
check_empty(grid_selection)


#this should populate an "X" in whatever space the user selected on the grid
# grid_selection = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
# place_symbol(grid_selection)

# this should prompt the user for an input and validate it before deciding to place it on the grid
# player_input()

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
#grid_selection = ['X',' ',' ',' ',' ',' ',' ',' ',' ']
#print_board(grid_selection)

#this should produce an empty 3x3 tic-tac-toe grid
#grid_selection = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#print_board(grid_selection)