import pandas as pd
import sys
import json

def searching_labels(dict_values, algorithm, params):

    print(algorithm)
    print(params)
    key_params = 'K' if algorithm in ['k-means', 'Birch'] else 'param'
    algorithm_use = 'K-means' if algorithm=='k-means' else algorithm

    labels = None

    for model in dict_values:
        if model['algorithm'] == algorithm_use and model[key_params] == params:
            labels = model['labels']
            break
    return labels

print("Get information")
dataset = pd.read_csv(sys.argv[1])
dataset = dataset.dropna().reset_index()
index_properties = dataset['INDEX_CODE']
data_properties = dataset.drop(columns=['INDEX_CODE'])

selected_models = pd.read_csv(sys.argv[2])

with open(sys.argv[3], 'r') as data_json:
    data_models = json.load(data_json)

path_export = sys.argv[4]

print("Searching partitions")
for i in range(len(selected_models)):
    algorithm = selected_models['algorithm'][i]
    params = selected_models['params'][i]

    labels = searching_labels(data_models, algorithm, params)
    df_export = pd.DataFrame()
    df_export['properties_values'] = index_properties
    df_export['label'] = labels

    name_export = "{}_{}.csv".format(algorithm, params)
    print("Export dataset: ", name_export)

    df_export.to_csv(path_export+name_export, index=False)

