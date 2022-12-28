import random
# from time import sleep
from collections import defaultdict
import tkinter as tk
# Need to import tkinter.font separately?
import tkinter.font as tkfont


class Game():
    """A game of noughts and crosses"""
    MOVES = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    WINNERS = {(0, 1, 2): "Top row", (3, 4, 5): "Middle row", (6, 7, 8): "Bottom row",
               (0, 3, 6): "Left column", (1, 4, 7): "Middle column", (2, 5, 8): "Right column",
               (0, 4, 8): "Top-left to bottom-right diagonal", (2, 4, 6): "Top-right to bottom-left diagonal"}
    TOKENS = {'X': 1, 'O': 2}

    def __init__(self):
        self.moveList = []
        self.winner = 0

    def check_winner(self):
        """Checks to see whether the last player to move has won"""
        result = None
        # Check moves for the last player to have moved (game would already be over if the other player had won)
        player = self.last_player()
        # The elements of self.moveList with even numbered index values belong to 'X'
        if player == 'X':
            playerMoves = [self.moveList[i] for i in range(len(self.moveList)) if i % 2 == 0]
        else:
            playerMoves = [self.moveList[i] for i in range(len(self.moveList)) if i % 2 == 1]
        # Only need to check the results for the current player since this method is called after each move
        for combo in Game.WINNERS:
            if set(combo).issubset(playerMoves):
                result = Game.TOKENS[player]
                # Have to return the result here - otherwise only the last combo in Game.WINNERS can win on the ninth move (see elif below)
                return result
            elif len(self.moveList) == 9:
                result = 3
        return result

    def get_available_moves(self):
        """Returns a set of the moves that have not yet been taken"""
        availableMoves = set(Game.MOVES).difference(set(self.moveList))
        return availableMoves

    def next_player(self):
        """Returns the next player to move, based on a current move number"""
        # If there has been no moves, len(self.moveList = 0 and 'X' is the next to move
        return 'X' if len(self.moveList) % 2 == 0 else 'O'

    def last_player(self):
        """Returns the last player to move by returning the opposite of self.next_player()"""
        return 'X' if self.next_player() == 'O' else 'O'

    def update_moves(self, move):
        self.moveList.append(move)
        self.winner = self.check_winner()


class HumanPlayer():
    """A human player for a game of noughts and crosses"""

    def __init__(self, name):
        self.name = name
        self.type = "Human"

    def set_name(self, newName):
        self.name = newName


