import pyrosim.pyrosim as pyrosim
import numpy as np
import os
import random
import time

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(3, 2) 
        self.weights = self.weights * 2 - 1
        self.Set_ID(nextAvailableID)

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name = "Box", pos = [-2, -2, 0.5], size = [1, 1, 1])
        pyrosim.End()

    def Create_Body(self, startingPosition):
        pyrosim.Start_URDF("body.urdf")
        absolutePosition = startingPosition
        pyrosim.Send_Cube(name="Torso", pos=absolutePosition , size=[1, 1, 1])
        absolutePosition[0] = absolutePosition[0] - 0.5
        absolutePosition[2] = absolutePosition[2] - 0.5
        pyrosim.Send_Joint(name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = absolutePosition)
        absolutePosition[0] = absolutePosition[0] - 1.5
        absolutePosition[2] = absolutePosition[2] - 2
        pyrosim.Send_Cube(name="Frontleg", pos=absolutePosition , size=[1, 1, 1])
        absolutePosition[0] = absolutePosition[0] + 2.5
        absolutePosition[2] = absolutePosition[2] + 2
        pyrosim.Send_Joint(name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = absolutePosition)
        absolutePosition[0] = absolutePosition[0] - 1.5
        absolutePosition[2] = absolutePosition[2] - 2
        pyrosim.Send_Cube(name="Backleg", pos=absolutePosition , size=[1, 1, 1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Frontleg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Backleg")
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + 3, weight= self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGui):
        self.Create_Body([1.5, 0, 2])
        self.Create_Brain()
        self.Create_World()
        os.system("start /B python simulate.py " + directOrGui + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.1)

        f = open(fitnessFileName, "r")
        self.fitness = float (f.read())
        f.close()
        os.system("del fitness" + str(self.myID) + ".txt")
    
    def Mutate(self):
        randomRow = random.randint(0, len(self.weights)-1)
        randomCol = random.randint(0, len(self.weights[randomRow])-1)
        self.weights[randomRow][randomCol] = random.random() * 2 - 1
    