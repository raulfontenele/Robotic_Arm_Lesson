import sim
import math

class Joint:
    def __init__(self,name,communication):
        self.name = name
        self.comm = communication
        self.handle = self.GetHandleObject()
        
    def GetHandleObject(self):
        returnCode,joint = sim.simxGetObjectHandle(self.comm.clientId, self.name, sim.simx_opmode_blocking)
        return joint

    def SetJointPosition(self, position):
        sim.simxSetJointTargetPosition(self.comm.clientId, self.handle, math.radians(position), sim.simx_opmode_oneshot)
    