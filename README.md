# Status:
As it stands, play2win.py is incomplete, but the other components are complete for now and work as standalone files.

# play2lose
A program that plays Tic Tac Toe with you. You just won't be able to win.

Included are the main file "play2lose.py" and supplementary files "TicTacToe.py" and "GameBoard.py". 

"GameBoard.py" was created alongside the main function of play2lose, providing the board that will contain the game board. 

Originally, the board was going to strictly be a 3x3 board but I decided to expand the concept of the idea and have the size of the board be user defined. Also, the original idea was to have
this class only work for Tic Tac Toe boards, but I decided to make it abstract and to work for all sorts of games, and instead put have restrictions for the type of game in the programs that inherit from "GameBoard.py".
All in all, GameBoard.py can be used as the foundation of any type of game that uses a tile-based board. It order to achieve this, GameBoard.py is an abstract base class and has abstract methods in which its children classes must make changes in order to use those methods.

"TicTacToe.py" contains the framework of a Tic Tac Toe game, building off of the foundation of "GameBoard.py". In this file, the specifics of the game and rules are set.

"play2lose.py" contains the bulk of the project. It contains "unbeatable AI" that will not lose to the player, no matter the skill level of the player. This required the most thought to be made, using algorithms based on determining the best possible next moves for the computer and playing them in order to progress.

This project is free-to-use, you can redistribute, add on to, and use it however way you wish. All I require is proper citation and credit to the source of your projects. Also, feel free to send me a message to projects that pull from this repo, I'm excited to see what sort of things that my little side project can be a part of!
