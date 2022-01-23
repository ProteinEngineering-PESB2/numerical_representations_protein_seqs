import pandas as pd
import sys
import os
import json
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

def get_metrics_prediction(prediction, real_labels):
    accuracy = accuracy_score(real_labels, prediction)
    fscore = f1_score(real_labels, prediction, average='weighted')
    precision = precision_score(real_labels, prediction, average='weighted')
    recall = recall_score(real_labels, prediction, average='weighted')

    dict_data = {"accuracy": accuracy, "f_score": fscore, "precision": precision, "recall": recall}
    return dict_data

def estimated_training_performances(scores):

    json_training = {}
    for key in scores:
        if key not in ['fit_time', 'score_time']:
            json_training.update({key:np.mean(scores[key])})
    return json_training

def discretize_response_funct(json_data, response_data):

    response_data_d = [json_data[element] for element in response_data]
    return response_data_d

print("Get input params")
dataset = pd.read_csv(sys.argv[1])
dataset = dataset.dropna()

path_export = sys.argv[2]
response_key = sys.argv[3]
discretize_response = int(sys.argv[4])
suffix_dir = sys.argv[5]

json_response = {}

command = "mkdir {}exploring_rf_results_{}".format(path_export, suffix_dir)
os.system(command)

print("Preparing dataset")
response_data = dataset[response_key]
unique_response = dataset[response_key].unique()

columns_ignore = [column for column in dataset.columns if "p_" not in column]
dataset = dataset.drop(columns=columns_ignore)

print("Discretizing response")
if discretize_response == 1:
        index=0
        for element in unique_response:
            json_response.update({element:index})
            index+=1
        response_data = discretize_response_funct(json_response, response_data)

print("Prepare dataset")
X_train, X_test, y_train, y_test = train_test_split(dataset, response_data, test_size=0.30, random_state=42)

print("Start exploring")
scoring = ['precision_weighted', 'recall_weighted', 'accuracy', 'f1_weighted']

dict_response_training_process = []
for n_estimator in [100, 150, 200, 250, 500]:
    for criterion in ['gini', 'entropy']:
        dict_values = {"n_estimator": n_estimator, "criterion": criterion}
        rf_clf = RandomForestClassifier(n_estimators=n_estimator, criterion=criterion)
        rf_clf.fit(X_train, y_train)
        scores = cross_validate(rf_clf, X_train, y_train, scoring=scoring, cv=10)
        training_scores = estimated_training_performances(scores)
        dict_values.update({"training_scores":training_scores})

        response_predict = rf_clf.predict(X_test)
        testing_scores = get_metrics_prediction(response_predict, y_test)

        dict_values.update({"testing_scores": testing_scores})
        dict_response_training_process.append(dict_values)

print("Exporting results")
name_export_dict = "{}exploring_rf_results_{}\\mean_responses.json".format(path_export, suffix_dir)
name_export_results = "{}exploring_rf_results_{}\\results_exploring.json".format(path_export, suffix_dir)

with open(name_export_dict, 'w') as f1:
    json.dump(json_response, f1)

with open(name_export_results, 'w') as f2:
    json.dump(dict_response_training_process, f2)

print(dict_response_training_process)
