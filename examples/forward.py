#!/usr/bin/env python3

from visual_kinematics.RobotSerial import *
import numpy as np
from math import pi


def main():
    np.set_printoptions(precision=3, suppress=True)
    # |  d  |  a  |  alpha  |  theta  |
    if False:

        dh_params = np.array([[0.32, 0.10,pi*0.5, pi*0.5],#1 last two negative
                            [0.,0.4, 0, pi*0.5],#2
                            [0, 0, -0.5*pi, 0.],#3
                            [-0.4, 0.0, -0.5 * pi, 0],#4
                            [0.0, 0,  -0.5 * pi, 0],
                            [0.065, 0,  0,0 ]])
        theta = np.array([np.deg2rad(45.), np.deg2rad(0.), np.deg2rad(30.), np.deg2rad(45.), np.deg2rad(-45.), np.deg2rad(-45.)])
    else:

        dh_params = np.array([[0.32, 0.10,pi*0.5, pi*0.5],#1 trial
                            [0.,0.4, 0, pi*0.5],#2
                            [0, 0, -0.5*pi, 0.],#3
                            [-0.4, 0.0, 0.5 * pi, 0],#4
                            [0.0, 0,  0.5 * pi, 0],
                            [0.065, 0,  0,0 ]])
        theta = np.array([np.deg2rad(45.), np.deg2rad(0.), np.deg2rad(30.), np.deg2rad(45.), np.deg2rad(45.), np.deg2rad(45.)])


    robot = RobotSerial(dh_params)

    # =====================================
    # forward
    # =====================================

    
    # theta = np.array([np.deg2rad(0.1), np.deg2rad(0.1), np.deg2rad(0.1), np.deg2rad(0.1), np.deg2rad(-0.1), np.deg2rad(-0.1)])
    f = robot.forward(theta)

    print("-------forward-------")
    print("end frame t_4_4:")
    print(f.t_4_4)
    print("end frame xyz:")
    print(f.t_3_1.reshape([3, ]))
    print("end frame abc:")
    print(f.euler_3)
    print("end frame rotational matrix:")
    print(f.r_3_3)
    print("end frame quaternion:")
    print(f.q_4)
    print("end frame angle-axis:")
    print(f.r_3)

    robot.show()


if __name__ == "__main__":
    main()
