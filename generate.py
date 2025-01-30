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
    
Generate_Body([1.5, 0, 2])