import matplotlib.pyplot 
import numpy as numpy


backLegSensorValues = numpy.load("data/file.npy") 
print(backLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()