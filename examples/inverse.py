#!/usr/bin/env python3

from visual_kinematics.RobotSerial import *
import numpy as np
from math import pi


def main():
    np.set_printoptions(precision=3, suppress=True)

    # dh_params = np.array([[0.163, 0., 0.5 * pi, 0.],
    #                       [0., 0.632, pi, 0.5 * pi],
    #                       [0., 0.6005, pi, 0.],
    #                       [0.2013, 0., -0.5 * pi, -0.5 * pi],
    #                       [0.1025, 0., 0.5 * pi, 0.],
    #                       [0.094, 0., 0., 0.]])
    dh_params = np.array([[0.32, 0.10,pi*0.5, pi*0.5],#1 trial
                        [0.,0.4, 0, pi*0.5],#2
                        [0, 0, -0.5*pi, 0.],#3
                        [-0.4, 0.0, 0.5 * pi, 0],#4
                        [0.0, 0,  0.5 * pi, 0],
                        [0.065, 0,  0,0 ]])

    robot = RobotSerial(dh_params)

    # =====================================
    # inverse
    # =====================================

    xyz = np.array([[0.38127], [0.], [0.9182]])
    abc = np.array([0.5 * pi, 0., pi])
    end = Frame.from_euler_3(abc, xyz)
    robot.inverse(end)

    print("inverse is successful: {0}".format(robot.is_reachable_inverse))
    print("axis values: \n{0}".format(robot.axis_values))
    robot.show()

    # example of unsuccessful inverse kinematics
    xyz = np.array([[2.2], [0.], [1.9]])
    end = Frame.from_euler_3(abc, xyz)
    robot.inverse(end)

    print("inverse is successful: {0}".format(robot.is_reachable_inverse))


if __name__ == "__main__":
    main()
