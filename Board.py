import pandas as pd

class Board:
    def __init__(self):
        self.board = pd.DataFrame([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], columns=['A', 'B', 'C'])

    def existsMove(self):
        return True in self.board.apply(lambda x: " " in x.values).values

    def add_move(self, player, move):
        if(not self.is_valid_move(move)):
            print("Not a valid move. Try Again")
            new_move = player.choose_move()
            self.add_move(player, new_move)
        else:
            self.board[move[0]].iloc[int(move[1])] = player.get_symbol()


    def is_valid_move(self, move):
        valid = True
        if(move[0] not in ['A', 'B', 'C']): valid = False
        elif(move[1] not in ['0', '1', '2']): valid = False
        elif self.board[move[0]].iloc[int(move[1])] != " " : valid = False
        
        return valid


    def show(self):
        print("   A B C")
        print("0", end = "  ")
        print(self.board['A'].iloc[0] + "|" + self.board['B'].iloc[0]+ "|" + self.board['C'].iloc[0])
        print("  -------")
        print("1", end = "  ")
        print(self.board['A'].iloc[1] + "|" + self.board['B'].iloc[1]+ "|" + self.board['C'].iloc[1])
        print("  -------")
        print("2", end = "  ")
        print(self.board['A'].iloc[2] + "|" + self.board['B'].iloc[2]+ "|" + self.board['C'].iloc[2])


    def tictactoe(self):
        #row win
        row_win = self.board.apply(lambda x : (len(x.unique()) == 1) & (" " not in x.unique()), 1)
        r = row_win[row_win==True].index.tolist()
        if(len(r) > 0):
            return self.board.iloc[r[0]]['A']


        #column win
        col_win = self.board.apply(lambda x : (len(x.unique()) == 1) & (" " not in x.unique()), 0)
        c = col_win[col_win==True].index.tolist()
        if(len(c) > 0):
            return self.board[c[0]].iloc[0]

        #diagonal win
        if((self.board['A'].iloc[0] == self.board['B'].iloc[1]) & ((self.board['A'].iloc[0] == self.board['C'].iloc[2]))):
            if(self.board['A'].iloc[0] is not " "):
                return self.board['A'].iloc[0]
        if((self.board['A'].iloc[2] == self.board['B'].iloc[1]) & ((self.board['A'].iloc[2] == self.board['C'].iloc[0]))):
            if(self.board['A'].iloc[2] is not " "):
                return self.board['A'].iloc[2]


    def reset(self):
        self.board = pd.DataFrame([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], columns=['A', 'B', 'C'])


if __name__ == '__main__':
    from Player import Player
    new_board = Board()
    p1 = Player("X")
    p2 = Player("O")
    new_board.add_move(p1, ("A","0"))
    new_board.add_move(p2, ("A","1"))
    new_board.add_move(p1, ("A","2"))
    new_board.add_move(p2, ("B","0"))
    new_board.add_move(p1, ("B","1"))
    new_board.add_move(p1, ("B","2"))
    new_board.add_move(p1, ("C","0"))
    new_board.add_move(p2, ("C","1"))
    new_board.add_move(p1, ("C","2"))


    new_board.show()
    print(new_board.existsMove())
    print(new_board.tictactoe())
