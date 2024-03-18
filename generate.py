import pyrosim.pyrosim as pyrosim 

height = 1
length = 1
width = 1
x = 1
y = 1
z = 1

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name = "Box", pos = [x,y,z], size = [height, length, width])
    pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name = "BackLeg", pos = [0.5, 0, 1.0], size = [height, length, width])
    pyrosim.Send_Joint(name = "Torso_BackLeg", parent = "Torso", child = "BackLeg", 
                       type = "revolute", position = [1.5, 0, 1.5])
    pyrosim.Send_Cube(name = "Torso", pos = [1.0, 0, 1.5], size = [height, length, width])
    pyrosim.Send_Joint(name = "Torso_FrontLeg", parent = "Torso", child = "FrontLeg",
                         type = "revolute", position = [1.0, 0, 0])
    pyrosim.Send_Cube(name = "FrontLeg", pos = [1.0, 0, 0.5], size = [height, length, width])
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
    pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BeckLeg")
    # pyrosim.Send_Cube(name = "BackLeg", pos = [0.5, 0, 1.0], size = [height, length, width])
    # pyrosim.Send_Joint(name = "Torso_BackLeg", parent = "Torso", child = "BackLeg", 
    #                    type = "revolute", position = [1.5, 0, 1.5])
    # pyrosim.Send_Cube(name = "Torso", pos = [1.0, 0, 1.5], size = [height, length, width])
    # pyrosim.Send_Joint(name = "Torso_FrontLeg", parent = "Torso", child = "FrontLeg",
    #                      type = "revolute", position = [1.0, 0, 0])
    # pyrosim.Send_Cube(name = "FrontLeg", pos = [1.0, 0, 0.5], size = [height, length, width])
    pyrosim.End()

Create_World()
Generate_Body()
Generate_Brain()
# pyrosim.Send_Cube(name = "Box2", pos = [x,y,z], size = [height, length, width])

# for i in range(10):
#     pyrosim.Send_Cube(name = "Boxs", pos = [x,y,z], size = [x,y,z])
# pyrosim.End()