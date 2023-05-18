import customtkinter
from constants import *
from board import Board
import random

# The class which runs the game
class main():
    def __init__(self):
        game = Game()
        game.run()


class Game:
    def __init__(self):
        # Initializing variables for future use
        self.player = "X"
        self.computer = "O"
        self.playerTurn = True
        # Randomizing if computer or player goes first
        if random.randint(0, 1) == 0:
            self.player = "O"
            self.computer = "X"
            self.playerTurn = False

        # Initializing the tkinter window
        customtkinter.set_appearance_mode("system")
        self.app = customtkinter.CTk()
        self.app.title("Tic Tac Toe - Unbeatable AI")
        
    def run(self):
        # Creating frames
        self.createFrames()
        # Creating the board
        self.board = Board(player=self.player, computer=self.computer, playerTurn=self.playerTurn, app=self.frame, infoFrame=self.infoFrame)
        self.board.createBoard()
        self.board.updateBoard()

        # Making the AI move
        if not self.playerTurn:
            self.board.AIMove()

        self.app.mainloop()

    # Creates frames for the app
    def createFrames(self):
        # Frame for information like who wins and what you're playing as
        self.infoFrame = customtkinter.CTkFrame(master=self.app, fg_color="transparent")
        self.infoFrame.grid(row=0, column=0)

        # The actual board frame
        self.frame = customtkinter.CTkFrame(master=self.app, fg_color="transparent")
        self.frame.grid(row=1, column=0)


if __name__ == "__main__":
    main()
