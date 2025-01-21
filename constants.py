import numpy as np

x = np.linspace(0, np.pi * 2, 1000)
backleg_amplitude = np.pi / 6
backleg_frequency = 5
backleg_phaseOffset = 0
frontleg_amplitude = np.pi / 2
frontleg_frequency = 5
frontleg_phaseOffset = np.pi/6
backleg_targetAngles = backleg_amplitude * np.sin(backleg_frequency * x + backleg_phaseOffset)
frontleg_targetAngles = frontleg_amplitude * np.sin(frontleg_frequency * x + frontleg_phaseOffset)
