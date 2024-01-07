
class Maze:

    def __init__(self):
        self.board = [[0,0,0],
                      [0,-10,-10],
                      [0,0,5]]
        
        self.player = [0,1]
        self.score = 0
        self.running = True


    def reset(self):
        pass
    def display_board(self):
        for row in self.board:
            print(row)

    def reset(self):
        self.score = 0
        self.running = True
    def step(self,action):
        print(self.player)
        self.display_board()
        self.move(action)
        self.evaluate()
        if self.player == [2,2]:
            self.running = False
            return (self.board[self.player[0]][self.player[1]])
        return (self.board[self.player[0]][self.player[1]])      
        
        
           

    def evaluate(self):
        self.score += self.board[self.player[0]][self.player[1]]

        
    def move(self,action):
        if action == "left":
            self.player[1] -= 1
        if action == "right":
            self.player[1] += 1
        if action == "up":
            self.player[0] += 1
        if action == "down":
            self.player[0] -= 1
        else:
            pass
