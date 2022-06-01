import pandas as pd
import sys

dataset = pd.read_csv(sys.argv[1])

hidrolases = dataset.loc[dataset['doc'] == 'hydrolases.csv']
hidrolases = hidrolases.reset_index()
hidrolases = hidrolases.drop(columns=['index', 'id_seq', 'doc'])

ligases = dataset.loc[dataset['doc'] == 'ligases.csv']
ligases = ligases.reset_index()
ligases = ligases.drop(columns=['index', 'id_seq', 'doc'])

hidrolases.to_csv("hydrolases_data_raw.csv", index=False)
ligases.to_csv("ligases_data_raw.csv", index=False)