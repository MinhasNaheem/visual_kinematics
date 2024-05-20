from roboticstoolbox.robot.DHRobot import DHRobot
from roboticstoolbox.robot.DHLink import RevoluteDH
import roboticstoolbox as rtb
from math import pi

class EpsonC4L(DHRobot):

    def __init__(self):
        super().__init__(
                [
                    RevoluteDH(d = 0.32,a =0.10,alpha = pi*0.5,offset = pi*0.5),
                    RevoluteDH(d = 0.,a=0.4,alpha =  0, offset = pi*0.5),
                    RevoluteDH(d=0, a=0, alpha = -0.5*pi, offset = 0),
                    RevoluteDH(d = -0.4, a = 0.0,alpha = 0.5 * pi, offset =  0),
                    RevoluteDH(d = 0.0,a = 0, alpha =  0.5 * pi,offset =  0),
                    RevoluteDH(d = 0.065,a = 0,alpha = 0,offset = 0)
                    
                
                ], name="EpsonC4L"
                        )
        
if __name__ == "__main__":
    rob = EpsonC4L()
    print(rob)
    rob.fkine([0, 0, 0, 0, 0, 0])
    solver = rtb.IK_GN(pinv=True)
    Tep = rob.fkine([pi/4, pi/4, pi/4, pi/4, pi/4, pi/4])
    sol = rob.ikine_LM(Tep) 
    sol1 = rob.ikine_6s( Tep, config = 'lun')
    print(sol)
    rob.plot(sol.q)
