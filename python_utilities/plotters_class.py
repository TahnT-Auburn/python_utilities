'''
#################### Plotters Class ####################

    Author: 
        Tahn Thawainin, AU GAVLAB

    Description: 
        A class to handle plotting data and figures.
        PLotters include:
            * Matplotlib
            {add plotters}

    Dependencies:
        * matplotlib
        * numpy
        {add dependencies}
        
########################################################
'''

import matplotlib.pyplot as plt
import numpy as np

class Plotters:

    def __init__(self):
        """
        Class Description:
            A class to handle plotting data and figures.
        Class Instance Input(s):
            None
        """

    def matPlot(self, sig_count:str='single', **kwargs):
        """
        `Description`:
            Plotting one or more singals on a single figure with MatPlotLib Library
        ------------
        `Input(s)`:

            sig_count: Count of signal(s). 
                          type: <str>
                          Formats include:
                          * single (default): Plots a single signal on a figure
                          * multi: Plots multiple signals on the same figure

            `**kwargs`:
            signals(s): Signal(s) for plotting
                       type: <list>
                       NOTE: single format: signal = list[x,y]
                             multi format: signals = list[list[x,y], ..., list[x,y]]
            [optional] label(s): Lable(s) for figure
                        type: <list>
                        NOTE: label format = list['title','xlabel','ylabel']
            [optional] limits: limits for axes
                        type: <dict>
                        NOTE: limits format = dict{'xlim': [x_min,x_max], 'ylim': [y_min,y_max]}
            [optional] legend: Legend
                        type: <list>
                        NOTE: legend format: list['signal1', ..., 'singal2']
        ------------
        `Ouput(s)`:
            None
        """
        #Parse inputs
        inp_sig = False
        inp_lab = False
        inp_lim = False
        inp_leg = False

        for key in kwargs.keys():

            if (key == 'signals'):
                inp_sig = True
                signals = kwargs['signals']
                assert type(signals) == list,\
                    f"Input <signal> has invalid type. Expected <list> but recieved <{type(signals)}"
                
            if (key == 'label'):
                inp_lab = True
                label = kwargs['label']
                assert type(label) == list,\
                    f"Input <label> has invalid type. Expected <list> but recieved <{type(label)}>"
                
            if (key == 'limits'):
                inp_lim = True
                limits = kwargs['limits']
                assert type(limits) == dict,\
                    f"Input <limits> has invalid type. Expected <list> but recieved <{type(label)}>"
                
            if (key == 'legend'):
                inp_leg = True
                legend = kwargs['legend']
                assert type(legend) == list,\
                    f"Input <legend> has invalid type. Expected <list> but recieved <{type(legend)}>"
            
        assert inp_sig == True,\
            f"No input signal detected for plotting."
        
        #Generate figure
        if (sig_count == 'single'):                 #Single signal
            if (len(signals) == 1):
                plt.plot(signals[0])
            else:
                plt.plot(signals[0],signals[1])     #Multi singals
        elif (sig_count == 'multi'):
            for signal in signals:
                if (len(signal) == 1):
                    plt.plot(signal[0])
                else:
                    plt.plot(signal[0],signal[1])
        
        #Generate labels
        if (inp_lab):
            plt.title(label[0])
            plt.xlabel(label[1])
            plt.ylabel(label[2])
        
        #Generate limits
        if (inp_lim):
            for lim_key in limits.keys():
                if (lim_key == 'xlim'):
                    plt.xlim(limits["xlim"])
                if (lim_key == 'ylim'):
                    plt.ylim(limits["ylim"])

        #Generate legend
        if (inp_leg):
            plt.legend(legend, loc="best")

        plt.tight_layout()
        plt.grid()
        plt.show()
        