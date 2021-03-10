#clear the command line
import os
os.system('clear')

#========================================================================================================
#initialization
#========================================================================================================
#import functions
from random import randint		#built-in random integer generator
import time

#initialize grid variables
grid_demo = ['1','2','3','4','5','6','7','8','9']
grid_selection = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

#========================================================================================================
#functions
#========================================================================================================
def print_board(grid_selection):
	print(f'\n \
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

def player_selector():
	#this randomly produces a number in the range [1,20]
	dice_roll = randint(1, 20)
	
	#this checks if the roll is high or low
	if dice_roll < 11:
		return 1
	elif dice_roll > 10:
		return 2 

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

def check_full(grid_selection):
	#this variable represents how many symbols have been placed
	symbol_count = 0
	
	#this control flow checks to see if every cell is occupied with a value
	for grid_space in grid_selection:
		if grid_space == "X" or grid_space == "O":
			symbol_count += 1
		elif grid_space == " ":
			return False

		if symbol_count == 9:
			return True

def check_win(grid_selection):
	#this is the dictionary of possible win conditions
	#future consideration is to re-write this as a tuple so that it is treated as immutable
	win_cons = {
	1 : ['*','*','*',' ',' ',' ',' ',' ',' '],
	2 : [' ',' ',' ','*','*','*',' ',' ',' '],
	3 : [' ',' ',' ',' ',' ',' ','*','*','*'],
	4 : ['*',' ',' ','*',' ',' ','*',' ',' '],
	5 : [' ','*',' ',' ','*',' ',' ','*',' '],
	6 : [' ',' ','*',' ',' ','*',' ',' ','*'],
	7 : ['*',' ',' ',' ','*',' ',' ',' ','*'],
	8 : [' ',' ','*',' ','*',' ','*',' ',' ']
	}

	#empty arrays that will individually represent a player
	#these will form patters that can be compared to the win_con dictionary
	grid_space_X = []
	grid_space_O = []
	grid_space_index = 0

	#this builds the arrays of patterns that will be checked against the win_con dictionary
	#an asterisk represents an arbitary symbol so that pattern matching is simpler
	for grid_space in grid_selection:
		if grid_space == 'X':
			grid_space_X.append('*')
		elif grid_space == 'O':
			grid_space_O.append('*')
		elif grid_space == ' ':
			grid_space_X.append(' ')
			grid_space_O.append(' ') 

		grid_space_index += 1

	#this control flow is responsible for checking the 'X' and 'Y' patterns against the win_con dictionary
	for key in win_cons:
		if win_cons[key] == grid_space_X:
			print('player X wins')
			return True
		elif win_cons[key] == grid_space_O:
			print('player O wins')
			return True
		else:
			return False

def validate_selection(player_selection):
	#validation statuses are assumed to be False unless proven to be True
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

#NEED TO ADD THIS VALIDATION TO THE PLAYER_INPUT() FUNCTION
def validate_gridspace(player_selection, grid_selection):
	#validation status is assumed to be False unless proven to be True
	validation_status = False

	# #checks if the player's selection is occupied by another symbol
	# if grid_selection[player_selection] == ' ':
	# 	validation_status = True
	# elif grid_selection[player_selection] == 'X' or grid_selection[player_selection] == 'O':
	# 	validation_status = False

#========================================================================================================
#game loop
#========================================================================================================
#this portion of code is the game loop. it calls in functions as-needed until the game is over.
print('Welcome to Tic-Tac-Toe!')
time.sleep(2)
print('This game is best played using a numpad')
time.sleep(2)
print('Each player inputs a number using this schema:')
print_board(grid_demo)
time.sleep(2)
print('Players should announce if they are Player 1 or 2')

#the ready and game statuses are intialized as False
player_ready = False
game_over = False

#this control flow waits for the players to 'ready-up'
while player_ready == False:
	ready_status = input('Have you decided? (Y/N) ')
	if ready_status == 'Y':
		player_ready = True
	elif ready_status == 'N':
		player_status = False
	else:
		player_status = False
		print('Read the prompt you Donkey')

first_player = player_selector()
print(f'Player {first_player} goes first and will use "X"')

# while game_over == False:
# 	if check_win(grid_selection) == False and check_full(grid_selection) == False:
# 		game_over == False
# 		selection = player_input()


#========================================================================================================
#testing
#========================================================================================================
#this test should roll a virtual d20 then choose a player
# player_selector()

# this test should exercise the code's ability to assess whether or not a player's selection conflicts with the current board
# player_selection = 0
# grid_selection = ['X']
# validate_gridspace(player_selection, grid_selection)
# grid_selection = ['O']
# validate_gridspace(player_selection, grid_selection)
# grid_selection = [' ']
# validate_gridspace(player_selection, grid_selection)

# #this test should exercise the code's ability to assess whether or not a player's symbols match any win-condition patterns
# grid_selection = ['X','X','X',' ',' ',' ',' ',' ',' ']
# check_win(grid_selection)
# grid_selection = ['O',' ',' ',' ','O',' ',' ',' ','O']
# check_win(grid_selection)

#this test should exercise the ability of the code to assess whether or not the board is fully populated
#expected output here is False
# grid_selection = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
# check_full(grid_selection)
# #expected outputs here are True
# grid_selection = ['X','X','X','X','O','X','X','X','X']
# check_full(grid_selection)
# grid_selection = ['X','X','X','X','X','X','X','X','X']
# check_full(grid_selection)

# this should populate an "X" in whatever space the user selected on the grid
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