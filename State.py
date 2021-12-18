class State:
    
    def __init__(self,value,parent,action):
        self.value = value
        self.parent = parent
        self.childs = []
        self.action = action
        self.explored = False
        self.visited = False
        
    def __str__(self):
        return "value = " + str(self.value) + " | explored = " + str(self.explored)