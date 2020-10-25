import numpy as np
import pylab as plt
from scipy.integrate import odeint


C = 1.0
gNa = 120.0
gK = 36.0
gL = 0.3
ENa = 56.0
EK = -96.0
EL = -55.0


# Gating functionality (alpha and beta for each of m, h, n)
def a_m(V):
    return 0.1 * (V + 40.0) / (1.0 - np.exp(-(V + 40.0) / 10.0))


def b_m(V):
    return 4.0 * np.exp(-(V + 65.0) / 18.0)


def a_h(V):
    return 0.07 * np.exp(-(V + 65.0) / 20.0)


def b_h(V):
    return 1.0 / (1.0 + np.exp(-(V + 35.0) / 10.0))


def a_n(V):
    return 0.01 * (V + 55.0) / (1.0 - np.exp(-(V + 55.0) / 10.0))


def b_n(V):
    return 0.125 * np.exp(-(V + 65) / 80.0)


#  Sodium Current (Na)
def SodiumCurrent(V, m, h):
    return gNa * m ** 3 * h * (V - ENa)


#  Potassium current (K)
def PotassiumCurrent(V, n):
    return gK * n ** 4 * (V - EK)


#  Leak current
def LeakCurrent(V):
    return gL * (V - EL)


# Stimulus current (over a total range of 500ms)
def StimulusCurrent(t):  # step up 10 from 100 to 200 and 20 from 300 to 400
    return 10 * (t > 100) - 10 * (t > 200) + 20 * (t > 300) - 20 * (t > 400)


# The time to integrate over (for the plot)
t = np.arange(0.0, 500.0, 0.1)


#Solve the equations
def compute(X, t):
    V, m, h, n = X

    # calculate membrane potential & activation variables
    voltage = (StimulusCurrent(t) - SodiumCurrent(V, m, h) - PotassiumCurrent(V, n) - LeakCurrent(V)) / C
    mRate = a_m(V) * (1.0 - m) - b_m(V) * m
    hRate = a_h(V) * (1.0 - h) - b_h(V) * h
    nRate = a_n(V) * (1.0 - n) - b_n(V) * n
    return voltage, mRate, hRate, nRate


X = odeint(compute, [-65, 0.05, 0.6, 0.32], t)
V = X[:, 0]
m = X[:, 1]
h = X[:, 2]
n = X[:, 3]
NaCurr = SodiumCurrent(V, m, h)
KCurr = PotassiumCurrent(V, n)
LCurr = LeakCurrent(V)

plt.figure()
plt.subplot(3, 1, 1)
plt.title('Hodgkin-Huxley Model of a Neuron')
plt.plot(t, V, 'k')
plt.ylabel('V (mV)')

plt.subplot(3, 1, 2)
plt.plot(t, NaCurr, 'b', label='$Na$')
plt.plot(t, KCurr, 'r', label='$K$')
plt.plot(t, LCurr, 'g', label='$L$')
plt.ylabel('Current')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, StimulusCurrent(t), 'k')
plt.xlabel('t (ms)')
plt.ylabel('$Stim Current$')
plt.ylim(-1, 31)

plt.tight_layout()
plt.show()
