import pyrosim.pyrosim as pyrosim
import time
class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = dict()
    
    def Get_Value(self):
        timeStamp = time.time()
        self.values[timeStamp] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
