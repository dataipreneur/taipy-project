import pandas as pd
import numpy as np

from data.data import data 

def get_zipcodes():
    zip_code_data = list(np.sort(data['zip_code'].astype(str).unique()))
    return zip_code_data

def get_states():
    address = data["full_address"].str.split(",", 3, expand=True)
    data['state'] = address.loc[:,2]
    unique_states = list(address.loc[:,2].unique())
    return unique_states