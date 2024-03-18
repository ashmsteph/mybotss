import numpy as np
import pyrosim.pyrosim as pyrosim
class SENSOR:
    def __init__(self,linkName,values):
        self.sensors[self.linkName] = SENSOR(self.linkName)
        self.values = np.zeros(10000)
    def Get_Value():
        backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")    
        