import numpy as np 


class Model:
    #Simple Q-learning model for maze solver
    


    def __init__(self):
        self.q_table = np.zeros((9,3))
        self.epsilon = 0.5
        self.alpha = 0
        self.R = 0
        


    def predict(state):
        
        
        #return an action
        pass