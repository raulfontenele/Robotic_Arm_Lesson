from Communication import Communication
from Joint import Joint
from Sensor import Sensor
import json
import time
import math

def Main():
    comm = Communication('127.0.0.1',19999)

    comm.Initialize()

    if comm.SucessConnect() == False:
        return

    fileJson = open("config.json")
    simulationParameters = json.load(fileJson)

    ## Inicializar os objetos a serem manipulados
    joint1 = Joint(simulationParameters['jointArm1'],comm)
    joint2 = Joint(simulationParameters['jointArm2'],comm)
    joint3 = Joint(simulationParameters['jointArm3'],comm)
    joint4 = Joint(simulationParameters['jointArm4'],comm)
    joint5 = Joint(simulationParameters['jointArm5'],comm)
    joint6 = Joint(simulationParameters['jointArm6'],comm)

    sensor = Sensor(simulationParameters['prox_sensor'],comm)

    jointAngles1 = [0,0,0,30,30,30,0,30,30,-10,-10]
    jointAngles2 = [0,60,30,30,60,30,30,40,30,30,40]
    jointAngles4 = [0,40,30,30,40,30,30,40,30,30,40]
    jointAngles6 = [0,70,30,30,70,30,30,70,30,30,70]

    ## Movimentação do braço robótico
    for index in range(11):
        comm.Pause(True)
        joint1.SetJointPosition(jointAngles1[index])
        joint2.SetJointPosition(jointAngles2[index])
        joint4.SetJointPosition(jointAngles4[index])
        joint6.SetJointPosition(jointAngles6[index])
        comm.Pause(False)

        time.sleep(1)

        ## Orientation of Joint
        orientation = joint6.GetJointAbsoluteOrientation()
        print(
        """
        // ============ Orientation  ============ // \n 
        [ 
            Name of joint: {} \n
            alpha: {}  \n
            beta: {}  \n
            gamma : {}  \n 
        ]
        """
        .format(joint6.name, orientation[0], orientation[1], orientation[2])
        )

        position = joint6.GetJointAbsolutePosition()
        print(
        """
        // ============ Position  ============ // \n 
        [ 
            Name of joint: {} \n
            x: {}  \n
            y: {}  \n
            x : {}  \n 
        ]
        """
        .format(joint6.name, position[0], position[1], position[2])
        )
    
    ## Voltar a posicição incial
    comm.Pause(True)
    joint1.SetJointPosition(0)
    joint2.SetJointPosition(0)
    joint4.SetJointPosition(0)
    joint6.SetJointPosition(0)
    comm.Pause(False)

    ## Rotacionar a junção 4 e verificar a posição do junção 6
    time.sleep(0.1)
    position = joint6.GetJointPosition()
    print("Position of joint 6 ::{} (degrees) before rotate".format( math.degrees(position) ) )

    joint4.SetJointPosition(60)
    time.sleep(0.1)
    position = joint6.GetJointPosition()
    print("Position of joint 6 ::{} (degrees)".format( math.degrees(position) ) )

    ## Leitura do sensor de distância
    distance = sensor.GetDistance()
    print("Distance readed:{}".format(distance))

    

    comm.Dispose()

Main()