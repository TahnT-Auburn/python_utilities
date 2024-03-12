'''
#################### Parsers Class ####################

    Author: 
        Tahn Thawainin, AU GAVLAB

    Description: 
        A class to handle parsing of various data types.
        Parsers include:
            *CSV Parser
            *YAML Parser
            {add parsers}

    Dependencies:
        <pandas>
        <pyyaml>
        <python-box>


#######################################################
'''
import pandas as pd
import yaml
import myaml
from box import Box

class Parsers:

    def __init__(self):
        '''
        Class Description:
            A class to handle parsing of various data types.
        Class Instance Input(s):
            None *class method specific*
        '''

    def csvParser(self, csv_filename):
        '''
        Description: 
            Parses cvs files and stores csv data in a python data frame.
        Input(s):
            csv_filename:   Name of csv file
                            type: <str>
        Output(s):
            csv_data: csv data frame
                        type: <pandas.DataFrame>
        '''

        #Read csv file using pandas
        csv_data = pd.read_csv(csv_filename, delimiter=',', header=0)
        
        return csv_data

    def yamlParser(self, yaml_file, myaml_conf:bool=False, box:bool=False):
        '''
        Description: 
            Parses yaml files and stores yaml data in a python dictionary.
        Input(s):
            yaml_file:  Name of yaml file 
                        type: <str>
            myaml:      Load yaml file under myaml
                        type: <bool>  
            box:        Coverts output dictionary to Box
                        type: <bool>
                 
        Output(s):
            yaml_data:  Data frame 
                        type: <dict> or <Box>
        '''

        #Open yaml file and load as dictionary
        if (myaml_conf):
            yaml_data = myaml.safe_load(yaml_file)
        else:
            with open(yaml_file, 'r') as file:
                yaml_data = yaml.safe_load(file)

        #Covert to box if specified
        if (box):
            yaml_data = Box(yaml_data)
            
        return yaml_data