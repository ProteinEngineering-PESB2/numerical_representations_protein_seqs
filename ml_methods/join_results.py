import os
import pandas as pd
import sys
import json

def create_dataset_from_json(json_values):

    matrix_values = []
    for element in json_values:
        row_p1 = [element['n_estimator'], element['criterion']]
        row_p2 = [element['training_scores']['test_precision_weighted'], element['training_scores']['test_recall_weighted'], element['training_scores']['test_accuracy'], element['training_scores']['test_f1_weighted']]
        row_p3 = [element['testing_scores']['precision'],
                  element['testing_scores']['recall'], element['testing_scores']['accuracy'],
                  element['testing_scores']['f_score']]

        row = row_p1+ row_p2 + row_p3
        matrix_values.append(row)

    df_values = pd.DataFrame(matrix_values, columns=['n_estimator','criterion', 'precision_tra', 'recall_tra', 'accuracy_tra', 'f_score_tra', 'precision_test', 'recall_test', 'accuracy_test', 'f_score_test' ])
    return df_values

print("Process list dir")
data_testing = sys.argv[1]
list_files = os.listdir(data_testing)
list_files = [v for v in list_files if "json" in v]
list_dfs = []

for element in list_files:
    print("Process ", element)
    with open(data_testing+element, 'r') as data_load:
        values_training = json.load(data_load)
    df_value = create_dataset_from_json(values_training)
    df_value['file'] = element
    list_dfs.append(df_value)

print("Creating export file")
df_concat = pd.concat(list_dfs)
df_concat.to_csv(data_testing+"exporting_join_results.csv", index=False)