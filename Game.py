from Player import Player
from Board import Board

class Game:
    def __init__(self):
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board()

    def get_winner(self):
        if self.board.tictactoe() == self.player1.get_symbol():
            return self.player1.name
        if self.board.tictactoe() == self.player2.get_symbol():
            return self.player2.name
        else:
            return None


    def play_game(self):
        print("Welcome to Tic Tac Toe")
        
        p1_name = input("Enter player 1's name: ")
        p2_name = input("Enter player 2's name: ")
        self.player1.set_name(p1_name)
        self.player2.set_name(p2_name)

        while(True):
            self.board.show()
            

            while(self.board.existsMove()):
                self.board.add_move(self.player1, self.player1.choose_move())
                self.board.show()
                if(self.board.tictactoe() is not None):
                    break

                self.board.add_move(self.player2, self.player2.choose_move())
                self.board.show()
                if(self.board.tictactoe() is not None):
                    break


            winner = self.get_winner()
            if(winner is None):
                print("It's a tie!")
            else:
                print(winner + " Wins!")


            print("Would you like to play again?")
            play_again = input("Y for yes, N for no: ")
            if(play_again == "Y"):
              self.board.reset()
            else:
                break


if __name__ == '__main__':
    game = Game()
    game.play_game()

        