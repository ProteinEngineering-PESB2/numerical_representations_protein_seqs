import pandas as pd
import sys
import numpy as np
import plotly.graph_objects as go

def create_average_curve(dataset_filter):

    average_value = [np.mean(dataset_filter[key]) for key in dataset_filter.columns if key not in ['id_seq','doc']]
    return average_value

dataset = pd.read_csv(sys.argv[1])
domain_data = pd.read_csv(sys.argv[2])
#enzyme
unique_docs = dataset['doc'].unique()
#unique_docs = [value for value in unique_docs if "alpha" in value]
fig = go.Figure()

for doc in unique_docs:
    df_filter = dataset.loc[dataset['doc'] == doc]
    response = create_average_curve(df_filter)[30:150]
    domain = [domain_data[key][0] for key in domain_data.columns][30:150]
    fig.add_trace(go.Scatter(x=domain, y=response,
                             mode='lines',
                             name=doc))

fig.write_image("enzyme.svg")

