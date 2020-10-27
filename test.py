import numpy as np
import matplotlib.pyplot as plt
import lif_neuron as leaky

# Testing
lif_neuron = leaky.lif_neuron(resistance=500, time_step=1)
lif_neuron.sim(50, 2000)
lif_neuron.sim(300,1000)
lif_neuron.sim(0,1000)
lif_neuron.sim(200, 500)
lif_neuron.sim(100, 3000)
lif_neuron.sim(0, 1500)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5))
ax1 = lif_neuron.plot_activity()
ax2 = lif_neuron.plot_rate()
