import pybullet_data
import pybullet as p
import time as t
import pyrosim.pyrosim as pyrosim
import numpy as numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId) 
backLegSensorValues = numpy.zeros(10000)
print(backLegSensorValues)

for i in range(10000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") 
   
    t.sleep(1/60)
    print(i)
    print(backLegSensorValues)
numpy.save(data, backLegSensorValues)
p.disconnect()
# print(backLegSensorValues)