import sim
import math

class Sensor:
    def __init__(self,name,communication):
        self.name = name
        self.comm = communication
        self.handle = self.GetHandleObject()
        
    def GetHandleObject(self):
        returnCode,joint = sim.simxGetObjectHandle(self.comm.clientId, self.name, sim.simx_opmode_blocking)
        return joint

    def GetDistance(self):
        returnCode, detectionState, detectedPoint, detectedObjectHandle, detectedSurfaceNormalVector = sim.simxReadProximitySensor(
            self.comm.clientId, self.handle, sim.simx_opmode_streaming)
        return detectedSurfaceNormalVector