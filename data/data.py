import pandas as pd


path_to_data = "data/restaurants.csv"
data = pd.read_csv(path_to_data, low_memory=False)