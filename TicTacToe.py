"""
# Copyright Johnson Zhong, 2018
# Distributed under the terms of the GNU General Public License.
# If any errors were found or you would like to contact me about anything, you
# can reach me via GitHub (https://github.com/Johnson-Zhong) or via my email
# Johnsonz8642@gmail.com
#
# This file was created alongside the main function of play2lose, providing the
# board that will contain the game board. Specifically, this program works on
# the groundwork that GameBoard.py made; focusing more on Tic Tac Toe games
# and the rules associated with it. Additionally, TicTacToe.py can be used to
# play a regular game of Tic Tac Toe with another person, rather than just
# being used for play2win.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""
from GameBoard import *


class TicTacToe(GameBoard):
    '''A class to represent objects that will replicate a Tic Tac Toe board.
    This class imports from the GameBoard class.'''
    def __init__(self):
        '''(TicTacToe) -> NoneType
        Creates a new TicTacToe object.
        '''
        # Create the TicTacToe object, a GameBoard object with dimensions 3x3.
        super().__init__(3, 3)

    def check_winner(self, row, col):
        '''(TicTacToe, int, int) -> bool
        Check if there is a winner of the Tic Tac Toe game. This method
        overwrites the check_winner() supermethod in GameBoard.
        '''
        # Create a variable that says if any of the win conditions were met.
        # If the win condition that is being checked is not met, then that
        # bool in <win_cond> will be set to False.
        win_cond = [True, True, True, True]
        i = 0
        # Get the value of the move in the most recent tile.
        played_move = self._board[row][col]
        # Depending on the recent move, check surrounding tiles to see if
        # a win has occured.
        # First, check along the row to see if there is a win
        while (win_cond[0] and i < self.get_dimensions()[0]):
            # If the move on the ith column at the given row is not the same as
            # the value of the most recent move, check other win cond.
            if (self._board[row][i] != played_move):
                win_cond[0] = False
            # Increment counter
            i += 1
        # Next, if the game didn't end from checking the row, check along
        # the column to see if there is a win.
        i = 0
        while (
                not win_cond[0] and win_cond[1] and i < self.get_dimensions(
                    )[1]):
            # If the move on the ith row at the given column is not the
            # same as the value of the most recent move, check other win cond.
            if (self._board[i][col] != played_move):
                win_cond[1] = False
            i += 1
        # If the move was placed on the center or top left diagonal, check
        # the tiles on the top left diagonal.
        if (any(win_cond) and (row == col)):
            i = 0
            while (win_cond[2] and i < self.get_dimensions()[0]):
                # If the move on the ith row and column is not the same as
                # the value of the most recent move, check other win cond.
                if (self._board[i][i] != played_move):
                    win_cond[2] = False
                i += 1
        # If the game hasn't ended and the move was placed on the top right
        # diagonal or center, check the top right diagonal.
        # It is on the top right diagonal if the absolute difference is 2 or
        # if <row> and <col> both are 2.
        i = 0
        if (any(win_cond) and ((((row - col) ** 2) ** 0.5) == 2 or (
                row == 2 and col == 2))):
            i = 0
            while (win_cond[3] and i < self.get_dimensions()[0]):
                # If the move on the ith row and the 3-ith column is not the
                # same as the value of the most recent move, check other win
                # cond.
                if (self._board[i][2 - i] != played_move):
                    win_cond[3] = False
                i += 1
        # If any win conditions are met (If none of <win_cond is False>)
        if any(win_cond):
            # Then the game is over
            win = True
        # Else the game is not over
        else:
            win = False
        # Return if the game is over or not.
        return win


def play_game(board):
    '''(TicTacToe) -> NoneType
    Play a game of Tic Tac Toe. Requires two players, which will alternate
    after each turn is made.
    '''
    print('Welcome to Tic Tac Toe, Pick the first move, X.')
    play_TTT(board, 1)


def play_TTT(board, turn):
    '''(TicTacToe, int) -> NoneType
    Play a game of Tic Tac Toe.
    '''
    game_ended = False
    # Check to see if the player was the first player.
    # If <turn> is odd, then the player was the first player. If <turn> is
    # even, then the player is not the first player.
    if turn % 2 == 0:
        # The player is the 'O' player. Enter their move into the board.
        move = 'O'
    else:
        # The player is the 'X' player. Enter their move into the board.
        move = 'X'
    print("TURN " + str(turn) + ":")
    (row, col) = [
        int(x) for x in input(
            "Enter two numbers that represent the tile you want to make your" +
            " move on, " + move + " (ie '1, 2'): ").split(',')]
    # Check to see if the input is within the dimensions of the board
    if ((row < 0 or row > 2) or (col < 0 or col > 2)):
        # Return an error
        raise TileError("You have entered an invalid space.")
    else:
        board.add_move(move, row, col)
        print(board)
        # Check the board to see if there is a game ended using the most recent
        # move. The game can only end if 5 or more moves have been made.
        if turn >= 5:
            game_ended = board.check_winner(row, col)
        # If the game has not ended (either there are more turns to play or
        # the game didn't end from that turn)
        if not (game_ended or turn == 9):
            # Run the function again, but switch turns to the computer
            # and increment 1 to <turn>
            play_TTT(board, turn + 1)
        # Else if there was a winner, display the player's symbol ('X' or 'O')
        else:
            if turn == 9:
                print('There is no winner!')
            else:
                print('The winner is ' + move + '! \n')

if(__name__ == '__main__'):
    while(True):
        game = TicTacToe()
        play_game(game)
