import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import time
import constants as c

for i in range(1000):
    p.stepSimulation()
    c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = c.robotId, jointName = b"Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = c.backleg_targetAngles[i], maxForce = 50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = c.robotId, jointName = b"Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition = c.frontleg_targetAngles[i], maxForce = 50)
    time.sleep(1/240)
np.save("data/backlegSensorValues.npy", c.backleg_targetAngles)
np.save("data/frontlegSensorValues.npy", c.frontleg_targetAngles)
p.disconnect()
