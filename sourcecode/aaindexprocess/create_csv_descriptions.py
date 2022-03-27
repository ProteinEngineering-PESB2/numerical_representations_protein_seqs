import sys
import pandas as pd

data = open(sys.argv[1], 'r')
path_output = sys.argv[2]

line = data.readline()

matrix_data = []

while line:
    values = line.replace("\n", "").split("|")
    row = [values[0], values[1][1:]]
    matrix_data.append(row)
    line = data.readline()
data.close()

df = pd.DataFrame(matrix_data, columns=['id_property', 'description'])
df.to_csv(path_output+"aa_index_db_descriptions.csv", index=False)

#Comment