import pybullet as p
import pyrosim as pyrosim
class WORLD:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI) 
        self.planeId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.planeId)
