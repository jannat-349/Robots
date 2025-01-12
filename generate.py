import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("tower.sdf")

pos_x = pos_y = -1
pos_z = 0.5
a = 1
rows = cols = 5

for row in range(rows):
    for col in range(cols):
        for level in range(10):
            pyrosim.Send_Cube(name="Box", pos=[pos_x,pos_y,pos_z] , size=[a, a, a])
            a = a * 0.9
            pos_z = pos_z + 1.5
        pos_y = pos_y + 2
        a = 1
        pos_z = 0.5
    pos_x = pos_x + 2
    pos_y = -1
    pos_z = 0.5
    a = 1
    
pyrosim.End()