class ComputerOpponent():
    """A computer opponent for a game of noughts and crosses"""

    def __init__(self, GameObject, token):
        self.game = GameObject
        self.token = token
        self.name = 'The computer'
        self.type = "computer"

    def set_name(self, newName):
        pass

    def get_player_move(self):
        """Chooses the best move based on the results of self.check_possible_moves()"""
        # Take the centre square on the first move
        # Running self.check_possible_moves() for an empty grid suggests that the centre is the best square to take on the first move
        if len(self.game.moveList) == 0:
            choice = 4
        # Likewise, self.check_possible_moves() indicates that the centre is the best option for the second move if not already taken
        # If the centre is taken first, one of the corner squares is the next best
        # Because the choice of opening move is quite limited, there is no need to recalculate this at the start of every game
        elif len(self.game.moveList) == 1:
            # Take a random corner square if opponent takes the centre on first go
            if self.game.moveList[0] == 4:
                choice = random.choice([0, 2, 6, 8])
            # Otherwise take the centre
            else:
                choice = 4
        # From third move onwards use analyse_next move and take the best option
        else:
            possibleMoves = self.check_possible_moves()
            # Analyse_next_move ranks moves from best to worst for X
            if self.token == 'X':
                # so possible_moves[0] is at least joint-best for X
                bestMove = possibleMoves[0]
            else:
                # so possible_moves[-1] is at least joint-best for O
                bestMove = possibleMoves[-1]
            # Discard any moves that have a different (i.e. worse) ranking than the best move
            bestMoves = [move for move in possibleMoves if move[1] == bestMove[1]]
            # Randomly select one of the moves with the best score
            choice = random.choice(bestMoves)[0]
        # print(self.name, ' takes ', choice)
        return choice

    def check_possible_moves(self):
        """Calculates all possible move combinations and ranks the results for each of the available moves"""
        availableMoves = self.game.get_available_moves()
        movesSoFar = self.game.moveList
        finishes = [[]]
        # finishes is a list of all of the possible move combinations to fill the grid from the current game position
        for i in range(len(availableMoves)):
            tempList = [subList + [elem]
                        for subList in finishes
                        for elem in availableMoves
                        if elem not in subList]
            finishes = tempList
        # possible moves is a list of with each element being a list that represents: [the next move square, the score for the full set of moves from self.get_winning_move()]
        possibleMoves = [[finish[0],
                          self.get_winning_move(movesSoFar + finish)]
                         for finish in finishes]
        resultsDict = defaultdict(int)
        # Now for each available square (i.e. possible next move) add up the scores for the possible moves combinations that start with that square
        for move in possibleMoves:
            # print(move)
            resultsDict[move[0]] += move[1]
        # sort the results in order of decreasing score
        rankedResults = sorted([[dkey, value] for dkey, value in resultsDict.items()], key=lambda x: x[1], reverse=True)
        # print(ranked_results)
        return rankedResults

    def get_winning_move(self, fullGame):
        """Checks a set of moves for winners from move five onwards, returns the winner and the winning move number"""
        for i in range(5, 10):
            # X has just moved if i is odd (e.g. i = 1 means one move in move_list)
            playerMoves = [fullGame[j] for j in range((i + 1) % 2, i, 2)]
            for combo in Game.WINNERS:
                if set(combo).issubset(playerMoves):
                    # This is the heart of the computer oponent's strategy - I have tried a few different ways of scoring the possible outcomes
                    # Option 1: return the winning move number (even implies X won)
                    # return i
                    # Option 2: return +1 for X wins and -1 for O wins
                    # return (-1) ** ((i + 1) % 2)
                    # Option 3: return higher values for wins and losses in fewer moves
                    return (-1) ** ((i + 1) % 2) * (10 - i)
        # return 0 for a tie
        return 0


