from operator import attrgetter
import random
import pdb

class Box:
    def __init__(self, row_pos, column_pos):
        self.isVisited = False
        self.num_of_knight_moves = 0
        self.knight_visit = 0
        self.column_pos = column_pos
        self.row_pos = row_pos

    def getRowAndCol(self):
        return self.row_pos, self.column_pos

class Knight:
    def __init__(self, row, column):
        row_pos = 0
        col_pos = 1

        self.current_row_pos = row_pos
        self.current_col_pos = col_pos
        self.knight_steps = [[1,2], [-1,2], [1,-2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]
        self.traverse = 1
        self.possible_moves = [self]

    def resetPossibleMoves(self):
        for move in self.possible_moves:
            move.num_of_knight_moves = 0
        
    def setCurrentPosBasedOnMinExits(self):
        if self.possible_moves:
            box = min(self.possible_moves,key=attrgetter('num_of_knight_moves'))        
            self.current_row_pos = box.row_pos
            self.current_col_pos = box.column_pos
            self.traverse += 1
            
    def findPossibleMoves(self, chessboard):
        del self.possible_moves[:]
        for knight_step in self.knight_steps:
            new_row, new_col = self.knight_move(self.current_row_pos, self.current_col_pos, knight_step)
            if self.isNotVisitedAndInBoard(chessboard, new_row, new_col):
                box = chessboard[new_row][new_col]
                self.possible_moves.append(box)
                
    def checkExits(self, chessboard):
        for box in self.possible_moves:
            for knight_step in self.knight_steps:
                new_row, new_col = self.knight_move(box.row_pos, box.column_pos, knight_step)
                if self.isNotVisitedAndInBoard(chessboard, new_row, new_col):
                    box.num_of_knight_moves += 1

    def isNotVisitedAndInBoard(self, chessboard, row_pos, col_pos):
        chessboard_column_length = len(chessboard[0]) - 1
        chessboard_row_length = len(chessboard) - 1
        return ((((col_pos >= 0 and col_pos <= chessboard_column_length)) and ((row_pos >= 0 and row_pos <= chessboard_row_length))) and (not (chessboard[row_pos][col_pos].isVisited)))

    def knight_move(self, row_pos, col_pos, knight_step):
        new_row = row_pos + knight_step[0]
        new_col = col_pos + knight_step[1]
        return new_row, new_col

    def setCurrentBoxAsVisted(self, chessboard):
        box = chessboard[self.current_row_pos][self.current_col_pos]
        box.knight_visit = self.traverse
        box.isVisited = True

class Knight_Tour:
    def __init__(self, row, column):
        self.chessboard = []
        self.row = row
        self.column = column
        for i in range(row):
            chessboard_row = []
            for j in range(column):
                new_box = Box(i,j)
                chessboard_row.append(new_box)
            self.chessboard.append(chessboard_row)
    
    def display(self, knight):
        for i in range(self.row):
            print('[', end=' ')
            for j in range(self.column):
                box = self.chessboard[i][j]
                print(box.knight_visit,end=" ")
            print(']')

    def start(self, knight):
        while(knight.possible_moves):
            knight.setCurrentBoxAsVisted(self.chessboard)
            knight.findPossibleMoves(self.chessboard)
            knight.checkExits(self.chessboard)
            knight.setCurrentPosBasedOnMinExits()
            knight.resetPossibleMoves()
            self.display(knight)
            print()

column = 5
row = 5
kt = Knight_Tour(row, column)
knight = Knight(row-1, column-1)
kt.start(knight)