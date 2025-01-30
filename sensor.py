import pyrosim.pyrosim as pyrosim
import time
class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = {}
    
    def Get_Value(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if i == 999:
            print(self.values[i])
        
