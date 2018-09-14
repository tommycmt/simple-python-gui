import threading
import logging
import os
from datetime import datetime

class Config():
    def __init__(self):
        self.isStopped = False
        self.condition = threading.Condition()
        currentPath = __file__.rsplit(os.sep,1)[0]
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)50s %(levelname)-8s %(message)s',
                            filename=currentPath+'/log/'+datetime.now().strftime('%m%d-%H%M%S')+'.log')
        
    def setModules(self, modules):
        self.modules = modules
    
