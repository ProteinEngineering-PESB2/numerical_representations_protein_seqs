import sys
import os
import pandas as pd
from Bio import SeqIO

fasta_sequences = sys.argv[1]
path_export = sys.argv[2]

sequences = []
activities = []

for record in SeqIO.parse(fasta_sequences, "fasta"):
    sequences.append(str(record.seq))
    activity = record.id.split(":")[-1]
    activities.append(activity)

df_data = pd.DataFrame()
df_data['sequence'] = sequences
df_data['activity'] = activities

for activity in df_data['activity'].unique():
    command = "mkdir {}{}".format(path_export, activity)
    os.system(command)

    filter_data = df_data.loc[df_data['activity'] == activity]
    filter_data = filter_data.reset_index()
    filter_data = filter_data.drop(columns = ['index', 'activity'])
    name_export = "{}.csv".format(activity)
    filter_data.to_csv(name_export, index=False)
