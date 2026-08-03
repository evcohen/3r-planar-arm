# import numpy as np
# import matplotlib.pyplot as plt


# theta1 = np.linspace(90,90,45)
# theta2 = np.linspace(-45,45,45)
# theta3 = np.linspace(-45,45,45)

# class arm:
#     def __init__(self,L1,L2,L3):
#         self.L1 = L1
#         self.L2 = L2
#         self.L3 = L3
#         self.xAll = []
#         self.yAll = []
#     def findPoints(self,theta1,theta2,theta3):
#         for thetaOne in theta1:
#             for thetaTwo in theta2:
#                 for thetaThree in theta3:
#                     x1 = self.L1 * np.cos(thetaOne)
#                     y1 = self.L1 * np.sin(thetaOne)
#                     x2 = x1 + self.L2 * np.cos(thetaOne + thetaTwo)
#                     y2 = y1 + self.L2 * np.sin(thetaOne + thetaTwo)
#                     x3 = x2 + self.L3 * np.cos(thetaOne + thetaTwo + thetaThree)
#                     y3 = y2 + self.L3 * np.sin(thetaOne + thetaTwo + thetaThree)
#                     self.xAll.append(x3)
#                     self.yAll.append(y3)
#     def plotPoints(self):
#         plt.scatter(self.xAll,self.yAll, alpha = .01, s = 1)
# sampleArm = arm(14,12,9)
# sampleArm.findPoints(np.radians(theta1),np.radians(theta2),np.radians(theta3))
# sampleArm.plotPoints()
# plt.axis("equal")
# plt.show()
import numpy as np
import matplotlib.pyplot as plt

theta1 = np.radians(np.linspace(90, 90, 90))
theta2 = np.radians(np.linspace(-45, 45, 90))
theta3 = np.radians(np.linspace(-45, 45, 90))

class Arm:
    def __init__(self, L1, L2, L3):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3

    def findPoints(self, theta1, theta2, theta3):
        t1, t2, t3 = np.meshgrid(theta1, theta2, theta3)

        x1 = self.L1 * np.cos(t1)
        y1 = self.L1 * np.sin(t1)
        x2 = x1 + self.L2 * np.cos(t1 + t2)
        y2 = y1 + self.L2 * np.sin(t1 + t2)
        self.xAll = (x2 + self.L3 * np.cos(t1 + t2 + t3)).ravel()
        self.yAll = (y2 + self.L3 * np.sin(t1 + t2 + t3)).ravel()

    def plotPoints(self):
        plt.scatter(self.xAll, self.yAll, alpha=0.01, s=1)

plt.ion()
fig, ax = plt.subplots()

while True:
    ax.cla()
    sampleArm = Arm(14, 12, 9)
    sampleArm.findPoints(theta1, theta2, theta3)
    sampleArm.plotPoints()
    ax.set_aspect("equal")
    plt.pause(0.5)