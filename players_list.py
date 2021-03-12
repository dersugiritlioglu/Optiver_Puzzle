class PlayersList:
    def __init__(self):
        self.p_values = [0,0,0,0]
        self.best = [[],[],[],[]]
        
    def change_value(self,p_id, p_value):
        self.p_values[p_id] = p_value
    
    def same_values_exist(self):
        for idx,i in enumerate(self.p_values):
            if i in self.p_values[:idx] or i in self.p_values[idx+1:]:
                return True
        return False