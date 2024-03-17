
import numpy as np
import matplotlib.pyplot


backLegSensorValues = np.load("data/file.npy")
frontLegSensorValues = np.load("record/data.npy")
print(backLegSensorValues)
print(frontLegSensorValues)
targetAngles = np.sin((0, np.pi * 2))
matplotlib.pyplot.plot(targetAngles)
matplotlib.pyplot.show()
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.show()

