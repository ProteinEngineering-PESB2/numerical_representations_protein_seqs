import pandas as pd
import sys
from Bio import SeqIO

input_dataset = sys.argv[1]
path_export = sys.argv[2]

matrix_data = []
for record in SeqIO.parse(input_dataset, "fasta"):
    data_id = record.id.split(":")
    sequence = str(record.seq)

