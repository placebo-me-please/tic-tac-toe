#========================================================================================================
#initialization
#========================================================================================================
#import functions
from random import randint		#built-in random integer generator for player selection
import time						#built-in time module for message delays

#clear the command line
import os
os.system('clear')
#========================================================================================================
#functions
#========================================================================================================
def tutorial():
	
	if player_choice('Do you need a tutorial? (Y/N): ') == True:
		print('This game is best played using a numpad')
		time.sleep(2)
		print('Each player inputs a number using this schema:')
		print_board(grid_demo)
		time.sleep(2)
		print('Players should announce if they are Player 1 or 2')
		time.sleep(2)

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

def player_selector():
	#this randomly produces a number in the range [1,20]
	dice_roll = randint(1, 20)
	
	#this checks if the roll is high or low
	if dice_roll < 11:
		return 1
	elif dice_roll > 10:
		return 2 

def player_choice(message):
	player_ready = False
	#this control flow waits for the players to 'ready-up'
	while player_ready == False:
		ready_status = input(message).upper()
		if ready_status == 'Y':
			return True
		elif ready_status == 'N':
			#cannot return False because the loop breaks
			return False
		else:
			player_status = False
			print('Read the prompt you Donkey')

def player_input(grid_selection):
	#selection status is assumed to be false unless the validation function passes the user selection
	selection_status = False
	while selection_status == False:
		#this loop executes until the selection is recognized as valid
		player_selection = input("Enter your selection (numeric value in the range [1,9]): ")
		selection_status = validate_selection(player_selection)
		
		#if the input is valid then the code needs to verify that the grid space is not already occupied
		if selection_status == True:
			player_selection = int(player_selection)
			selection_status = validate_gridspace(player_selection, grid_selection)
		elif selection_status == False:
			pass

		#if the input is valid then this function returns the input an integer
		if selection_status == True:
			return player_selection
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
	win_count_X = 0
	win_count_O = 0

	#this checks if any of the symbols match the win condition pattern
	#an asterisk represents an arbitary symbol so that pattern matching is simpler
	for key in win_cons:
		
		#zips the current board together with a win condition for comparison
		comparison_list = list(zip(win_cons[key], grid_selection))

		#for every pair that is valid the win count is increased by 1
		for symbol_pair in comparison_list:
			if symbol_pair[0] == '*' and symbol_pair[1] == 'X':
				win_count_X += 1
			elif symbol_pair[0] == '*' and symbol_pair[1] == 'O':
				win_count_O += 1

		#any player with a count of 3 wins the game
		if win_count_X == 3:
			return 1
		elif win_count_O == 3:
			return 2
		elif win_count_X != 3 and win_count_O != 3:
			win_count_X = win_count_O = 0 

	#this returns false if neither player won
	if win_count_X == 0 and win_count_O == 0:
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

def validate_gridspace(player_selection, grid_selection):
	#validation status is assumed to be False unless proven to be True
	validation_status = False

	#checks if the player's selection is occupied by another symbol
	if grid_selection[player_selection - 1] == ' ':
		validation_status = True
		return True
	elif grid_selection[player_selection - 1] == 'X' or grid_selection[player_selection - 1] == 'O':
		print('That space is taken you Donkey')
		validation_status = False
		return False

#========================================================================================================
#game loop
#========================================================================================================
#initialize grid and player variables
grid_demo = ['1','2','3','4','5','6','7','8','9']
grid_selection = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
player_symbol = ['X','O']

#the loop calls in functions as-needed until the game is over.
print('Welcome to Tic-Tac-Toe!')
time.sleep(2)
tutorial()

#the game status is intialized as False
game_over = False
player_1 = 1
player_2 = 0

player_choice('Have you decided who is Player 1 and who is Player 2? (Y): ')

active_player= player_selector()
print(f'Player {active_player} goes first and will use "{player_symbol[active_player - 1]}"')

while game_over == False:
	
	player_selection = player_input(grid_selection)

	if active_player - 1 == 0:
		grid_selection[player_selection - 1] = player_symbol[0]
		active_player += 1
	elif active_player - 1 == 1:
		grid_selection[player_selection - 1] = player_symbol[1]
		active_player -= 1
	
	print_board(grid_selection)

	if check_win(grid_selection) == False and check_full(grid_selection) == False:
		game_over = False
	elif check_win(grid_selection) != False:
		game_over = True
		print(f'Player {check_win(grid_selection)} won the game')
	elif check_full(grid_selection) == True:
		print('The board is full and the game is over')
		game_over = True

print('Thanks for playing!')
#========================================================================================================
#testing
#========================================================================================================
# #this test should roll a virtual d20 then choose a player
# print(f'Player {player_selector()} will go first')

# # this test should exercise the code's ability to assess whether or not a player's selection conflicts with the current board
# player_selection = 0
# grid_selection = ['X']
# validate_gridspace(player_selection, grid_selection)
# grid_selection = ['O']
# validate_gridspace(player_selection, grid_selection)
# grid_selection = [' ']
# validate_gridspace(player_selection, grid_selection)

# #this test should exercise the code's ability to assess whether or not a player's symbols match any win-condition patterns
# grid_selection = ['X','X','X',' ',' ',' ',' ',' ',' ']
# print(f'Player {check_win(grid_selection)} won the game')
# grid_selection = ['O',' ',' ',' ','O',' ','O',' ','O']
# print(f'Player {check_win(grid_selection)} won the game')
# grid_selection = ['O',' ','X',' ','O','X','O',' ','O']
# print(f'Player {check_win(grid_selection)} won the game')
# grid_selection = ['O',' ',' ',' ',' ',' ','O',' ','O']
# print(f'Player {check_win(grid_selection)} won the game')

# #this test should exercise the ability of the code to assess whether or not the board is fully populated
# # expected output here is False
# grid_selection = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
# print(check_full(grid_selection))
# #expected outputs here are True
# grid_selection = ['X','X','X','X','O','X','X','X','X']
# print(check_full(grid_selection))
# grid_selection = ['X','X','X','X','X','X','X','X','X']
# print(check_full(grid_selection))

# #this should validate if the value is numeric and within range, and return an appropriate error if one or both conditions are untrue
# player_selection = ['0','5','10', 'A']
# validate_selection(player_selection[0])
# validate_selection(player_selection[1])
# validate_selection(player_selection[2])
# validate_selection(player_selection[3])

# #this should produce a 3x3 tic-tac-toe grid with only an 'X' in the lower-left corner
# grid_selection = ['X',' ',' ',' ',' ',' ',' ',' ',' ']
# print_board(grid_selection)

# #this should produce an empty 3x3 tic-tac-toe grid
# grid_selection = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
# print_board(grid_selection)