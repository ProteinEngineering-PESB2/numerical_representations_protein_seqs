import pandas as pd
import sys
import random

dataset = pd.read_csv(sys.argv[1])
dataset = dataset.loc[dataset['filter_example'] == 0].reset_index()

number_examples = int(sys.argv[2])
path_export = sys.argv[3]

list_index = [i for i in range(len(dataset))]
random.shuffle(list_index)

matrix_data = []

for i in range(number_examples):
    row = [dataset['sequence'][list_index[i]], dataset['ddg_response'][list_index[i]]]
    matrix_data.append(row)

df_export = pd.DataFrame(matrix_data, columns=['seq', 'ddg_response'])
df_export.to_csv(path_export+"processed_data.csv", index=False)
