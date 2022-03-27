import pandas as pd
import json
import sys
import numpy as np

def searching_best_values (value, dataset, key):

    df_select = dataset.loc[dataset[key] == str(value)]
    df_select = df_select.reset_index()
    return df_select

print("Reading data")
dataset = pd.read_csv(sys.argv[1])
path_export = sys.argv[2]

print("Get values")
calinski_values = [float(value) for value in dataset['calinski'] if value != 'ERROR']
siluetas_values = [float(value) for value in dataset['siluetas'] if value != 'ERROR']

print("Get max values")
max_value_cal = np.max(calinski_values)
max_value_siluetas = np.max(siluetas_values)

print("Searching data")
df_siluetas = searching_best_values(max_value_siluetas, dataset, 'siluetas')
df_calinski = searching_best_values(max_value_cal, dataset, 'calinski')

df_siluetas.to_csv(path_export+"best_siluetas.csv", index=False)
df_calinski.to_csv(path_export+"best_calinski.csv", index=False)