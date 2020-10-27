import numpy as np
import matplotlib.pyplot as plt
import lif_neuron as leaky

# Testing
lif_neuron = leaky.lif_neuron(resistance=500, time_step=1)
lif_neuron.sim(20, 2000)
lif_neuron.sim(100,1000)
lif_neuron.sim(0,1000)
f1 = plt.figure(1)
lif_neuron.plot_activity()
f2 = plt.figure(2)
lif_neuron.plot_rate()
plt.show()
