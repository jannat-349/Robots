import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import time

physicsClient = p.connect(p.GUI) 
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setGravity(0,0,-9.8)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
x = np.linspace(0, np.pi * 2, 1000)
targetAngles = np.sin(x)

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b"Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = random.uniform(-np.pi/2.0, np.pi/2.0), maxForce = 50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b"Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition = random.uniform(-np.pi/2.0, np.pi/2.0), maxForce = 50)
    time.sleep(1/60)
np.save("data/backlegSensorValues.npy", backLegSensorValues)
np.save("data/frontlegSensorValues.npy", frontLegSensorValues)
np.save("data/targetAngleValues.npy", targetAngles)
p.disconnect()
