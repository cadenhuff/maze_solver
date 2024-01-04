import numpy as np 
import model 
import game
class Agent:




    def __init__(self):
        #Each agent will have one model that saves through each episode
        #In this context an episode is defined as the completion of a maze run, ie when the agent reaches the goal.
        self.model = model.Model()

        self.state = [0,1]
    


    def play_game(self):
        game = game.Game()
        
        while game.running == True:
            #Use model to determine action
            action = self.model.predict(self.state)
            #Update player in game
            game.step(action)
            #Update agents state, this is the same as the Player's position in game
            self.state = game.player
        
        
    def run_n_times(self,n):

        pass

        

        



    
        




    
        
        