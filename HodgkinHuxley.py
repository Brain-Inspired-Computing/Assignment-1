import numpy as np
import matplotlib.pyplot as plt

# Simulates neuron using the Hodgkin Huxley model.

#Membrane Capacitance
C = 1.0

#Sodium voltage-controlled conductance
gNa = 120.0

#Potassium voltage-controlled conductance
gK = 36

#Leak channel conductance
gL = .3

#Sodium ion voltage source
ENa = 115

#Potassium ion voltage source
EK = -12

#Leak current density voltage source
EKL = 10.6

#Equations for rate variables
def a_n(Vm):
    return (0.01 * (Vm + 55)) / (1 - np.exp((-1) * ((Vm+55)/10)))


def b_n(Vm):
    return 0.125 * (np.exp((-1) * ((Vm + 65) / 80)))


def a_m(Vm):
    return (0.1 * (Vm + 40)) / (1 - np.exp((-1) * ((Vm+40)/10)))


