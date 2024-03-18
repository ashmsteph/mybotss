from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import time as t
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        # physicsClient = p.connect(p.GUI)
        # p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.planeId = p.loadURDF("plane.urdf")
        self.robotId = p.loadURDF("body.urdf")
        p.loadSDF("world.sdf")
        pyrosim.Prepare_To_Simulate(self.robotId) 
        #prepare to Sense
        
    def Run(self):
        for i in range(10000):
            # print(i)
            p.stepSimulation()
            ROBOT.Sense
            # backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") 
            # frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") 
            pyrosim.Set_Motor_For_Joint(
              bodyIndex = self.robotId,
              jointName = b'Torso_BackLeg',
              controlMode = p.POSITION_CONTROL,
              targetPosition = random.random(),
              maxForce = 0.0)
            pyrosim.Set_Motor_For_Joint(
              bodyIndex = self.robotId,
              jointName = b'Torso_FrontLeg',
              controlMode = p.POSITION_CONTROL,
              targetPosition = random.random(),
              maxForce = 0.0)
            t.sleep(1/60)
    
        def __del__(self):
            p.disconnect()