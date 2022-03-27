import pandas as pd
import sys
import numpy as np

def encoding_seq(sequence, encoders, group, allow_residues):

    vector_encoder = []
    sequence = sequence.upper()
    for residue in sequence:
        if residue in allow_residues:
            df_enc = encoders.loc[encoders['residue'] == residue].reset_index()
            vector_encoder.append(df_enc[group][0])
        else:
            vector_encoder.append(None)
    return vector_encoder

#Get params
dataset = pd.read_csv(sys.argv[1])
properties_values = pd.read_csv(sys.argv[2])
key_seq = sys.argv[3]
path_export = sys.argv[4]

columns = dataset.columns
columns_filter = [value for value in columns if value != key_seq]

allow_residues = [residue for residue in properties_values['residue']]

for group in ['Group_0','Group_1','Group_2','Group_3','Group_4','Group_5','Group_6','Group_7']:
    print("Encoding_values using group: ", group)
    matrix_encoding = []
    length_data = []
    for i in range(len(dataset)):
        print("Encoding sequence: ", i)
        sequence = dataset[key_seq][i]
        encoding_sequence = encoding_seq(sequence, properties_values, group, allow_residues)
        matrix_encoding.append(encoding_sequence)
        length_data.append(len(encoding_sequence))

    print("Apply zero padding")
    max_value = np.max(length_data)

    for i in range(len(matrix_encoding)):
        for j in range(len(matrix_encoding[i]), max_value):
            matrix_encoding[i].append(0)

    print("Exporting_df")
    header = ["p_{}".format(i) for i in range(max_value)]
    df_export = pd.DataFrame(matrix_encoding, columns=header)
    for column in columns_filter:
        df_export[column] = dataset[column]

    print(df_export)
    df_export.to_csv("{}{}_properties.csv".format(path_export, group), index=False)

