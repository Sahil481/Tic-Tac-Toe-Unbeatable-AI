from constants import *
from customtkinter import CTkButton, CTkLabel
from ai import AI
    
'''This is the file which handles every task related to the board and also the information frame'''

class Board():

    def __init__(self, player, computer, playerTurn, app, infoFrame):
        # Intializing everything
        self.player = player
        self.computer = computer
        self.playerTurn = playerTurn
        self.infoFrame = infoFrame
        self.app = app
        self.buttons = {}
        self.board = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "}
        self.drawOnce = True

    # Creating the buttons
    def createBoard(self):
        # Creating all 9 buttons
        for i in range(9):
            # Looping through everything and pushing the button to the buttons dict
            button = Button().createButton(app=self.app, btnId=i, board=self)
            button.grid(row=i // 3, column=i % 3)
            self.buttons[i] = button 

        # The "you're playing as " text
        message = f"You're playing as {self.player}"
        self.label = CTkLabel(self.infoFrame, fg_color=TEXT_FG_COLOR, text_color=TEXT_COLOR, font=("Helvetica", 20), width=200, height=100, text=message)
        self.label.pack()

    # This function updates the visual representation of the board
    def updateBoard(self):
        for btnId, button in self.buttons.items():
            # Changing the button text relevant to the board array
            button.configure(text=self.board[btnId])
            # Changing the button state if it's available
            if button.cget("text") == " ":
                button.configure(state="normal")
            else:
                button.configure(state="disabled")

    # This updates the info bar to show the winner
    def showWinnerMessage(self, winner):
        message = f"{winner} Won!!"
        # Color green if won red if lost
        if winner == self.player:
            text_color="#32CD32"
        else:
            text_color="#cc0000"
        # Creating the actual text
        label = CTkLabel(self.infoFrame, fg_color=TEXT_FG_COLOR, text_color=text_color, font=("Helvetica", 15), width=200, height=50, text=message, anchor="n")
        self.label.configure(height=60)
        label.pack()

    # This updates the info bar to show that the match was a draw
    def showDraw(self):
        # Just draws once (because of bugs)
        if self.drawOnce:
            label = CTkLabel(self.infoFrame, fg_color=TEXT_FG_COLOR, text_color=TEXT_COLOR, font=("Helvetica", 15), width=200, height=50, text="Draw!", anchor="n")
            label.pack()
            self.label.configure(height=60)
        self.drawOnce = False

    # Handle the click of a button
    def handleClick(self, id):
        # Change the board array to the button pressed
        self.board[id] = self.player
        self.playerTurn = not self.playerTurn
        # Update the visual representation of the board
        self.updateBoard()
        # Check if won or draw?
        winner = self.checkWin()
        if self.checkWin() != None:
            self.showWinnerMessage(winner)
        elif self.checkDraw():
            self.showDraw()
        else:
            # Making the AI move after player
            self.AIMove()

    # Making the AI Move
    def AIMove(self):
        # Getting the best move
        ai = AI(board=self.board, computer=self.computer, player=self.player)
        bestMove = ai.bestMove()

        # Updating the board
        self.board[bestMove] = self.computer
        self.updateBoard()

        # Checking to see if won or draw?
        winner = self.checkWin()
        if self.checkWin() != None:
            self.showWinnerMessage(winner)
        elif self.checkDraw():
            self.showDraw()

    
    # Checks if anyone won or not
    def checkWin(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != " ":
                return self.board[i]

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return self.board[i]

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]

        # No one won
        return None
    
    # Checks if the match was a draw
    def checkDraw(self):
        for value in self.board.values():
            if value == " ":
                return False
        
        return True

# Creates the button
class Button():
    def createButton(self, app, btnId, board):
        button = CTkButton(app, text=" ", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, border_width=BUTTON_BORDER_WIDTH, border_color=BUTTON_BORDER_COLOR, fg_color=BUTTON_FG_COLOR, font=BUTTON_FONT, hover_color=BUTTON_HOVER_COLOR, state="normal", command=lambda: board.handleClick(id=btnId))
        return button