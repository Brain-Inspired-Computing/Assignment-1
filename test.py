import numpy as np
import matplotlib.pyplot as plt
import lif_neuron as leaky

# Testing
lif_neuron = leaky.lif_neuron(resistance=500, time_step=2 , debug=True)
lif_neuron.sim(50, 2000)
lif_neuron.sim(300,1000)
lif_neuron.sim(0,1000)
lif_neuron.sim(200, 500)
lif_neuron.sim(100, 3000)
lif_neuron.sim(0, 1500)
lif_neuron.plot_activity()