import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np

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
backleg_amplitude = np.pi / 6
backleg_frequency = 5
backleg_phaseOffset = 0
frontleg_amplitude = np.pi / 2
frontleg_frequency = 5
frontleg_phaseOffset = np.pi/6
backleg_targetAngles = backleg_amplitude * np.sin(backleg_frequency * x + backleg_phaseOffset)
frontleg_targetAngles = frontleg_amplitude * np.sin(frontleg_frequency * x + frontleg_phaseOffset)
