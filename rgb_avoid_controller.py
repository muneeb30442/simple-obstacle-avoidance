
from controller import Robot, Camera, Motor
import numpy as np

robot = Robot()
timestep = int(robot.getBasicTimeStep())

camera = robot.getDevice("rgb_camera")
camera.enable(timestep)

left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(2.0)
right_motor.setVelocity(2.0)

def detect_obstacle(image):
    image_array = np.frombuffer(image, np.uint8).reshape((480, 640, 4))
    brightness = image_array[:, :, :3].mean()
    return brightness < 100

while robot.step(timestep) != -1:
    image = camera.getImage()
    if detect_obstacle(image):
        left_motor.setVelocity(-2.0)
        right_motor.setVelocity(2.0)
    else:
        left_motor.setVelocity(2.0)
        right_motor.setVelocity(2.0)
