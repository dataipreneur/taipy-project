import pandas as pd
import numpy as np

from taipy.gui import Gui
from data.data import data 
from pages.functions import *
from pages.map import *

data = data.dropna()

data['state'] = [ x.split(', ')[-2] for x in data['full_address']]


zip_code_data = list(data['zip_code'].unique())
zip_selector = '35207'

state_data = list(data['state'].unique())
state_selector = 'AL'

text_map = ['full_address','name','zip_code']
marker_map = {"showscale":True, "colorscale":"Viridis"}
layout_map = {
            "dragmode": "zoom",
            "mapbox": { "style": "open-street-map", "center": { "lat": 38, "lon": -90 }, "zoom": 3}
            }
options = {"unselected":{"marker":{"opacity":0.5}}}

page1='''

<center> <h2>TAIPY RESTO</h2> </center>

<|layout|1 1|

<|
##State
<|{state_selector}|selector|lov={state_data}|dropdown|on_change=map_filler|>

<|Submit|button|on_action=rest_fill|>
|>

<|
##Zip
<|{zip_selector}|selector|lov={zip_code_data}|dropdown|on_action=zip_2|filter|>
|>

|>

<|layout|1 1|
<|
##Map
<|{data_province_displayed}|chart|type=scattermapbox|lat=lat|lon=lng|height=500px|width=800px|options={options}|layout={layout_map}|mode=markers|text={text_map}|hovertext=state|>
|>

<|
##Restaurant List
<|{data}|table|columns=name;zip_code;state|page_size=10|page_size_options=10;30;100|not allow_all_rows|show_all=No|auto_loading=False|width=40vw|height=100vw|>
|>

|>

'''

pages = Gui(page=page1)

if __name__ == '__main__':
    pages.run(title="Map",
                        dark_mode=True,
                        use_reloader=False)
