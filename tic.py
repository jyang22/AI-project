import random
import sys
import getopt

class gameBoard(object):
    winning_states = (

    [0,1,2],[3,4,5],[6,7,8],

    [0,3,6],[1,4,7],[2,5,8],

    [0,4,8],[2,4,6])

    game_board = ([0,1,2],[3,4,5],[6,7,8])

    squares = (0,1,2,3,4,5,6,7,8)

    markers = ('_','X','O')

    x_token = -1
    open_token = 0
    o_token = 1

    def __init__(self):

        self.board = [0 for i in range(9)]

    def show_board(self):
        for row in self.game_board:
            for slot in row:
                print '|'+self.markers[self.board[slot]]+'|',
            print

    def legal_move(self):
        for slot in self.squares:
            if self.board[slot] == 0:
                return True
        return False

    def winner(self):
        for combo in self.winning_states:
            combo_sum= self.board[combo[0]] + self.board[combo[1]]+ self.board[combo[2]]
            if combo_sum == 3 or combo_sum == -3:
                return self.board[combo[0]]
        return 0

    def newGame(self):
        print 'Welcome to the Python Tic Tac Toe Game!'
        print 'Player go first, select 1-9 to make your move'


def alphaBeta(board, player, next_player, alpha, beta):
    winner = board.winner()
    if winner != 0:
        return winner
    elif not board.legal_move():
        return 0

    for move in board.squares:
        if board.board[move] == 0:
            board.board[move] = player
            val = alphaBeta(board,next_player,player,alpha,beta)
            board.board[move] = board.open_token
            if player == board.o_token:
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val< beta:
                    beta = val
                if beta <= alpha:
                    return alpha
    if player == board.o_token:
        retval = alpha
    else:
        retval = beta

    return retval

def aiMove(board):
    best = -2
    ai_moves = []
    for move in board.squares:
        if board.board[move] == 0:
            board.board[move] = board.o_token
            val = alphaBeta(board, board.x_token, board.o_token, -2,2)
            board.board[move] = 0
            if val > best:
                best = val
                ai_moves = [move]
            if val == best:
                ai_moves.append(move)

    return random.choice(ai_moves)

def playerMove(board):
    loop = True
    while loop:
        try:
            inp = input('You select: ')
            player_move = int(inp-1)
            if 0 <= player_move <=8:
                if board.board[player_move] == 0:
                    loop = False
                else:
                    print 'Occupied, select another square.'

            else:
                print 'Please enter 1-9 to pick a spot.'

        except EOFError:
            print
            sys.exit(0)

        if loop:
            board.show_board()

    return player_move

def play(board):
    player =1
    ai = 0
    next_move = player
    while board.legal_move() and board.winner()== 0:

        board.show_board()
        if next_move == player and board.legal_move():
            player_move = playerMove(board)
            board.board[player_move]= board.x_token
            next_move = ai

        if next_move == ai and board.legal_move():
            ai_move = aiMove(board)
            board.board[ai_move]= board.o_token
            next_move = player


    board.show_board()

    print ["It's a draw -_-",'Too bad, I won :)','You won :('][board.winner()]


def main():
    t = gameBoard()
    t.newGame()
    play(t)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print
        sys.exit(1)
