import pandas as pd
import sys
from Bio import SeqIO

input_dataset = sys.argv[1]
path_export = sys.argv[2]

matrix_data = []
for record in SeqIO.parse(input_dataset, "fasta"):
    data_id = record.id.split(":")
    sequence = str(record.seq)
    row = [data_id[0], sequence, data_id[-1]]
    matrix_data.append(row)

df_export = pd.DataFrame(matrix_data, columns=['id_seq', 'seq', 'response'])
df_export.to_csv(path_export+"process_dataset.csv", index=False)


