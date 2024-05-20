import roboticstoolbox as rtb

import roboticstoolbox as rtb
puma = rtb.models.DH.Puma560()
traj = rtb.jtraj(puma.qz, puma.qr, 100)
traj.q.shape
rtb.qplot(traj.q)


panda = rtb.models.Panda().ets()
solver = rtb.IK_GN(pinv=True)
Tep = panda.fkine([0, -0.3, 0, -2.2, 0, 2, 0.7854])
sol = solver.solve(panda, Tep)

print(sol)

qz = [ 0., -0.3,  0., -2.2,  0., 2.,  0.78539816]
qr = [0., 0., 0., 0., 0., 0., 0.]
traj = rtb.jtraj(qz, qr, 100)
print(traj.q.shape)
rtb.qplot(traj.q)

