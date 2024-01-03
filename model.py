import numpy as np 


class Model:
    #Simple Q-learning model for maze solver
    


    def __init__(self):
        self.q_table = np.zeros((9,4))
        self.state_to_row = {[0,1]:0,}
        self.inaccessbile_cols = {0: [0, 3], 1: [3], 2: [1,3], 3: [0], 5: [1], 6: [0, 2], 7: [2], 8: [1, 2]}
        self.epsilon = 0.5
        self.alpha = 0
        self.R = 0
        


    def predict(self,state):
        #State is array representing position of Agent, [0,1] = spot (0,1) on board
        row_num = self.state_to_row[state]

        accessible_cols = np.array([col for col in range(self.q_table.shape[1]) if col not in self.inaccessible_cols.get(row_num, [])])
        row_x = table[x, accessible_cols]
        
        #return an action
        pass