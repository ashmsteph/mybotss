import pyrosim.pyrosim as pyrosim 

height = 1
length = 1
width = 1
x = 1
y = 1
z = 1
pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name = "Box", pos = [x,y,z], size = [height, length, width])

pyrosim.End()