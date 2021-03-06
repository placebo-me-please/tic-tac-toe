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

grid_selection = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]
print_board(grid_selection)

