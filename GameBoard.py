"""
# Copyright Johnson Zhong, 2018
# Distributed under the terms of the GNU General Public License.
# If any errors were found or you would like to contact me about anything, you
# can reach me via GitHub (https://github.com/Johnson-Zhong) or via my email
# Johnsonz8642@gmail.com
#
# This file was created alongside the main function of play2lose, providing the
# board that will contain the game board. Originally, the board was going to be
# limited to 3x3 tiles but I decided to expand the concept of the idea and have
# the size of the board be user defined. Also, the original idea was to have
# this class only work for Tic Tac Toe boards, but I decided to make it more
# abstract and to work for all sorts of games, and instead put restrictions
# when it came to Tic Tac Toe when trying to play that game instead.
# All in all, GameBoard.py can be used as the foundation of any type of game
# that uses a tile-based board.
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
from abc import ABC, abstractmethod


class GameBoard(ABC):
    '''A class to represent objects that'll replicate a generic game board.'''
    def __init__(self, length, height):
        '''(GameBoard, int, int) -> NoneType
        Creates a new GameBoard object.
        '''
        # The items in the GameBoard object are stored in <_board>, a
        # dictionary of lists.
        # The keys of the outer dictionary are ints, representing the rows. The
        # lists of the dictionary contain the move played on the tile, where
        # the index of the move represent the column of the time. The baord is
        # index based, meaning tile positions start from 0, rather than 1.

        self._length = length
        self._height = height
        # Create the board.
        self._board = self.__blank_board__(self._length, self._height)

    @staticmethod
    def __blank_board__(length, height):
        '''(int, int) -> dict of {list of [int]}
        Given two integers representing the width and length of the board,
        create a dictionary representation of the board. This is a static
        method, as it is more of a helper method for the class.
        '''
        # Create an empty dictionary.
        board = {}
        # Create <width> different keys for the dictionary.
        for row in range(height):
            # Create an empty list per row
            l = []
            for column in range(length):
                # Append an empty string representing a blank tile for
                # each tile.
                l.append('')
            board[row] = l
        return board

    def __str__(self):
        '''(GameBoard) -> str
        Return the string representation of the board.
        '''
        # Print the elements of the row, with 1 space between each element
        board = ''
        # line by line
        for row in range(self._height):
            # Get each element in the list
            for column in range(self._length):
                # If there is no move in the tile
                if self._board[row][column] == '':
                    # Add two blank spaces
                    board += '  '
                # Else add in the move plus a space
                else:
                    board += self._board[row][column] + ' '
            board += "\n"
        return board

    def get_move(self, row, column):
        '''(GameBoard, int, int) -> str
        Get the move that is on the tile given by <row> and <tile>.
        '''
        return self._board[row][column]

    def add_move(self, move, row, column):
        '''(GameBoard, str, int, int) -> NoneType
        Add <move> to an empty tile given by <row> and <column>.
        Attempting to add a move to a tile to a nonempty tile will raise a
        TileNotEmptyError.
        '''
        # Check if the tile is able to have a move added to it
        # If the tile does not exist on the board, raise a TileError.
        if (row > self._height and column > self._length):
            raise TileError("That tile does not exist.")
        # If the tile has already has a move, raise a TileError.
        if(len(self._board[row][column]) != 0):
            raise TileError("This tile already has a move.")
        # Else it is not empty, add the move to that tile.
        else:
            self._board[row][column] = move

    def delete_move(self, row, column):
        '''(GameBoard, int, int) -> NoneType
        Delete the move at the tile given by <row> and <column if there
        is a move it.
        '''
        # If the tile does not exist on the board, raise a TileError.
        if (row > self._height or column > self._length):
            raise TileError("That tile does not exist.")
        else:
            # Else, set the tile to have a empty string.
            self._board[row][column] = ''

    def reset(self):
        '''(GameBoard) -> NoneType
        Clear the entire GameBoard, removing all added moves to tiles.
        '''
        # Change all the items to blanks by creating a new fresh board.
        self._board = self.__blank_board__(self._length, self._height)

    def get_dimensions(self):
        '''(GameBoard) -> tuple of (int, int)
        Return the dimensions of the GameBoard.
        '''
        return (self._length, self._height)

    def tile_is_empty(self, row, col):
        '''(GameBoard) -> bool
        Return whether a tile on the GameBoard is empty.
        '''
        # Check to see if the tile given by <row>, <col> is ''. If it is, then
        # it is empty.
        return self._board[row][col] == ''

    def is_empty(self):
        '''(GameBoard) -> bool
        Return whether GameBoard is empty.
        '''
        # Check if all of the tiles have '' characters iteratively by using
        # <tile_is_empty> on all tiles.
        tiles_blank = True
        row = 0
        while (row < self._height and tiles_blank):
            col = 0
            while (col < self._length and tiles_blank):
                tiles_blank = self.tile_is_empty(row, col)
                col += 1
            row += 1
        return tiles_blank

    @abstractmethod
    def check_winner(self):
        ''' (GameBoard) -> NoneType
        This is an abstract method that cannot be called except inside the
        subclass of GameBoard. This method must be overwritten.
        '''
        print("Check to see if there is a winner.")

    def test(self):
        self._board = {}
        for row in range(self._height):
            l = []
            for column in range(self._length):
                l.append('X')
            self._board[row] = l


class TileError(Exception):
    '''An error that is raised when trying to perform an invalid action on a
    tile (adding to a nonempty tile) or accessing a tile that doesn't exist.
    '''
    pass
