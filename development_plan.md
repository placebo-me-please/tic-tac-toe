*“There's a point, around the age of twenty, when you have to choose whether to be like everybody else the rest of your life, or to make a virtue of your peculiarities.”* 

Ursula K. Le Guin, *The Dispossessed*

## Summary ##

The goal of this project is to develop a simple, two-user game of Tic-Tac-Toe. The game must have an interactive input field and a graphical display of the game that is updated to reflect the current state of the game.

Because the reason I chose to learn software is to explore new career options, I decided I should approach this project with good development practices in mind. However, the limited complexity of the project does not warrant more than a single page.

## User Story ##

This game will be played by two human users. One player will be randomly selected to select a symbol and go first. They will take turns selecting their Tic-Tac-Toe spaces via an input field. The graphics display will update the board after each turn. After the game is complete, the computer will verify if any player won the game. Finally, the computer will announce its decision.

## Requirements ##

 * The game shall be written using Python
 * The game shall be playable from the terminal window
 * The terminal window shall display a Tic-Tac-Toe grid comprised of ASCII characters
 * The terminal window shall update the state of the game after each user takes their turn
 * The terminal window shall only accept numeric inputs in the range [1, 9] and reject invalid inputs of any other kind
 * The program shall assess the board at the conclusion of a game and correctly declare a winner (if there is one)

## Development Management Plan ##

The code will be written using the Sublime IDE and version controlled using GitHub. Test Driven Development (see *The Art of Agile Development*) will be implemented. Methods for managing bugs will be developed ad hoc. The artifacts of this project will be kept in this repo. Finally, a summary will be written at project closure to document my experience and report any interesting findings.
