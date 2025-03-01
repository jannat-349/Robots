import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT
import time

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI) 
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setGravity(0,0,-9.8)
        self.robotId = p.loadURDF("body.urdf")
        self.planeId = p.loadURDF("plane.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(1000):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(self.robotId)
            time.sleep(1/240)
    
    def Get_Fitness(self):
        self.robot.Get_Fitness(self.robotId)
    
    def __del__(self):
        p.disconnect()
