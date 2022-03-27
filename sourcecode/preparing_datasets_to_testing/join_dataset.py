import pandas as pd
import sys
import os

path_input = sys.argv[1]
list_files = os.listdir(path_input)

list_df = []
counts = []
print("Reading documents")
for element in list_files:
    name_doc = "{}{}".format(path_input, element)
    df_reader = pd.read_csv(name_doc)
    df_reader['doc'] = element
    list_df.append(df_reader)
    counts.append(len(df_reader))

print("Creating random dataset using the min values to make a balance dataset")
min_length = min(counts)

print(counts)
list_df_filter = []

for df in list_df:
    df_filter = df[:min_length]
    list_df_filter.append(df_filter)

df_filter_concat = pd.concat(list_df_filter)
df_filter_concat.to_csv(path_input+"dataset_processed.csv", index=False)
