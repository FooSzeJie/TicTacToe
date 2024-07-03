class TikTacToe: 
    def __init__(self):
        # Initialize the board with empty strings
        self.ttt = {
            'top-l': '', 'top-c': '', 'top-r': '',
            'mid-l': '', 'mid-c': '', 'mid-r': '',
            'bot-l': '', 'bot-c': '', 'bot-r': '',
        }

    def print_tile(self): 
        # Print the current state of the board
        print(self.ttt['top-l'], '|', self.ttt['top-c'], '|', self.ttt['top-r'])
        print('- + - + -')
        print(self.ttt['mid-l'], '|', self.ttt['mid-c'], '|', self.ttt['mid-r'])
        print('- + - + -')
        print(self.ttt['bot-l'], '|', self.ttt['bot-c'], '|', self.ttt['bot-r'])

    def PlayerSymbol(self, player1):
        # Determine the symbol for player 2 based on player 1's choice
        if player1 == 'x':
            player2 = 'o'
        else: 
            player2 = 'x'

        return player1, player2

    def positionName(self, positionName, symbol):
         # Place the symbol on the board if the position is valid and empty
        match positionName:
            case 'tl':
                if self.ttt['top-l'] == '':
                    self.ttt['top-l'] = symbol
                    return True;
                else:
                    return False
                    
            case 'tc':
                if self.ttt['top-c'] == '':
                    self.ttt['top-c'] = symbol
                    return True;
                else:
                    return False
                    
            case 'tr':
                if self.ttt['top-r'] == '':
                    self.ttt['top-r'] = symbol
                    return True;
                else:
                    return False
                    
            case 'ml':
                if self.ttt['mid-l'] == '':
                    self.ttt['mid-l'] = symbol
                    return True;
                else:
                    return False
            case 'mc':
                if self.ttt['mid-c'] == '':
                    self.ttt['mid-c'] = symbol
                    return True;
                else:
                    return False
                    
            case 'mr':
                if self.ttt['mid-r'] == '':
                    self.ttt['mid-r'] = symbol
                    return True;
                else:
                    return False
                    
            case 'bl':
                if self.ttt['bot-l'] == '':
                    self.ttt['bot-l'] = symbol
                    return True;
                else:
                    return False
                    
            case 'bc':
                if self.ttt['bot-c'] == '':
                    self.ttt['bot-c'] = symbol
                    return True;
                else:
                    return False
            case 'br':
                if self.ttt['bot-r'] == '':
                    self.ttt['bot-r'] = symbol
                    return True;
                else:
                    return False  

    def Player1Section(self, symbol):
        # Allow Player 1 to select a position and place their symbol
        while True:
            player1Position = input('\nPlayer 1, What position you want to tic?')

            if self.positionName(player1Position, symbol):
                break
            else:
                print("Position already taken or invalid. Try again.")

        self.print_tile()

    def Player2Section(self, symbol):
        # Allow Player 2 to select a position and place their symbol
        while True:
            player2Position = input('\nPlayer 2, What position you want to tic?')
            if self.positionName(player2Position, symbol):
                break
            else:
                print("Position already taken or invalid. Try again.")
                
        self.print_tile()

    def winnerCondition(self, player1, player2):
        # Check for a win or draw condition
        # Player 1 Win condition
        if (
            (self.ttt['top-l'] == player1 and self.ttt['top-c'] == player1 and self.ttt['top-r'] == player1) or 
            (self.ttt['mid-l'] == player1 and self.ttt['mid-c'] == player1 and self.ttt['mid-r'] == player1) or
            (self.ttt['bot-l'] == player1 and self.ttt['bot-c'] == player1 and self.ttt['bot-r'] == player1) or
            (self.ttt['top-l'] == player1 and self.ttt['mid-l'] == player1 and self.ttt['bot-l'] == player1) or
            (self.ttt['top-c'] == player1 and self.ttt['mid-c'] == player1 and self.ttt['bot-c'] == player1) or
            (self.ttt['top-r'] == player1 and self.ttt['mid-r'] == player1 and self.ttt['bot-r'] == player1) or
            (self.ttt['top-l'] == player1 and self.ttt['mid-c'] == player1 and self.ttt['bot-r'] == player1) or
            (self.ttt['top-r'] == player1 and self.ttt['mid-c'] == player1 and self.ttt['bot-l'] == player1)
           ):
            print('Player 1 is Winner!')
            return True

        # Player 2 Win condition
        elif (
            (self.ttt['top-l'] == player2 and self.ttt['top-c'] == player2 and self.ttt['top-r'] == player2) or
            (self.ttt['mid-l'] == player2 and self.ttt['mid-c'] == player2 and self.ttt['mid-r'] == player2) or
            (self.ttt['bot-l'] == player2 and self.ttt['bot-c'] == player2 and self.ttt['bot-r'] == player2) or
            (self.ttt['top-l'] == player2 and self.ttt['mid-l'] == player2 and self.ttt['bot-l'] == player2) or
            (self.ttt['top-c'] == player2 and self.ttt['mid-c'] == player2 and self.ttt['bot-c'] == player2) or
            (self.ttt['top-r'] == player2 and self.ttt['mid-r'] == player2 and self.ttt['bot-r'] == player2) or
            (self.ttt['top-l'] == player2 and self.ttt['mid-c'] == player2 and self.ttt['bot-r'] == player2) or
            (self.ttt['top-r'] == player2 and self.ttt['mid-c'] == player2 and self.ttt['bot-l'] == player2)
        ):
            print('Player 2 is the Winner!')
            return True

         # Draw condition
        elif '' not in self.ttt.values():
            print('The game is a draw.')
            return True

        return False
            
            
    def PlayGame(self, player1):
        # Main game loop
        player1, player2 = self.PlayerSymbol(player1)
            
        while True:
            print('\ntop left = tl \ntop center = tc \ntop right = tr')
            print('\nmid left = ml \nmid center = mc \nmid right = mr')
            print('\nbottom left = bl \nbottom center = bc \nbottom right = br')

            while True:
                self.Player1Section(player1)
                if self.winnerCondition(player1, player2):
                    break

                self.Player2Section(player2)
                if self.winnerCondition(player1, player2):
                    break
            break
        
        