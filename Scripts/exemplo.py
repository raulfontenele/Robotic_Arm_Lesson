import sim
import time
import math
from testeresol import InverseKinematic


#CONSTANTS
jointArm1 = "redundantRob_joint1"
jointArm2 = "redundantRob_joint2"
jointArm3 = "redundantRob_joint3"
jointArm4 = "redundantRob_joint4"
jointArm5 = "redundantRob_joint5"
jointArm6 = "redundantRob_joint6"

link5Arm = "redundantRob_link5"

eofArm = "Rectangle4"

dummy = "Dummy"

def diffAngles(initAngle,finalAngle,orientation):
        diff = finalAngle - initAngle
        if orientation == 1:
            if diff < 0:
                diff = (360 - initAngle) + finalAngle
        else:
            if diff <= 0:
                diff*=-1
            else:
                diff = 360 - (diff)
        return diff

def diffAngleThreshold(threshold,orientation):
    angleHor = diffAngles(threshold,orientation,1)
    angleAntiHor = diffAngles(threshold,orientation,-1)
    if angleAntiHor > angleHor:
        return angleHor
    else:
        return -angleAntiHor

def getAbsolutePosition(flag,idClient,robot):
    if flag == True:
        returnCode,position = sim.simxGetObjectPosition(idClient,robot,-1,sim.simx_opmode_streaming )
    else:
        returnCode,position = sim.simxGetObjectPosition(idClient,robot,-1,sim.simx_opmode_buffer )
    return position



def SetJointOrientation(flag,idClient,robot,orientation):
    
    returnCode,position = sim.simxGetObjectPosition(idClient,robot,-1,sim.simx_opmode_oneshot )

def getAbsoluteOrientation(flag,idClient,robot):
    if flag == True:
        returnCode,eulerAngles = sim.simxGetObjectOrientation(idClient,robot,-1,sim.simx_opmode_oneshot_wait)
    else:
        returnCode,eulerAngles = sim.simxGetObjectOrientation(idClient,robot,-1,sim.simx_opmode_remove)
    
    #print("Return code of get orientation:{}".format(returnCode))
    #Com a conversão dos angulos de euler
    '''
        Os valores dos ângulos de euler variam de 0 a -2*pi entre os ângulos de 90º e -90º nos quadrantes 1 e 4
        enquanto os valores 0 a 2*pi entre os ângulos de 90º e -90º nos quadrantes 2 e 3.
        A conversão consiste em transformar em valores de 0 a 360º com 90º sendo o zero e crescendo no sentido horário
        
    '''
    return eulerAngles
    '''
    print(eulerAngles)
    for i in range(len(eulerAngles)):
        if eulerAngles[i] < 0:
            eulerAngles[i] = abs(eulerAngles[i])*180/math.pi
        else:
            eulerAngles[i] = (math.pi + abs(math.pi - eulerAngles[i]))*180/math.pi
        if eulerAngles[i] >= 360:
            eulerAngles[i] -= 360
    
    print("angulos de euler graus:{}".format(eulerAngles))
    return eulerAngles
    '''
print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections

clientID = sim.simxStart('127.0.0.1',19999,True,True,5000,5)

