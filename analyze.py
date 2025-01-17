import numpy as np
import matplotlib.pyplot as plt

backlegSensorValues = np.load("data/backlegSensorValues.npy")
frontlegSensorValues = np.load("data/frontlegSensorValues.npy")
targetAngles = np.load("data/targetAngleValues.npy")
plt.plot(backlegSensorValues, label = 'Backleg', linewidth = 3)
plt.plot(frontlegSensorValues, label = 'Frontleg', linewidth = 1)
# plt.plot(targetAngles, label = 'Sine Values')
plt.legend()
plt.show()

