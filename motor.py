import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
        self.motorValues

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.frequency
        x = np.linspace(0, np.pi * 2, 1000)
        self.motorValues = self.amplitude * np.sin(self.frequency * x + self.offset)

    def Set_Value(self, robotId, i):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[i], maxForce = 50)
            
