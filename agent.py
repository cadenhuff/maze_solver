import numpy as np 
import model 

class Agent:




    def __init__(self):
        #Each agent will have one model that saves through each episode
        #In this context an episode is defined as the completion of a maze run, ie when the agent reaches the goal.
        self.model = model.Model()

        self.state = [0,1]


    def play_game(self):


        #Use model to determine action


        #Update game with action


        #Update state

        pass


    
        




    
        
        