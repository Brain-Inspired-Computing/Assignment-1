import numpy as np
import matplotlib.pyplot as plt

# Simulate a neuron using the Izhikevich model.


class Izhikevich:
    def __init__(self, a=0.02, b=0.2, c=-65, d=2):
        """
        Initialize the Izhikevich model

        by changing a,b,c,d you can get different spiking behavior

        reference the paper of this model: https://courses.cs.washington.edu/courses/cse528/07sp/izhi1.pdf for a,b,c,d parameters
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = 0.5  # step size

    def model(self, I=5, start=300, end=800):  # time is in MS, I is the input in mV
        """
        Run the model

        I : input current magnitude
        start : start time of current
        end : end time of current
        """
        if start > end:
            print("Start time must be before end time")
            return
        # Simulate
        self.time = np.arange(0, max(1000, end) + 0.01, self.h)  # total time 1s
        self.v = np.zeros(len(self.time))  # array to hold v
        self.u = np.zeros(len(self.time))  # array to hold u
        self.v[0] = -65  # set the initial value of v
        self.u[0] = self.b * self.v[0]  # set the initial value of u

        for i in range(1, len(self.time)):  # simuluate time
            self.v[i] = self.v[i - 1] + self.h * (
                0.04 * self.v[i - 1] ** 2
                + 5 * self.v[i - 1]
                + 140
                - self.u[i - 1]
                + (I if start <= i * self.h <= end else 0)
            )  # solving for v_i
            self.u[i] = self.u[i - 1] + self.h * (
                self.a * (self.b * self.v[i - 1] - self.u[i - 1])
            )  # solving for u_i
            if self.v[i] >= 30:  # checking if there is a spike
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


Izhikevich().model()

# Chattering:
# Izhikevich(0.02, 0.2, -50,2).model()