if clientID!=-1:
    print ('Connected to remote API server')

    # Start the simulation:
    sim.simxStartSimulation(clientID,sim.simx_opmode_oneshot_wait)

    velocity = 1
    # Get id of joint
    

    returnCode,joint1 = sim.simxGetObjectHandle(clientID,jointArm1,sim.simx_opmode_blocking)
    returnCode,joint2 = sim.simxGetObjectHandle(clientID,jointArm2,sim.simx_opmode_blocking)
    returnCode,joint3 = sim.simxGetObjectHandle(clientID,jointArm3,sim.simx_opmode_blocking)
    returnCode,joint4 = sim.simxGetObjectHandle(clientID,jointArm4,sim.simx_opmode_blocking)
    returnCode,joint5 = sim.simxGetObjectHandle(clientID,jointArm5,sim.simx_opmode_blocking)
    returnCode,joint6 = sim.simxGetObjectHandle(clientID,jointArm6,sim.simx_opmode_blocking)

    returnCode,link5 = sim.simxGetObjectHandle(clientID,link5Arm,sim.simx_opmode_blocking)

    returnCode,eofObject = sim.simxGetObjectHandle(clientID,eofArm,sim.simx_opmode_blocking)
    returnCode,dummyObject = sim.simxGetObjectHandle(clientID,dummy,sim.simx_opmode_blocking)


    initAngle = math.radians(0)
    returnCode =    sim.simxPauseCommunication(clientID,True)
    returncode =    sim.simxSetJointTargetPosition(clientID, joint1, initAngle, sim.simx_opmode_oneshot)
    returncode =    sim.simxSetJointTargetPosition(clientID, joint2, initAngle, sim.simx_opmode_oneshot)
    returncode =    sim.simxSetJointTargetPosition(clientID, joint3, initAngle, sim.simx_opmode_oneshot)
    returncode =    sim.simxSetJointTargetPosition(clientID, joint4, initAngle, sim.simx_opmode_oneshot)
    returncode =    sim.simxSetJointTargetPosition(clientID, joint5, initAngle, sim.simx_opmode_oneshot)
    returncode =    sim.simxSetJointTargetPosition(clientID, joint6, initAngle, sim.simx_opmode_oneshot)
    returnCode =    sim.simxPauseCommunication(clientID,False)

    flag = False
    ot = getAbsoluteOrientation(flag,clientID,eofObject)
    print("Value of init ot:{}".format(ot))
    time.sleep(0.1)

    flag = True
    initOrientation = getAbsoluteOrientation(flag,clientID,eofObject)
    print("Value of init orientation:{}".format(initOrientation))
    time.sleep(1)

    
    returnCode = sim.simxPauseCommunication(clientID,True)
    returncode = sim.simxSetJointTargetPosition(clientID, joint2, math.radians(30), sim.simx_opmode_oneshot)
    returncode = sim.simxSetJointTargetPosition(clientID, joint4, math.radians(40), sim.simx_opmode_oneshot)
    returnCode = sim.simxPauseCommunication(clientID,False)
    
    '''
    flag = True
    orientation = getAbsoluteOrientation(flag,clientID,eofObject)
    print("Orientation:{}".format(orientation))
    
    returncode =    sim.simxSetJointTargetPosition(clientID, joint4, math.radians(30), sim.simx_opmode_oneshot)

    orientation = getAbsoluteOrientation(flag,clientID,eofObject)
    print("Orientation:{}".format(orientation))
    '''
    #returnCode=sim.simxSetObjectOrientation(clientID,joint1,-1,[10,20,30],sim.simx_opmode_oneshot)
    #print("Código de retorno de orientação: {}".format(returnCode))
    #time.sleep(5)
    # Set joint velocity
   
    flag = True
    for value in [-60,-40,-20,0, 20, 40, 60]:
       # print("Value of the angle:{}".format(value))
        rad = value*math.pi/180
        #flag = False
        #print(rad)
        '''
        returnCode =    sim.simxPauseCommunication(clientID,True)
        returncode =    sim.simxSetJointTargetPosition(clientID, joint1, rad, sim.simx_opmode_oneshot)
        returncode =    sim.simxSetJointTargetPosition(clientID, joint2, rad, sim.simx_opmode_oneshot)
        returncode =    sim.simxSetJointTargetPosition(clientID, joint3, rad, sim.simx_opmode_oneshot)
        returnCode =    sim.simxPauseCommunication(clientID,False)
        
        if flag:
            flag = False
            returnCode,position=sim.simxGetJointPosition(clientID,joint1,sim.simx_opmode_streaming)
        else:
            returnCode,position=sim.simxGetJointPosition(clientID,joint1,sim.simx_opmode_buffer)
        '''
        
        returncode =    sim.simxSetJointTargetPosition(clientID, joint1, math.radians(value), sim.simx_opmode_oneshot)
        '''
        returncode =    sim.simxSetJointTargetPosition(clientID, joint2, math.radians(value), sim.simx_opmode_oneshot)
        time.sleep(0.1)
        orientation = getAbsoluteOrientation(flag,clientID,eofObject)
        print("Orientation:{}".format(orientation))
        

        angle = math.degrees(orientation[1])
        print("Value of angle:{}".format(angle))

        if angle > 0:
            diff = diffAngleThreshold(angle,180)
        else:
            diff = diffAngleThreshold(angle,-180)
        
        #if( abs(diff)>120 )

        #print("Necessary diff:{}".format(diff))
        #time.sleep(3)
        '''
        '''
        if(orientation[1]>0):
            diff = abs(-math.pi - orientation[1])
        else:
            diff = abs(math.pi - orientation[1])
        '''
        #if(diff > 4*math.pi/5)
        #print("Difference in radius{}".format(diff))

        #returncode =    sim.simxSetJointTargetPosition(clientID, joint6, math.radians(diff), sim.simx_opmode_oneshot)
        '''
        time.sleep(0.1)
        orientation = getAbsoluteOrientation(flag,clientID,link5)
        print("Orientation after movement:{}".format(orientation))
        time.sleep(1)
        #print("Posição:{}".format(position*180/math.pi))
        '''
        '''
        time.sleep(3)
        orientation = getAbsoluteOrientation(flag,clientID,eofObject)
        print("Orientation:{}".format(orientation))
        value = 0 - orientation[0]
        print(value)
        returncode =    sim.simxSetJointTargetPosition(clientID, joint4, value, sim.simx_opmode_oneshot)
        '''
        #returnCode = sim.simxSetObjectOrientation(clientID,joint4,-1,[math.pi/2,0,0],sim.simx_opmode_oneshot)
    #returncode = sim.simxSetJointTargetVelocity(clientID,joint1,5,sim.simx_opmode_streaming)
    #print("Código de retorno set velocidade2: {}".format(returncode))
    #time.sleep(3)

    #returncode = sim.simxSetJointTargetVelocity(clientID,joint1,0,sim.simx_opmode_streaming)
    #print("Código de retorno set velocidade para zero: {}".format(returncode))

    # Stop simulation:
    #sim.simxStopSimulation(clientID,sim.simx_opmode_oneshot_wait)

    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
    