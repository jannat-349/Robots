from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data as pybullet_data
import pyrosim as pyrosim
class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        self.physicsClient = p.connect(p.GUI) 
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setGravity(0,0,-9.8)
        pyrosim.Prepare_To_Simulate(self.robot.robotId)