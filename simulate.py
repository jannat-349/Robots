# import pybullet as p
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy as np
# import random
# import time
# import constants as c
from simulation import SIMULATION

# backLegSensorValues = np.zeros(1000)
# frontLegSensorValues = np.zeros(1000)

# for i in range(1000):
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
#     pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b"Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = c.backleg_targetAngles[i], maxForce = 50)
#     pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b"Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition = c.frontleg_targetAngles[i], maxForce = 50)
#     time.sleep(1/240)
# np.save("data/backlegSensorValues.npy", c.backleg_targetAngles)
# np.save("data/frontlegSensorValues.npy", c.frontleg_targetAngles)
# p.disconnect()

simulation = SIMULATION()