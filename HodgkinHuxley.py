import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Simulates neuron using the Hodgkin Huxley model.

class HodgkinHuxley():
    # Time variables for plotting graph
    T = np.arange(0.0, 1000, .01)

    # Membrane Capacitance
    C = 1.0

    # Sodium voltage-controlled conductance
    gNa = 120.0

    # Potassium voltage-controlled conductance
    gK = 36

    # Leak channel conductance
    gL = .3

    # Sodium ion voltage source
    ENa = 115

    # Potassium ion voltage source
    EK = -12

    # Leak current density voltage source
    EKL = 10.6

    # Equations for rate variables
    def a_m(self, V):
        return (0.1 * (V + 40)) / (1 - np.exp((-1) * ((V + 40) / 10)))

    def b_m(self, V):
        return 4 * np.exp((-V + 65) / 18)

    def a_n(self, V):
        return (0.01 * (V + 55)) / (1 - np.exp((-1) * ((V + 55) / 10)))

    def b_n(self, V):
        return 0.125 * (np.exp((-1) * ((V + 65) / 80)))

    def a_h(self, V):
        return 0.07 * np.exp((-1) * ((V + 65) / 20))

    def b_h(self, V):
        return 1 / (1 + ((np.exp((-1) * (V + 35))) / 10))


    def GK(self, V, n, gK):
        return gK * np.power(n, 4.0) * (V - self.EK)

    def GNA(self, V, m, h):
        return self.gNa * np.power(m, 3.0) * h - (V - self.ENa)

    def GL(self, V):
        return self.gL * (V - self.EKL)

    def inputStim(self, t):
        return 10 * (t > 200) - 10 * (t > 500) + 35 * (t > 700) - 35 * (t > 900)

    def calculate(self, Z, t0):
        V = Z
        m = Z
        n = Z
        h = Z

        # du/dt
        dudt = self.inputStim(t0)

        # dm/dt
        dmdt = (self.a_m(V) * (1 - m)) - (self.b_m(V) * m)

        # dh/dt
        dhdt = (self.a_h(V) * (1 - h)) - (self.b_h(V) * h)

        # dn/dt
        dndt = (self.a_n(V) * (1 - n)) - (self.b_n(V) * n)

        return dudt, dmdt, dhdt, dndt

    # State of Voltage and m, n, and h
    # S = np.array([0.0, infinite_m(0.0), infinite_n(0.0), infinite_h(0.0)])

    def Main(self):
        X = odeint(self.calculate, [-65, 0.05, 0.6, 0.32], self.T)
        V = X[:, 0]
        m = X[:, 1]
        h = X[:, 2]
        n = X[:, 3]

        # K conductance
        GK = (self.gK / self.C) * np.power(n, 4.0)

        # Na conductance
        GNa = (self.gNa / self.C) * np.power(m, 3.0) * h

        # Leak conductance
        GL = self.gL / self.C

        plt.figure()
        plt.subplot(4, 1, 1)
        plt.title('Hodgkin-Huxley Neuron')
        plt.plot(self.t, V, 'k')
        plt.ylabel('V (mV)')

        plt.subplot(4, 1, 2)
        plt.plot(self.t, GNa, 'c', label='$I_{Na}$')
        plt.plot(self.t, GK, 'y', label='$I_{K}$')
        plt.plot(self.t, GL, 'm', label='$I_{L}$')
        plt.ylabel('Current')
        plt.legend()

        plt.subplot(4, 1, 3)
        plt.plot(self.t, m, 'r', label='m')
        plt.plot(self.t, h, 'g', label='h')
        plt.plot(self.t, n, 'b', label='n')
        plt.ylabel('Gating Value')
        plt.legend()

        plt.subplot(4, 1, 4)
        i_inj_values = [self.I_inj(t) for t in self.t]
        plt.plot(self.t, i_inj_values, 'k')
        plt.xlabel('t (ms)')
        plt.ylabel('$I_{inj}$ ($\\mu{A}/cm^2$)')
        plt.ylim(-1, 40)

        plt.show()


if __name__ == '__main__':
    runner = HodgkinHuxley()
    runner.Main()
