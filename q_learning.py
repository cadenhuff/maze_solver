



class Maze:

    def __init__(self):
        self.board = [[0,0,0],
                      [0,-10,-10],
                      [0,0,5]]
        
        self.player = [0,1]
        self.score = 0


    def display_board(self):
        for row in self.board:
            print(row)


    def run_maze(self):
        print(self.player)
        self.display_board()
        self.move()

        self.evaluate()
       

        if self.player == [2,2]:
            return True, self.score
        else:
            return False, self.score

    def evaluate(self):
        self.score += self.board[self.player[0]][self.player[1]]
    def move(self):
        direction = input("enter direction: ")
        

        if direction == "left":
            self.player[1] -= 1
        if direction == "right":
            self.player[1] += 1
        if direction == "up":
            self.player[0] += 1
        if direction == "down":
            self.player[0] -= 1
        else:
            pass

if __name__ == "__main__":
    myMaze = Maze()
    while True:


        game_over, score = myMaze.run_maze()

        if game_over == True:
            break

    print(score)
