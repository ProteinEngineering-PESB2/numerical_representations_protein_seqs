import pandas as pd
import sys
import numpy as np
import plotly.graph_objects as go

def create_average_curve(dataset_filter):

    average_value = [np.mean(dataset_filter[key]) for key in dataset_filter.columns if key not in ['id_seq','doc']]
    return average_value

def get_dataset(dataset, folding):
    matrix_data = []
    for i in range(len(dataset)):
        if folding in dataset['doc'][i] and 'alpha_beta' not in dataset['doc'][i]:
            row = [dataset[value][i] for value in dataset.columns]
            matrix_data.append(row)
    df_search = pd.DataFrame(matrix_data, columns=dataset.columns)
    return df_search

dataset = pd.read_csv(sys.argv[1])
domain_data = pd.read_csv(sys.argv[2])
unique_docs = dataset['doc'].unique()
enzyme = ["alpha", "beta"]

for enzyme_value in enzyme:
    fig = go.Figure()

    df_filter = get_dataset(dataset, enzyme_value)

    unique_enzyme = df_filter['doc'].unique()
    print(unique_enzyme)
    for enzyme_data in unique_enzyme:
        df_search = df_filter.loc[df_filter['doc'] == enzyme_data]
        response = create_average_curve(df_search)[30:150]
        print(response)
        domain = [domain_data[key][0] for key in domain_data.columns][30:150]
        fig.add_trace(go.Scatter(x=domain, y=response,
                                 mode='lines',
                                 name=enzyme_data))

    fig.write_image("{}.svg".format(enzyme_value))
