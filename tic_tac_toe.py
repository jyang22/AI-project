import copy

class TicTacToe:
    def __init__(self):
        self.table = [[" " for _ in xrange(3)] for _ in xrange(3)]
        self.printTable()


    def play(self, i, j):
        self.table[i][j] = "1"
        self.printTable()
        if self.checkWin():
            print "You win"
            return
        self.AIplay()
        if self.checkWin():
            print "I win"
            return


    def AIplay(self):
        table = copy.deepcopy(self.table)
        i, j = self.(table)
        self.table[i][j] = "2"


    def dfs(self, ):



    def checkWin(self):
        if self.table[0][0] == self.table[0][1] == self.table[0][2]:
            return True

        if self.table[1][0] == self.table[1][1] == self.table[1][2]:
            return True

        if self.table[2][0] == self.table[2][1] == self.table[2][2]:
            return True

        if self.table[0][0] == self.table[1][0] == self.table[2][0]:
            return True

        if self.table[1][1] == self.table[1][1] == self.table[2][1]:
            return True

        if self.table[0][2] == self.table[1][2] == self.table[2][2]:
            return True

        if self.table[0][0] == self.table[1][1] == self.table[2][2]:
            return True

        if self.table[0][2] == self.table[1][1] == self.table[2][0]:
            return True


    def printTable(self):
        print self.table[0]
        print self.table[1]
        print self.table[2]
        print "---------------"

t = TicTacToe()
t.play(1,1)