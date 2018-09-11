class Config():
    def __init__(self, condition):
        self.isStopped = False
        self.condition = condition

    def setModules(self, modules):
        self.modules = modules
    
