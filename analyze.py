import numpy as np
import matplotlib.pyplot as plt

backlegSensorValues = np.load("data/backlegSensorValues.npy")
frontlegSensorValues = np.load("data/frontlegSensorValues.npy")
plt.plot(backlegSensorValues)
plt.plot(frontlegSensorValues)
plt.show()

