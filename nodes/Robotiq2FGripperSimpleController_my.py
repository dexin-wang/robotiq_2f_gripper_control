#!/usr/bin/env python

"""
subscrib topic and control gripper
"""

import roslib; roslib.load_manifest('robotiq_2f_gripper_control')
import rospy
from robotiq_2f_gripper_control.msg import _Robotiq2FGripper_robot_output  as outputMsg
from time import sleep
from std_msgs.msg import String


# def genCommand(char, command):
#     """Update the command according to the character entered by the user."""    
        
#     if char == 'a':
#         command = outputMsg.Robotiq2FGripper_robot_output();
#         command.rACT = 1
#         command.rGTO = 1
#         command.rSP  = 255
#         command.rFR  = 150

#     if char == 'r':
#         command = outputMsg.Robotiq2FGripper_robot_output();
#         command.rACT = 0

#     if char == 'c':
#         command.rPR = 255

#     if char == 'o':
#         command.rPR = 0   

#     #If the command entered is a int, assign this value to rPRA
#     try: 
#         command.rPR = int(char)
#         if command.rPR > 255:
#             command.rPR = 255
#         if command.rPR < 0:
#             command.rPR = 0
#     except ValueError:
#         pass                    
        
#     if char == 'f':
#         command.rSP += 25
#         if command.rSP > 255:
#             command.rSP = 255
            
#     if char == 'l':
#         command.rSP -= 25
#         if command.rSP < 0:
#             command.rSP = 0

            
#     if char == 'i':
#         command.rFR += 25
#         if command.rFR > 255:
#             command.rFR = 255
            
#     if char == 'd':
#         command.rFR -= 25
#         if command.rFR < 0:
#             command.rFR = 0

#     return command
        

# def askForCommand(command):
#     """Ask the user for a command to send to the gripper."""    

#     currentCommand  = 'Simple 2F Gripper Controller\n-----\nCurrent command:'
#     currentCommand += '  rACT = '  + str(command.rACT)
#     currentCommand += ', rGTO = '  + str(command.rGTO)
#     currentCommand += ', rATR = '  + str(command.rATR)
#     currentCommand += ', rPR = '   + str(command.rPR )
#     currentCommand += ', rSP = '   + str(command.rSP )
#     currentCommand += ', rFR = '   + str(command.rFR )


#     print currentCommand

#     strAskForCommand  = '-----\nAvailable commands\n\n'
#     strAskForCommand += 'r: Reset\n'
#     strAskForCommand += 'a: Activate\n'
#     strAskForCommand += 'c: Close\n'
#     strAskForCommand += 'o: Open\n'
#     strAskForCommand += '(0-255): Go to that position\n'
#     strAskForCommand += 'f: Faster\n'
#     strAskForCommand += 'l: Slower\n'
#     strAskForCommand += 'i: Increase force\n'
#     strAskForCommand += 'd: Decrease force\n'
    
#     strAskForCommand += '-->'

#     return raw_input(strAskForCommand)


def UpdateCmdCallback(msg):

    global command, updateCmd

    if msg.data == 'a':
        # print('activate robotiq')
        command = outputMsg.Robotiq2FGripper_robot_output();
        command.rACT = 1
        command.rGTO = 1
        command.rSP  = 255
        command.rFR  = 150

    if msg.data == 'r':
        command = outputMsg.Robotiq2FGripper_robot_output();
        command.rACT = 0

    if msg.data == 'c':
        command.rPR = 255

    if msg.data == 'o':
        command.rPR = 0   

    #If the command entered is a int, assign this value to rPRA
    try: 
        command.rPR = int(msg.data)
        if command.rPR > 255:
            command.rPR = 255
        if command.rPR < 0:
            command.rPR = 0
        # print('move robotiq')
    except ValueError:
        pass                    
        
    if msg.data == 'f':
        command.rSP += 25
        if command.rSP > 255:
            command.rSP = 255
            
    if msg.data == 'l':
        command.rSP -= 25
        if command.rSP < 0:
            command.rSP = 0

            
    if msg.data == 'i':
        command.rFR += 25
        if command.rFR > 255:
            command.rFR = 255
            
    if msg.data == 'd':
        command.rFR -= 25
        if command.rFR < 0:
            command.rFR = 0

    updateCmd = True



if __name__ == '__main__':
    rospy.init_node('Robotiq2FGripperSimpleController_my')
    
    pub = rospy.Publisher('Robotiq2FGripperRobotOutput', outputMsg.Robotiq2FGripper_robot_output)
    rospy.Subscriber("/robotiq/gripper_cmd", String, UpdateCmdCallback)  # update received control cmd

    command = outputMsg.Robotiq2FGripper_robot_output()
    updateCmd = False

    while not rospy.is_shutdown():
        
        if updateCmd:
            pub.publish(command)
            updateCmd = False

        rospy.sleep(0.1)
