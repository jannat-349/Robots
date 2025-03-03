import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import os

class ROBOT:
    def __init__(self, solutionID):
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system("del brain" + str(solutionID) + ".nndf")
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, i):
        for sensor in self.sensors.values():
            sensor.Get_Value(i)  
   
    def Think(self):
        self.nn.Update()

    def Act(self, robotId):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode()
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(robotId, desiredAngle)  

    def Get_Fitness(self, robotId, solutionID):
        stateOfLinkZero = p.getLinkState(robotId, 0) 
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("tmp" + str(solutionID)  + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system("rename tmp" + str(solutionID) + ".txt fitness" + str(solutionID) + ".txt")
            



