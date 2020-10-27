import numpy as np
import pylab as plt
from scipy.integrate import odeint

# Membrane Conductance
C = 1.0

# Sodium Conductance
gNa = 120.0

# Potassium Conductance
gK = 36.0

# Leak Conductance (Chloride and other small-impact ions)
gL = 0.3

# Equilibrium Potentials
ENa = 60.0
EK = -88.0
EL = -61.0


# The individual ionic currents can be calculated as such:

#  Sodium Current (Na)
def SodiumCurrent(V, m, h):
    return gNa * (np.power(m, 3)) * h * (V - ENa)


#  Potassium current (K)
def PotassiumCurrent(V, n):
    return gK * (np.power(n, 4)) * (V - EK)


#  Leak current
def LeakCurrent(V):
    return gL * (V - EL)


# Gating functionality (alpha and beta for each of m, n, h)
def a_m(V):
    return 0.1 * (V + 40.0) / (1.0 - np.exp(-(V + 40.0) / 10.0))


def b_m(V):
    return 4.0 * np.exp(-(V + 65.0) / 18.0)


def a_n(V):
    return 0.01 * (V + 55.0) / (1.0 - np.exp(-(V + 55.0) / 10.0))


def b_n(V):
    return 0.125 * np.exp(-(V + 65) / 80.0)


def a_h(V):
    return 0.07 * np.exp(-(V + 65.0) / 20.0)


def b_h(V):
    return 1.0 / (1.0 + np.exp(-(V + 35.0) / 10.0))


# The time to integrate over (for the plot and current input)
t = np.arange(0.0, 1000, .5)


# Stimulus current to produce spikes
def StimulusCurrent(t):
    return 10 * (t > 100) - 10 * (t > 200) + 20 * (t > 400) - 20 * (t > 500) + 30 * (t > 700) - 30 * (t > 800)


# Solve the equations
def compute(X, t):
    V, m, h, n = X

    # Equations for action potential
    voltage = (StimulusCurrent(t) - SodiumCurrent(V, m, h) - PotassiumCurrent(V, n) - LeakCurrent(V)) / C

    # Equations for the rate variables
    mRate = a_m(V) * (1.0 - m) - b_m(V) * m
    hRate = a_h(V) * (1.0 - h) - b_h(V) * h
    nRate = a_n(V) * (1.0 - n) - b_n(V) * n

    return voltage, mRate, hRate, nRate


q = [-65, .05, .6, .32]
X = odeint(compute, q, t)
# Store sliced array parts into V, m, h, n after calculating derivatives
V = X[:, 0]
m = X[:, 1]
h = X[:, 2]
n = X[:, 3]

# Plot everything
plt.figure()
plt.title('Hodgkin-Huxley Model of a Neuron')

plt.subplot(2, 1, 1)
plt.plot(t, V, 'k')
plt.ylabel('Membrane Potential (mV)')
plt.xlabel('t (ms)')

plt.subplot(2, 1, 2)
plt.plot(t, StimulusCurrent(t), 'k')
plt.xlabel('t (ms)')
plt.ylabel('$Stimulus Current$')

plt.tight_layout()
plt.show()
