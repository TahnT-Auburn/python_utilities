#%% 
from python_utilities.parsers_class import *
from python_utilities.plotters_class import *

if __name__ == '__main__':

    #-----CSV Parser-----
    csv_file = 'data/example_data.csv'
    data_frame = Parsers().csvParser(csv_file)
    
    #-----YAML Parser-----
    yaml_file = 'data/ex_myaml.yaml'
    yaml_dict = Parsers().yamlParser(yaml_file,myaml_conf=True,box=True)

    #-----Matplotlib Plotter-----
    x = [1,2,3,4]
    y = [4,5,6,7]
    y2 = [7,6,5,4]
    signal = [x,y]
    signal2 = [x,y2]
    signals = [signal, signal2]
    label = ['Plotting Test','x', 'y']
    legend = ['signal1','signal2']
    limits = {'xlim':[0,5],'ylim':[0,10]}
    Plotters().matPlot(sig_count='multi',signals=signals,label=label,legend=legend,limits=limits)