import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool


class ZeroClimateModel:
    """
    Zero dimensional climate model
    """
    def __init__(self):
        self.C = 2e8
        self.S0 = 1340
        self.S2 = -0.477
        self.alpha_ice = 0.62
        self.alpha_noice = 0.3
        self.temp_ice = 258
        self.temp_noice = 288
        self.A = -367.3
        self.B = 2.09

    def ice_edge(self, temperature):
        temperature = np.array(temperature)

        ice = temperature > self.temp_noice
        no_ice = temperature < self.temp_ice
        middle = np.ones_like(no_ice) - no_ice.astype(float) - ice.astype(float)

        x_edge = middle * (1 + ((temperature - self.temp_noice) / (self.temp_noice - self.temp_ice))) + ice.astype(float)
        return x_edge

    def albedo(self, x_edge):
        alpha = self.alpha_ice + (self.alpha_noice - self.alpha_ice) * ((1 - self.S2 / 2) * x_edge + self.S2 / 2 * x_edge ** 3)
        return alpha

    def step(self, temperature):
        x_edge = self.ice_edge(temperature)
        alpha = self.albedo(x_edge)
        temp_derivative = 1/self.C * (self.S0/4 * (1-alpha) - (self.A + self.B * temperature))
        return temp_derivative

    def first_term(self, temperature):
        x_edge = self.ice_edge(temperature)
        alpha = self.albedo(x_edge)
        return self.S0 / 4 * (1 - alpha)

    def second_term(self, temperature):
        return self.A + self.B * temperature







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