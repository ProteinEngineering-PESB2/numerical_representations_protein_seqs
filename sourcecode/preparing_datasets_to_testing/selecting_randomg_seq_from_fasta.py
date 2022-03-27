import pandas as pd
import sys
import random
from Bio import SeqIO

input_dataset = sys.argv[1]
number_examples = int(sys.argv[2])
path_export = sys.argv[3]

matrix_data = []
list_index = []
index=0
for record in SeqIO.parse(input_dataset, "fasta"):
    data_id = record.id
    sequence = str(record.seq)
    row = [data_id, sequence]
    matrix_data.append(row)
    list_index.append(index)
    index+=1

random.shuffle(list_index)

matrix_data_filter = []

for i in range(len(number_examples)):
    matrix_data_filter.append(matrix_data[list_index[i]])

df_export = pd.DataFrame(matrix_data_filter, columns=['id_seq', 'seq'])
df_export.to_csv(path_export+"data_processed.csv", index=False)