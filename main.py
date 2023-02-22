import pandas as pd
import numpy as np

from taipy.gui import Gui
from data.data import data 
from pages.functions import *
from pages.map import *

zipcodes = get_zipcodes()
states = get_states()

page1='''
#MAP
<|layout|columns= 2 3 3|
<|part|class_name=card|
<|{selected_zipcode}|selector|lov={zipcodes}|on_change=check_zipcode|dropdown|label=ZipCode|>
|>
<|{selected_state}|selector|lov={states}|on_change=check_state|dropdown|label=State|>
|>
'''

page = page1+map_md

gui_multi_pages = Gui(page=page)

if __name__ == '__main__':
    gui_multi_pages.run(title="Map",
                        dark_mode=False,
                        use_reloader=False,
                        port = 5000)