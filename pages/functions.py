import pandas as pd
import numpy as np

from data.data import data 

def zip_filler(state):
    #notify(state,"info", f'The state is {state.state_selector}')
    #notify(state,"info", f'The zip codes are {state.zip_selector}')
    notify(state,"info", f'Its entered')
    
def initialize_map(data):
    data_province = data[data['state'] == state_selector][0:1000] 
    return data_province

data_province_displayed = initialize_map(data)

def map_filler(state):
    notify(state,"info", f'The state is {state.state_selector}')
    data_state = data
    state.data_province_displayed = data_state[data_state['state'] == state.state_selector][0:1000] 


def rest_fill(state):
    notify(state,"info", f'The state inside button is {state.state_selector}')
    state.data = data[data['state'] == state.state_selector][0:1000] 
