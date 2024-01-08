import numpy as np
class Model:
    #Simple Q-learning model for maze solver
    


    def __init__(self):
        #Init for tester
        self.q_table = np.zeros((9,4))
        self.state_to_row = {(0,0):0,(0,1):1, (0,2): 2,(1,0):3,(1,1):4,(1,2):5,(2,0):6,(2,1):7,(2,2):8}
        self.inaccessible_cols = {0: [0, 3], 1: [3], 2: [1,3], 3: [0], 5: [1], 6: [0, 2], 7: [2], 8: [1, 2]}
        self.accessible_cols = {0: [1,2], 1: [0,1,2], 2: [0,2], 3: [1,2,3], 5: [0,2,3], 6: [1,3], 7: [0,1,3], 8: [0,3]}
        self.epsilon = 0.5
        self.alpha = 1
        self.y = 1
        

        
    def predict(self,state):
        #State is array representing position of Agent, [0,1] = spot (0,1) on board
        row_num = self.state_to_row[state]
        row = self.q_table[row_num, self.accessible_cols[row_num]]
        #For right now I'm just doing the max, but later I will implement episilon which will
        #act as the exploratory factor
        max_index = np.argmax(row)
        action_index = self.accessible_cols[row_num][max_index]


        print(action_index)
        
        #return an action
        return action_index

    def recompute(self,state,old_state,action,reward):
        #Recompute Q-table with given

        new_state_row_num = self.state_to_row[state]
        old_state_row_num = self.state_to_row[old_state]
        
        current_val_of_old_state = self.q_table[old_state_row_num][action]
        self.q_table[old_state_row_num][action] = current_val_of_old_state + (self.alpha*(reward + (self.y)*(max(self.q_table[new_state_row_num])) - current_val_of_old_state))
        print(self.q_table)
        pass


my_model = Model()


my_model.predict((0,2))
my_model.recompute((1,2),(0,2),2,-10)
my_model.recompute(())