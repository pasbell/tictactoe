class Player:
    def __init__(self, symbol, name = "Unknown"):
        self.name = name
        self.symbol = symbol

    def set_name(self, name):
        self.name = name
    
    def get_symbol(self):
        return self.symbol

    def choose_move(self):
        print(self.name + ": ")
        x = input("Enter the column value of your move: ")
        y = input("Enter the row value of your move: ")

        return (x,y)

if __name__ == '__main__':
    p = Player("X")
    p.set_name("Pascale")
    print(p.choose_move())