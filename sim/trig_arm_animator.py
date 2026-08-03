import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
fig, ax = plt.subplots()
plt.subplots_adjust(bottom = .5)
theta1A = fig.add_axes([.2,.1,.6,.075])
theta2A = fig.add_axes([.2,.25,.6,.075])
theta3A = fig.add_axes([.2,.4,.6,.075])
armPlot = ax.plot([0],[0])

class arm:
    def __init__(self,L1,L2,L3):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3
    def forward_Kinematics(self, theta1, theta2, theta3):
        self.x1 = self.L1 * np.cos(theta1)
        self.y1 = self.L1 * np.sin(theta1) 
        self.x2 = self.x1 + self.L2 * np.cos(theta2 + theta1)
        self.y2 = self.y1 + self.L2 * np.sin(theta2 + theta1)
        self.x3 = self.x2 + self.L3 * np.cos(theta3 + theta2 + theta1)
        self.y3 = self.y2 + self.L3 * np.sin(theta3 + theta2 + theta1)
    def display(self):
        ax.plot([0,self.x1],[0,self.y1], "b-", linewidth = 2)
        ax.plot([self.x1,self.x2],[self.y1,self.y2], "g-", linewidth = 2)
        ax.plot([self.x2,self.x3],[self.y2,self.y3], "r-", linewidth = 2)
        ax.plot([0,self.x1,self.x2,self.x3],[0,self.y1,self.y2,self.y3], "ko", markersize = 8)
    def update(self,val):
        ax.cla()
        L_tot = self.L1 + self.L2 + self.L3
        theta1 = np.radians(theta1S.val)
        theta2 = np.radians(theta2S.val)
        theta3 = np.radians(theta3S.val)
        firstArm.forward_Kinematics(theta1,theta2,theta3)
        firstArm.display()
        ax.set_xlim(-L_tot,L_tot)
        ax.set_ylim(-L_tot,L_tot)
        ax.set_aspect("equal")
        ax.grid("true")
        fig.canvas.draw_idle()
firstArm = arm(140,110,90)
theta1S = Slider(theta1A, "theta1",30,150,valinit=0)
theta2S = Slider(theta2A, "theta2",-90,90,valinit=0)
theta3S = Slider(theta3A, "theta3",-90,135,valinit=0)
theta1S.on_changed(firstArm.update)
theta2S.on_changed(firstArm.update)
theta3S.on_changed(firstArm.update)  
firstArm.update(None)
plt.show()
        