import pybullet_data
import pybullet as p
import time as t
import pyrosim.pyrosim as pyrosim
import numpy as np
import random


BLamplitude = 1/4
BLfrequency = 1
BLphaseOffset = 0

FLamplitude = 1/4
FLfrequency = 1
FLphaseOffset = 0
targetAngles = np.sin((0, np.pi * 2))

BLtargetAngles = np.sin(BLfrequency*targetAngles + BLphaseOffset) * BLamplitude
FLtargetAngles = np.sin(FLfrequency*targetAngles + FLphaseOffset) * FLamplitude

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId) 
backLegSensorValues = np.zeros(10000)
frontlegSensorValues = np.zeros(10000)
print(backLegSensorValues)


for i in range(10000):
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") 
    frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") 
    pyrosim.Set_Motor_For_Joint(
      bodyIndex = robotId,
      jointName = b'Torso_BackLeg',
      controlMode = p.POSITION_CONTROL,
      targetPosition = random.random(),
      maxForce = 0.0)
    pyrosim.Set_Motor_For_Joint(
      bodyIndex = robotId,
      jointName = b'Torso_FrontLeg',
      controlMode = p.POSITION_CONTROL,
      targetPosition = random.random(),
      maxForce = 0.0)
    t.sleep(1/60)
    print(backLegTouch)
    print(frontLegTouch)

np.save("data/file.npy", backLegSensorValues)
p.disconnect()
np.save("record/data.npy", backLegSensorValues)