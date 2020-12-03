import numpy as np
import matplotlib.pyplot as plt

C  = 2e8
S0 = 1340
S2 = -0.477
alpha_ice = 0.62
alpha_noice = 0.3
T_ice = 258
T_NoIce = 288
A = 367.3
B = 2.09

def ice_edge(temperature):
    no_ice = temperature > T_NoIce
    ice =  temperature < T_ice
    middle = np.ones_like(no_ice) - no_ice - ice
    x_edge = middle * (1+((temperature - T_NoIce)/(T_NoIce-T_ice))) + ice
    return x_edge


def albedo(x_edge):
    alpha = alpha_ice + (alpha_noice - alpha_ice) * ((1-S2/2) * x_edge + S2/2 *x_edge**3)
    return alpha


def EBM(alpha, Ts):
    dT = 1/C * (S0/4 * (1-alpha) - A + B * Ts)
    return dT


def first_term(alpha):
    return S0 / 4 * (1 - alpha)


def second_term(Ts):
    return - A - B * Ts


T_earth = np.linspace(250, 300, 100)

albedo_earth = albedo(ice_edge(T_earth))
first = first_term(albedo_earth)
second = second_term(T_earth)

fig, ax = plt.subplots()

ax.plot(T_earth, first)
ax.plot(T_earth, )
fig.show()




'''
class Model:
    def __init__(self, capacity_earth, solar_constant):
        self.capacity_earth = capacity_earth
        self.solar_constant = solar_constant
        self.Ts

    @property
    def albedo(self):

        return

    @property
    def
'''