class Board(tk.Frame):
    """A board for a game of noughts and crosses"""
    # Board.BUTTONS contains info for each button in the format (button number, xpos, ypos)
    BUTTONS = ((0, 0, 0), (1, 1, 0), (2, 2, 0), (3, 0, 1), (4, 1, 1), (5, 2, 1), (6, 0, 2), (7, 1, 2), (8, 2, 2))

    def __init__(self, rootWindow):
        super(Board, self).__init__(rootWindow)
        # 0 = game in progress, 1 = X wins, 2 = O wins, 3 = Tie
        self.rootWindow = rootWindow
        self.grid()
        self.buttons = []
        self.labelFont = tkfont.Font(size=11)
        self.namesPopUp = NamesWindow(self)
        self.add_elements()
        # Don't use pack and grid together!
        # self.pack()
        self.theGame = Game()
        self.isOver = False
        self.players = {'X': HumanPlayer(self.namesPopUp.p1Name), 'O': HumanPlayer(self.namesPopUp.p1Name)}
        self.computerPlayers = 0

    def get_result_description(self):
        """Returns a text string describing the result (assuming self.theGame.winner != 0)"""
        results = {1: self.players['X'].name + ' wins!',
                   2: self.players['O'].name + ' wins!',
                   3: 'Game tied.'}
        return results[self.theGame.winner]

    def add_elements(self):
        """Adds the buttons and the menus to the game window"""
        buttonFont = tkfont.Font(size=36, weight='bold')
        for buttonOptions in Board.BUTTONS:
            buttonNumber, xpos, ypos = buttonOptions
            blank = ''
            # Use width = height = 1 to create buttons wuth a minimal size and add padding with padx and pady
            button = tk.Button(self, text=blank, width=1, height=1, borderwidth=3, font=buttonFont,
                               padx=20, pady=15, command=lambda b=buttonNumber: self.button_click(b))
            button.grid(column=xpos, row=ypos, padx=1, pady=1)
            self.buttons.append(button)
        self.info = tk.Label(self, text='New 2 player game started.', font=self.labelFont)
        self.info.grid(column=0, row=3, columnspan=3, sticky='W')
        menu = tk.Menu(self.rootWindow)
        self.rootWindow.configure(menu=menu)
        gameMenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='Game', menu=gameMenu)
        newGameSubmenu = tk.Menu(gameMenu, tearoff=0)
        newGameSubmenu.add_command(label='1 player vs. computer', command=self.new_1player_game)
        newGameSubmenu.add_command(label='2 player', command=self.new_2player_game)
        gameMenu.add_cascade(label='Start new game', menu=newGameSubmenu)
        gameMenu.add_command(label='Exit', command=self.exitProgram)
        playersMenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='Players', menu=playersMenu)
        playersMenu.add_command(label='Player names ...', command=self.namesPopUp.names_pop_up)

    def button_click(self, buttonNumber):
        """Checks whether a clicked button is available - if it is, self.update_game() is called"""
        nextToken = self.theGame.next_player()
        player = self.players[nextToken]
        # Clear any previous messages - the label will be updated later if new info is generated
        self.info['text'] = ''
        if self.isOver:
            # Buttons do nothing if the game is over
            self.info['text'] = 'Game over. ' + self.get_result_description()
        elif player.type == 'computer':
            # Buttons do nothing if clicked during the computer's turn
            self.info['text'] = 'Waiting for computer move.'
        elif self.buttons[buttonNumber]['text'] != '':
            self.info['text'] = 'That square is already taken.'
        else:
            self.update_game(buttonNumber, nextToken)
            if (self.computerPlayers == 1) and (not self.isOver):
                computerMove = self.players['O'].get_player_move()
                self.info['text'] = 'The computer takes square ' + str(computerMove + 1)
                self.update_game(computerMove, 'O')

    def update_game(self, buttonNumber, playerToken):
        button = self.buttons[buttonNumber]
        colours = {'X': '#ff0000', 'O': '#0000ff'}
        colour = colours[playerToken]
        button['activeforeground'] = colour
        button['fg'] = colour
        button['text'] = playerToken
        self.theGame.update_moves(buttonNumber)
        if self.theGame.winner:
            self.info['text'] = self.get_result_description()
            self.isOver = True

    def new_1player_game(self):
        self.info['text'] = 'New game vs computer started.'
        self.reset_game()
        self.players['X'] = HumanPlayer(self.namesPopUp.p1Name)
        self.players['O'] = ComputerOpponent(self.theGame, 'O')
        self.computerPlayers = 1

    def new_2player_game(self):
        self.info['text'] = 'New 2 player game started.'
        self.reset_game()
        self.players['X'] = HumanPlayer(self.namesPopUp.p1Name)
        self.players['O'] = HumanPlayer(self.namesPopUp.p2Name)
        self.computerPlayers = 0

    def reset_game(self):
        for button in self.buttons:
            button['text'] = ''
        self.isOver = False
        self.theGame = Game()

    def exitProgram(self):
        exit()


class NamesWindow():
    def __init__(self, BoardObject):
        self.board = BoardObject
        self.p1Name = 'Player 1'
        self.p2Name = 'Player 2'

    def names_pop_up(self):
        labelFont = tkfont.Font(size=11)
        self.names = tk.Toplevel()
        self.names.wm_title('Names')
        namesLabel = tk.Label(self.names, text='Enter players\' names', font=labelFont)
        namesLabel.grid(row=0, column=0, columnspan=2)
        p1Label = tk.Label(self.names, text='Player 1:', font=labelFont)
        p1Label.grid(row=1, column=0, sticky='W', pady=2)
        self.p1Entry = tk.Entry(self.names)
        self.p1Entry.insert(0, self.p1Name)
        self.p1Entry.grid(row=1, column=1, sticky='W', padx=4, pady=2)
        p2Label = tk.Label(self.names, text='Player 2:', font=labelFont)
        p2Label.grid(row=2, column=0, sticky='W', pady=2)
        self.p2Entry = tk.Entry(self.names)
        self.p2Entry.insert(0, self.p2Name)
        self.p2Entry.grid(row=2, column=1, sticky='W', padx=4, pady=2)
        names_button = tk.Button(self.names, text='OK', command=self.set_player_names)
        names_button.grid(row=3, column=0, columnspan=2, pady=2)

    def set_player_names(self):
        self.p1Name = self.p1Entry.get()
        self.p2Name = self.p2Entry.get()
        self.board.players['X'].set_name(self.p1Name)
        self.board.players['O'].set_name(self.p2Name)
        self.names.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Noughts and crosses')
    newgame = Board(root)
    root.mainloop()