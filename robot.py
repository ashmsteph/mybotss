import pybullet_data 
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time as t
from pyrosim.neuralNetwork import NEURAL_NETWORK
class ROBOT:
    def __init__(self):
        # physicsClient = p.connect(p.GUI)
        # p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNametoIndices:
            print(linkName)
    def Sense(self):
        for i in self.sensors():
            self.sensors.Get_Value() 
    def Think(self):
        self.nn.Print()
        self.nn.Update()
        print(self.nn)
    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            print(neuronName)
    
        
            