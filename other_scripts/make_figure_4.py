import pandas as pd
import sys
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

def estimated_average_curve(data_values):

    array_data = [np.mean(data_values[key]) for key in data_values.columns if "p_" in key]
    return array_data

path_input = sys.argv[1]

fig = make_subplots(rows=2, cols=4, subplot_titles=("Alpha structure", "Beta structure", "Hydrophobicity", "Volume", "Energy", "Hydropathy", "Secondary structure", "Other indexes"))
row_v = 1
col_v = 1

for i in range(8):
    print("Processing index: ", i)
    data_encoding = pd.read_csv(path_input+"Group_{}_fft_encoding_v2.csv".format(i))
    data_domain = pd.read_csv(path_input+"Group_{}_fft_domain_v2.csv".format(i))
    unique_class = data_encoding['response'].unique()
    for response in unique_class:
        df_data = data_encoding.loc[data_encoding['response'] == response]
        average = estimated_average_curve(df_data)[30:]
        domain = [data_domain[key][0] for key in data_domain.columns][30:]
        fig.add_trace(go.Scatter(x=domain, y=average,
                                 mode='lines',
                                 name=response),
                      row=row_v,
                      col=col_v)

    if i == 3:
        row_v+=1
        col_v=1
    else:
        col_v+=1
    print(row_v, col_v)
fig.update_layout(height=1600, width=1600)
fig.write_image("demo_multiple.svg")

