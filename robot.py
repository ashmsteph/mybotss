import pybullet_data 
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time as t
class ROBOT:
    def __init__(self):
        # physicsClient = p.connect(p.GUI)
        # p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNametoIndices:
            print(linkName)
    def Sense(self):
        for i in self.sensors():
            self.sensors.Get_Value() 
    def Act():
        pass
        
            