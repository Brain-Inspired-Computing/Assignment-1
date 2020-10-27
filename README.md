# Assignment-1

Run LIF:  
  python test.py  
  To add a simulation segment, add a lif_neuron.sim([input current], [duration of current]) line.
  To change resistance or capacitance, use lif_neuron(capacitance=[capacitance], resistance=[resistance]).
  To change range of "rate as function of current" plot, use lif_neuron.plot_rate(max_current=[highest current to test]).
  
Run Izhikevich:  
  python Izhikevich.py  
  
Run Hodgkin-Huxley:  
  python HodgkinHuxley.py  
