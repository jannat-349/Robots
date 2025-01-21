import pybullet as p
class ROBOT:
    def __init__(self):
        self.sensors = dict()
        self.motors = dict()
        self.robotId = p.loadURDF("body.urdf")