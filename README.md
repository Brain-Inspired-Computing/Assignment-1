# Assignment-1

## Run LIF:  

  python test.py  
  
  - To add a simulation segment, add a lif_neuron.sim([input current], [duration of current]) line.
  - To change resistance or capacitance, use lif_neuron(capacitance=[capacitance], resistance=[resistance]).
  - To change range of "rate as function of current" plot, use lif_neuron.plot_rate(max_current=[highest current to test]).
  
## Run Izhikevich:  

  python Izhikevich.py  
  
  - to change a,b,c, or d values use the Izhikevich constructor the default values are for the regular spiking behavior
  - the model function takes in I, start, end as optional parameters that represents the magnitude of the input current, the start of the current, and the end of the current respectively. The default values for this method are I = 5, start = 300, and end = 800.
  
## Run Hodgkin-Huxley: 

  python HodgkinHuxley.py  
