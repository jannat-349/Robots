import pyrosim.pyrosim as pyrosim
import numpy as np
class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(1000)
    
    def Get_Value(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        np.save("data/SensorValues.npy", self.values)

        
