"""
Class to simulate a a neuron with the leaky integrate-and-fire model.

by Peter Tilton
"""

import numpy as np
import matplotlib.pyplot as plt

# Leaky integrate and fire model
class lif_neuron:
    def __init__(self, capacitance=10000, resistance=1, time_step=1, debug=False):
        self.debug = debug

        # Properties
        self.capacitance = capacitance # Capacitance in miliVolts
        self.resistance = resistance # Resistance in kiloOhms
        self.time_step = time_step # Time between integrations in miliseconds

        # Activity tracking
        # Each array index corresponds to one time step
        self.input = np.array([0])
        self.potential = np.array([0])
        self.output = np.array([0])

    # Function simulates the neuron for a given time in miliseconds and input voltage in milivolts
    def sim(self, voltage, time):
        # Scaling variables
        n_steps = int(time/self.time_step)

        # Extending the tracking arrays
        self.input.resize(len(self.input) + n_steps)
        self.potential.resize(len(self.potential) + n_steps)
        self.output.resize(len(self.output) + n_steps)

        # Adding to activity tracking arrays
        for i in range(len(self.output)-n_steps, len(self.output)):
            self.input[i] = voltage # Adding input voltage to neuron sim
            if(self.debug): print("Input is " + str(self.input[i]) + " mV at " + str(i) + " ms.")

            # Simulating the next time step
            new_output = 0 # Default to no new spike
            new_potential = self.potential[i-1]
            new_potential += voltage/self.time_step
            new_potential = new_potential - max(0, self.potential[i-1]/(self.resistance/self.time_step)) # Accounting for leak
            if (new_potential > self.capacitance):
                new_potential = 0
                new_output = 1 # Spike time!
                if(self.debug): print("Spike at " + str(i) + " ms.")

            self.potential[i] = new_potential # Adding new potential to neuron sim
            self.output[i] = new_output # Adding spike to neuron sim
            if(self.debug): print("Potential is " + str(self.potential[i]) + " at " + str(i) + " ms.")
        return 0

    def plot_activity(self):
        #fig = plt.figure()
        ax = plt.axes()
        
        x = np.linspace(0, self.time_step, len(self.input))
        ax.plot(x, self.input/max(self.input)/2, linestyle="--", label="Input Voltage")
        ax.plot(x, self.potential/max(self.potential), label="Membrane Potential")
        ax.plot(x, self.output/max(self.output), linewidth = 3, label="Spike Activity")
        ax.legend()
        ax.set(
            xlabel='time (s)', ylabel='value',
            title="LIF Neuron Simulation"
        )
        plt.show()
        return 0