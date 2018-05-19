"""
# Copyright Johnson Zhong, 2018
# Distributed under the terms of the GNU General Public License.
# If any errors were found or you would like to contact me about anything, you
# can reach me via GitHub (https://github.com/Johnson-Zhong) or via my email
# Johnsonz8642@gmail.com
#
# This program requires the supplementary files
# GameBoard.py and TicTacToe.py to operate, as this file imports from them.
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

from TicTacToe import *
from random import *


def play2lose(board):
    '''(TicTacToe) -> NoneType
    Given a 3x3 Tic Tac Toe board, play a game with Tic Tac Toe by typing in
    moves that you want to make. The function asks the user which player will
    go first (user or computer) and then asks for inputs for moves.
    When the game is over, return whether the computer won the match TicTacToe
    game or in the worst case, tied. The player who moves first is 'X', while
    the other player is 'O'. This function only works for 3x3 boards and will
    refuse to work if <board> is not 3x3. The function uses index based
    counting, meaning it starts counting at 0.
    '''
    # Verify that the board is TicTacToe board.
    if not(isinstance(board, TicTacToe)):
        result = 'play2lose only works for TicTacToe boards.'
    else:
        print(
            'Welcome to play2lose, the game that you will never win.\nPlay a' +
            ' standard game of Tic Tac Toe with the computer, and enter your' +
            ' moves.\nYou will never win a game, no matter what moves you' +
            ' make.\nNote that when entering moves, the function uses 0' +
            ' based counting, rather than starting at 1.\nTo start, decide' +
            ' who will go first, you or the computer.\n')
        got_first_player = False
        # Loop until the user makes valid input
        while not (got_first_player):
            # Get first_player through user input
            first_player = input('Enter the first player ("H" or "C") ')
            # Catch if the user made an invalid input
            if (first_player != 'H' and first_player != 'C'):
                print('Invalid input, enter "H" or "C" or we cannot play.\n')
            else:
                got_first_player = True
        # Use a helper function to play out the game.
        play_losing_game(board, first_player, 1)


def play_losing_game(board, player, turn):
    '''(TicTacToe, str, int) -> NoneType
    Given a 3x3 Tic Tac Toe board, play a game of Tic Tac Toe. If it is
    the user's turn, input the move you want to make.
    Otherwise, the computer will play its move. The current board will be
    printed out after turn is made.
    '''
    game_ended = False
    print("TURN " + str(turn) + ":")
    # If it is the player's turn, get their input on the move they want to make
    if player == 'H':
        # Check to see if the player was the first player.
        # If <turn> is odd, then the player was the first player. If <turn> is
        # even, then the player is not the first player.
        if turn % 2 == 0:
            # The player is the 'O' player. Enter their move into the board.
            move = 'O'
        else:
            # The player is the 'X' player. Enter their move into the board.
            move = 'X'
        (row, column) = [
            int(x) for x in input(
                "Enter two numbers that represent the tile you want to" +
                " make your move on, " + move + " (ie '1, 2'): ").split(',')]
        # Check to see if the input is within the dimensions of the board
        if ((row < 0 or row > 2) or (col < 0 or col > 2)):
            # Return an error
            raise TileError("You have entered an invalid space.")
        else:
            board.add_move(move, row, column)
            # Switch to the computer's turn and increment <turn>.
            player = 'C'
            turn += 1
            print(board)
    # Else if it the computer's turn, calculate their move.
    if player == 'C':
        # Run the algorithm for the computer's turn.
        generate_move(board, turn, row, column)
        # Check the board to see if there is a game ended using the most recent
        # move. The game can only end if 5 or more moves have been made.
        if turn >= 5:
            game_ended = board.check_winner((row, column))
    print(board)
    # Check the board to see if there is a game ended using the most recent
    # move. The game can only end if 5 or more moves have been made.
    if turn >= 5:
        game_ended = board.check_winner((row, column))
    # If the game has not ended (either there are more turns to play or
    # the game didn't end from that turn)
    if not (game_ended or turn == 9):
        # Run the function again and switch the player to be the human player.
        play_losing_game(board, 'H', turn + 1)
    # Else if there was a winner, display who won the game.
    else:
        # If the winner was the human player
        if player == 'H':
            winner = ' the human player!'
        # Else if the winner was the computer
        else:
            winner = ' the computer player, unsurprisingly.'
        print('The winner is' + winner)


def generate_move(board, turn):
    '''(TicTacToe, int) -> NoneType
    Given a TicTacToe object, and the number of turns that the game went
    through, generate the best move that the computer can
    take on its turn.
    '''
    # Through the states of the game board, choose the best move. There are 3
    # moves that the computer can take, 'corner', 'centre', and 'side'.
    # All of the possible moves in Tic Tac Toe can be described as one of these
    # plays, as the board can be rotated any way to produce a similar game.
    # ///MIGHT DELETE THIS BECAUSE THIS IS KINDA A BAD WAY
    # The computer should start out by playing on any corner tile on
    # the first turn.
    if turn == 1:
        # Get two random numbers (0 or 2) to get the position of the tile
        # we will play.
        row = choice([i for i in range(0, 3) if i not in [1]])
        col = choice([i for i in range(0, 3) if i not in [1]])
        # Since the computer plays on the first turn, it is the 'X' player.
        board.add_move('X', row, col)
    # Else, if it isn't the first move, the computer will have to play
    # depending on the current state of the game.
    else:
        move_over = False
        # Get the computer's symbol. The computer always plays 'X on odd turns,
        # 'O' on even turns.
        if turn % 2 == 0:
            move = 'O'
            oppo = 'X'
        else:
            move = 'X'
            oppo = 'O'
        # First, check if the computer has any win conditions play it if it
        # exists. If it does, then its turn is over.
        winning_move = play_winning_move(board, move)
        # If winning_move is not None, place the move at that tile.
        if winning_move is not None:
            move_over = True
            board.add_move(move, winning_move[0], winning_move[1])
        # If the computer does not have a winning move, then check if the
        # player has any winning moves. This is done by checking if there are
        # any win conditions for the opponent. If there is a win condition
        # for the opponent, block it.
        if not move_over:
            block_win = play_winning_move(board, oppo)
            # If there is a winning move for the opponent, block it by
            # placing you next move in that tile.
            if block_win is not None:
                move_over = True
                board.add_move(move, block_win[0], block_win[1])
        # Now, dpeending on the situation of the board, play corner, centre
        # or side..
        # If there the opponent has two opposite corners and the computer has
        # centre, choose a side to block the opponent.
        if (board.get_move(1, 1) == move and (
            (board.get_move(0, 2) == oppo and board.get_move(
                2, 0) == oppo) or (board.get_move(
                    0, 0) == oppo and board.get_move(2, 2) == oppo))):
        # Play a random unblocked side tile.
            found_side = False
            while found_side != False:
                row = choice([i for i in range(0, 3) if i not in [1]])

def play_winning_move(board, move, player):
    '''(TicTacToe, str, str) -> tuple of (int, int) or NoneType
    Given a TicTacToe object, the move that is going to be played next, and
    the player who is trying to win, return the co-ordinates of the tile that
    will lead to a win. If no win can be made from the next move, return None.
    '''
    # Clone the current board object
    
    # The computer will need to play their move in every open slot.
    found_move = False    
    move_to_play = None
    row = 0
    # Search the row for a winning move
    while (not found_move and row < board.get_dimensions()[0]):
        # Search the column for a winning move
        col = 0
        while (not found_move and col < board.get_dimensions()[0]):
            # Check to see if the move can be placed in the tile
            if not board.is_tile_empty(row, col):
                # Place the move in that tile
                board.add_move(move, row, col)
                # Check if that lead to a win
                win = board.check_winner(row, col)
                if win:
                    # If this was a win condition, then this is the move that
                    # will be played next.
                    found_move = True
                    move_to_play = (row, col)
                # Delete the move afterward to not make changes to the board.
                board.delete_move(row, col)
            col += 1
        row += 1
    # If by the end of this loop <found_move> is still False, then a winning
    # move cannot be found. If there is a winning move, return the tile that
    # the player needs to play the move.
    if found_move:
        move_to_play = (row, col)
    # Return the winning move.
    return move_to_play
if (__name__ == "__main__"):
    print('---PLAY THE GAME---')
    x = TicTacToe()
    play2lose(x)
