import pandas as pd
import sys

def get_overfitting_rage(dataset, training_col, testing_col):

    column_values = []
    for i in range(len(dataset)):
        rate = float(dataset[training_col][i]) / float(dataset[testing_col][i])
        column_values.append(rate)
    return column_values

dataset = pd.read_csv(sys.argv[1])
path_export = sys.argv[2]

print("Estimated overfitting")

value_precision = get_overfitting_rage(dataset, 'precision_tra', 'precision_test')
value_recall = get_overfitting_rage(dataset, 'recall_tra', 'recall_test')
value_accuracy = get_overfitting_rage(dataset, 'accuracy_tra', 'accuracy_test')
value_f_score = get_overfitting_rage(dataset, 'f_score_tra', 'f_score_test')

dataset['precision_rate'] = value_precision
dataset['recall_rate'] = value_recall
dataset['accuracy_rate'] = value_accuracy
dataset['fscore_rate'] = value_f_score

dataset.to_csv(path_export+"adding_overfitting_rate.csv", index=False)