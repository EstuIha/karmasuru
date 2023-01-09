import numpy as np
from dronekit import connect


class Connect():

    def Connect(self):
        Agent1 = connect('127.0.0.1:14550', wait_ready=True)
        Agent2 = connect('127.0.0.1:14560', wait_ready=True)
        Agent3 = connect('127.0.0.1:14570', wait_ready=True)
        Agent4 = connect('127.0.0.1:14580', wait_ready=True)
        Agent5 = connect('127.0.0.1:14590', wait_ready=True)
        Agent6 = connect('127.0.0.1:14600', wait_ready=True)
        Agent7 = connect('127.0.0.1:14610', wait_ready=True)
        Agent8 = connect('127.0.0.1:14620', wait_ready=True)
        Agent9 = connect('127.0.0.1:14630', wait_ready=True)

        Agents = [Agent1, Agent2, Agent3, Agent4, Agent5, Agent6, Agent7, Agent8, Agent9]

        pos1 = Agent1.location.local_frame
        pos2 = Agent2.location.local_frame
        pos3 = Agent3.location.local_frame
        pos4 = Agent4.location.local_frame
        pos5 = Agent5.location.local_frame
        pos6 = Agent6.location.local_frame
        pos7 = Agent7.location.local_frame
        pos8 = Agent8.location.local_frame
        pos9 = Agent9.location.local_frame

        Positions = np.array([
            [pos1[0], pos1[1], pos1[2]],
            [pos2[0], pos2[1], pos2[2]],
            [pos3[0], pos3[1], pos3[2]],
            [pos4[0], pos4[1], pos4[2]],
            [pos5[0], pos5[1], pos5[2]],
            [pos6[0], pos6[1], pos6[2]],
            [pos7[0], pos7[1], pos7[2]],
            [pos8[0], pos8[1], pos8[2]],
            [pos9[0], pos9[1], pos9[2]]
        ])
