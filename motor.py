import pyrosim.pyrosim as pyrosim
import constants as c
class MOTOR:
    def __init__(self, jointName):
        self.jointName = pyrosim.jointNamesToIndices 
    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOff
