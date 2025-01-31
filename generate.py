import pyrosim.pyrosim as pyrosim

def Generate_Body(startingPosition):
    pyrosim.Start_URDF("body.urdf")
    absolutePosition = startingPosition
    print(absolutePosition)
    pyrosim.Send_Cube(name="Torso", pos=absolutePosition , size=[1, 1, 1])
    absolutePosition[0] = absolutePosition[0] - 0.5
    absolutePosition[2] = absolutePosition[2] - 0.5
    print(absolutePosition)
    pyrosim.Send_Joint(name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = absolutePosition)
    absolutePosition[0] = absolutePosition[0] - 1.5
    absolutePosition[2] = absolutePosition[2] - 2
    print(absolutePosition)
    pyrosim.Send_Cube(name="Frontleg", pos=absolutePosition , size=[1, 1, 1])
    absolutePosition[0] = absolutePosition[0] + 2.5
    absolutePosition[2] = absolutePosition[2] + 2
    print(absolutePosition)
    pyrosim.Send_Joint(name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = absolutePosition)
    absolutePosition[0] = absolutePosition[0] - 1.5
    absolutePosition[2] = absolutePosition[2] - 2
    print(absolutePosition)
    pyrosim.Send_Cube(name="Backleg", pos=absolutePosition , size=[1, 1, 1])
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")
    pyrosim.End()
   
Generate_Body([1.5, 0, 2])
Generate_Brain()