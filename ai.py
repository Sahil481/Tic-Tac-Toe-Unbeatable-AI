
'''This is the file which gives us the best move to play using minimax algorithm'''

class AI:
    def __init__(self, board, computer, player):
        # Intializing varibales
        self.board = board
        self.player = player
        self.computer = computer

    # Finding the best move to play
    def bestMove(self):
        bestScore = -800
        bestMove = 0

        for key in self.board.keys():
            if self.board[key] == " ":
                self.board[key] = self.computer
                score = self.minimax(False)
                self.board[key] = " "

                if score > bestScore:
                    bestScore = score
                    bestMove = key
        return bestMove
    
    # Check if the move leads to a win
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

        return None
    
    # Check if the move leads to a draw
    def checkDraw(self):
        for value in self.board.values():
            if value == " ":
                return False
        
        return True
    
    # The minimax algorithm for finding the bestmove
    def minimax(self, isMaximizing):
        # Check who won
        if self.checkWin() == self.computer:
            return 1
        elif self.checkWin() == self.player:
            return -1
        elif self.checkDraw():
            return 0
        
        # If computer turn
        if isMaximizing:
            # Find best move
            bestScore = -800
            for key in self.board.keys():
                if self.board[key] == " ":
                    self.board[key] = self.computer
                    score = self.minimax(False)
                    self.board[key] = " "
                    if score > bestScore:
                        bestScore = score
            return bestScore
        # If player turn
        else:
            bestScore = 800
            for key in self.board.keys():
                if self.board[key] == " ":
                    self.board[key] = self.player
                    score = self.minimax(True)
                    self.board[key] = " "
                    if score < bestScore:
                        bestScore = score
            return bestScore