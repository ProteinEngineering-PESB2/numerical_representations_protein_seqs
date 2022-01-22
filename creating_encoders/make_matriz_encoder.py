import pandas as pd
import sys
import os

print("Getting properties")
dataset_labeled = pd.read_csv(sys.argv[1])
dataset_properties = pd.read_csv(sys.argv[2])
path_export = sys.argv[3]

print("Merge dataset")
dataset_merge = dataset_labeled.merge(dataset_properties, left_on='id_property', right_on='INDEX_CODE')

print("Split into datasets")
labels = dataset_merge['label'].unique()

for label in labels:
    command = "mkdir {}{}".format(path_export, label.replace(" ", "_"))
    os.system(command)

    print("Process label: ", label)
    df_search = dataset_merge.loc[dataset_merge['label'] == label]
    df_search = df_search.dropna().reset_index()
    df_search = df_search.drop(columns=['description', 'label', 'INDEX_CODE', 'index'])
    df_search_t = df_search.T
    df_search_t.to_csv("{}{}\\dataset.csv".format(path_export, label.replace(" ", "_")))
