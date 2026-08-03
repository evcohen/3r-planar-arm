import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
class R3arm:
    def __init__(self,L1,L2,L3):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3
        self.fig, self.ax = plt.subplots()
    def fk_func(self, theta):
        self.x1 = self.L1 * np.cos(theta[0])
        self.y1 = self.L1 * np.sin(theta[0]) 
        self.x2 = self.x1 + self.L2 * np.cos(theta[1] + theta[0])
        self.y2 = self.y1 + self.L2 * np.sin(theta[1] + theta[0])
        self.x3 = self.x2 + self.L3 * np.cos(theta[2] + theta[1] + theta[0])
        self.y3 = self.y2 + self.L3 * np.sin(theta[2] + theta[1] + theta[0])
        return np.array([self.x3,self.y3])
    def jacobian_numerical(self, theta, delta = 1e-6):
        J = np.zeros((2,3))
        for i in range(3):
            theta_change_Pos = theta.copy()
            theta_change_Neg = theta.copy()
            theta_change_Pos[i] += delta
            theta_change_Neg[i] -= delta
            x1 = self.fk_func(theta_change_Neg)
            x2 = self.fk_func(theta_change_Pos)
            J[:, i] = (x2 - x1) / (2 * delta)
        return J
    def jacobian(self, theta):
        J = np.zeros((2,3))
        J[0,0] = -(self.L1*np.sin(theta[0]) + self.L2*np.sin(theta[0] + theta[1]) + self.L3*(np.sin(theta[0] + theta[1] + theta[2])))
        J[0,1] = -(self.L2*np.sin( theta[0] + theta[1]) + self.L3*(np.sin(theta[0] + theta[1] + theta[2])))
        J[0,2] = -(self.L3*(np.sin(theta[0] + theta[1] + theta[2])))
        J[1,0] = (self.L1*np.cos(theta[0]) + self.L2*np.cos(theta[0] + theta[1]) + self.L3*(np.cos(theta[0] + theta[1] + theta[2])))
        J[1,1] = (self.L2*np.cos(theta[0] + theta[1]) + self.L3*(np.cos(theta[0] + theta[1] + theta[2])))
        J[1,2] = (self.L3*(np.cos(theta[0] + theta[1] + theta[2])))
        return J
    def display(self):
        self.ax.plot([0,self.x1],[0,self.y1], "b-", linewidth = 2)
        self.ax.plot([self.x1,self.x2],[self.y1,self.y2], "g-", linewidth = 2)
        self.ax.plot([self.x2,self.x3],[self.y2,self.y3], "r-", linewidth = 2)
        self.ax.plot([0,self.x1,self.x2,self.x3],[0,self.y1,self.y2,self.y3], "ko", markersize = 8)
    def update(self,val):
        self.ax.cla()
        L_tot = self.L1 + self.L2 + self.L3
        theta1 = np.radians(theta1.val)
        theta2 = np.radians(theta2.val)
        theta3 = np.radians(theta3.val)
        self.fk_func(theta1,theta2,theta3)
        self.display()
        self.ax.set_xlim(-L_tot,L_tot)
        self.ax.set_ylim(-L_tot,L_tot)
        self.ax.set_aspect("equal")
        self.ax.grid("true")
        self.fig.canvas.draw_idle()

