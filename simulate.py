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
backleg_amplitude = np.pi / 4
backleg_frequency = 10
backleg_phaseOffset = 0
frontleg_amplitude = np.pi / 4
frontleg_frequency = 10
frontleg_phaseOffset = np.pi
backleg_targetAngles = backleg_amplitude * np.sin(backleg_frequency * x + backleg_phaseOffset)
frontleg_targetAngles = frontleg_amplitude * np.sin(frontleg_frequency * x + frontleg_phaseOffset)

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b"Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = backleg_targetAngles[i], maxForce = 50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b"Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition = frontleg_targetAngles[i], maxForce = 50)
    time.sleep(1/240)
np.save("data/backlegSensorValues.npy", backleg_targetAngles)
np.save("data/frontlegSensorValues.npy", frontleg_targetAngles)
p.disconnect()
