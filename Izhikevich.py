import numpy as np
import matplotlib.pyplot as plt

# Simulate a neuron using the Izhikevich model.


class Izhikevich:
    def __init__(self, a=0.02, b=0.2, c=-65, d=2):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = 0.5  # step size
        self.time = np.arange(0, 1000.01, self.h)  # total time 1s
        self.v = np.zeros(len(self.time))
        self.u = np.zeros(len(self.time))

    def model(self, I=5, start=300, end=800):  # time is in MS, I is the input in mV
        # Simulate
        self.v[0] = -65
        self.u[0] = self.b * self.v[0]

        for i in range(1, len(self.time)):
            self.v[i] = self.v[i - 1] + self.h * (
                0.04 * self.v[i - 1] ** 2
                + 5 * self.v[i - 1]
                + 140
                - self.u[i - 1]
                + (I if start <= i * self.h <= end else 0)
            )
            self.u[i] = self.u[i - 1] + self.h * (
                self.a * (self.b * self.v[i - 1] - self.u[i - 1])
            )  # not sure if it is self.v[i] or self.v[i-1]
            if self.v[i] >= 30:
                self.v[i] = self.c
                self.u[i] += self.d

        # Plot
        plt.figure()
        plt.plot(self.time, self.v, "b-")
        Input = (self.time == start) | (self.time == end)
        plt.scatter(self.time[Input], self.v[Input], color="red")
        plt.xlabel("Time (ms)")
        plt.ylabel("Membrane Potential (mV)")
        plt.title(
            f"Izhikevich Single Neuron a: {self.a} b: {self.b} c: {self.c} d: {self.d}"
        )
        plt.figtext(0, 0, "Red dots are the start and end of current.")
        plt.show()


Izhikevich(0.02, 0.2, -50, 2).model()

# Chattering: 0.02, 0.2, -50,2

