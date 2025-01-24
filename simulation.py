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
        for _ in range(1000):
            p.stepSimulation()
            self.robot.Sense()
            # pyrosim.Set_Motor_For_Joint(bodyIndex = c.robotId, jointName = b"Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = c.backleg_targetAngles[i], maxForce = 50)
            # pyrosim.Set_Motor_For_Joint(bodyIndex = c.robotId, jointName = b"Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition = c.frontleg_targetAngles[i], maxForce = 50)
            time.sleep(1/240)
    
    def __del__(self):
        p.disconnect()
