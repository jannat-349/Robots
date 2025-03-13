import pyrosim.pyrosim as pyrosim
import numpy as np
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) 
        self.weights = self.weights * 2 - 1
        self.Set_ID(nextAvailableID)

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name = "Box", pos = [-2, -2, 0.5], size = [1, 1, 1])
        pyrosim.End()

    def Create_Body(self, startingPosition):
        pyrosim.Start_URDF("body.urdf")
        absolutePositionOfTorso = startingPosition
        pyrosim.Send_Cube(name="Torso", pos=absolutePositionOfTorso , size=[1, 1, 1])

        absolutePositionOfTorsoFrontleg = [0, 0.5, 1]
        pyrosim.Send_Joint(name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = absolutePositionOfTorsoFrontleg, jointAxis = "1 0 0")
        relativePositionOfFrontleg = [0, 0.5, 0]
        pyrosim.Send_Cube(name="Frontleg", pos=relativePositionOfFrontleg , size=[0.2, 1, 0.2])

        absolutePositionOfFrontlegFrontLowerleg = [0, 1, 0]
        pyrosim.Send_Joint(name = "Frontleg_FrontLowerleg" , parent= "Frontleg" , child = "FrontLowerleg" , type = "revolute", position = absolutePositionOfFrontlegFrontLowerleg, jointAxis = "0 1 0")
        relativePositionOfFrontLowerleg = [0, 0, -0.5]
        pyrosim.Send_Cube(name="FrontLowerleg", pos=relativePositionOfFrontLowerleg , size=[0.2, 0.2, 1])
        
        absolutePositionOfTorsoBackleg = [0, -0.5, 1]
        pyrosim.Send_Joint(name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = absolutePositionOfTorsoBackleg, jointAxis = "1 0 0")
        relativePositionOfBackleg = [0, -0.5, 0]
        pyrosim.Send_Cube(name="Backleg", pos=relativePositionOfBackleg , size=[0.2, 1, 0.2])

        absolutePositionOfBacklegBackLowerleg = [0, -1, 0]
        pyrosim.Send_Joint(name = "Backleg_BackLowerleg" , parent= "Backleg" , child = "BackLowerleg" , type = "revolute", position = absolutePositionOfBacklegBackLowerleg, jointAxis = "0 1 0")
        relativePositionOfBackLowerleg = [0, 0, -0.5]
        pyrosim.Send_Cube(name="BackLowerleg", pos=relativePositionOfBackLowerleg , size=[0.2, 0.2, 1])

        absolutePositionOfTorsoLeftleg = [-0.5, 0, 1]
        pyrosim.Send_Joint(name = "Torso_Leftleg" , parent= "Torso" , child = "Leftleg" , type = "revolute", position = absolutePositionOfTorsoLeftleg, jointAxis = "0 1 0")
        relativePositionOfLeftleg = [-0.5, 0, 0]
        pyrosim.Send_Cube(name="Leftleg", pos=relativePositionOfLeftleg , size=[1, 0.2, 0.2])
        
        absolutePositionOfLeftlegLeftLowerleg = [-1, 0, 0]
        pyrosim.Send_Joint(name = "Leftleg_LeftLowerleg" , parent= "Leftleg" , child = "LeftLowerleg" , type = "revolute", position = absolutePositionOfLeftlegLeftLowerleg, jointAxis = "0 1 0")
        relativePositionOfLeftLowerleg = [0, 0, -0.5]
        pyrosim.Send_Cube(name="LeftLowerleg", pos=relativePositionOfLeftLowerleg , size=[0.2, 0.2, 1])
        
        absolutePositionOfTorsoRightleg = [0.5, 0, 1]
        pyrosim.Send_Joint(name = "Torso_Rightleg" , parent= "Torso" , child = "Rightleg" , type = "revolute", position = absolutePositionOfTorsoRightleg, jointAxis = "0 1 0")
        relativePositionOfRightleg = [0.5, 0, 0]
        pyrosim.Send_Cube(name="Rightleg", pos=relativePositionOfRightleg , size=[1, 0.2, 0.2])

        absolutePositionOfRightlegRightLowerleg = [1, 0, 0]
        pyrosim.Send_Joint(name = "Rightleg_RightLowerleg" , parent= "Rightleg" , child = "RightLowerleg" , type = "revolute", position = absolutePositionOfRightlegRightLowerleg, jointAxis = "0 1 0")
        relativePositionOfRightLowerleg = [0, 0, -0.5]
        pyrosim.Send_Cube(name="RightLowerleg", pos=relativePositionOfRightLowerleg , size=[0.2, 0.2, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "Leftleg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "Rightleg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "BackLowerleg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "FrontLowerleg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerleg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLowerleg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_Frontleg")
        pyrosim.Send_Motor_Neuron( name = 11, jointName = "Torso_Leftleg")
        pyrosim.Send_Motor_Neuron( name = 12, jointName = "Torso_Rightleg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Backleg_BackLowerleg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "Frontleg_FrontLowerleg")
        pyrosim.Send_Motor_Neuron( name = 15, jointName = "Leftleg_LeftLowerleg")
        pyrosim.Send_Motor_Neuron( name = 16, jointName = "Rightleg_RightLowerleg")
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + 3, weight= self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGui):
        self.Create_Body([0, 0, 1])
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
    