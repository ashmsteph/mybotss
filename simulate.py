import pybullet_data
import pybullet as p
import time as t
import pyrosim.pyrosim as pyrosim
import numpy as np

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId) 
backLegSensorValues = np.zeros(10000)
# print(backLegSensorValues)

for i in range(10000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") 
    pyrosim.Set_Motor_For_Joint(
      bodyIndex = robotId,
      jointName = b'Torso_BackLeg',
      controlMode = p.POSITION_CONTROL,
     targetPosition = 0.0,
     maxForce = 500)


    t.sleep(1/60)
    print(i)
   
# np.save("data/file.npy", backLegSensorValues)

p.disconnect()
print(backLegSensorValues)
# np.save("data/file1.npy", backLegSensorValues)