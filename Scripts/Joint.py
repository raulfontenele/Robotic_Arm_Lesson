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
    
    def SetJointVelocity(self, velocity):
        sim.simxSetJointTargetVelocity(self.comm.clientId, self.handle, velocity, sim.simx_opmode_oneshot)
        
    def GetJointAbsoluteOrientation(self):
        returnCode,eulerAngles = sim.simxGetObjectOrientation(self.comm.clientId,self.handle,-1,sim.simx_opmode_oneshot_wait)
        return eulerAngles

    def GetJointAbsolutePosition(self):
        eturnCode,position = sim.simxGetObjectPosition(self.comm.clientId, self.handle, -1, sim.simx_opmode_oneshot_wait )
        return position

    def GetJointPosition(self):
        returnCode, position = sim.simxGetJointPosition(self.comm.clientId, self.handle, sim.simx_opmode_oneshot_wait)
        return position
    