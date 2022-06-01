import pandas as pd
import sys

dataset = pd.read_csv(sys.argv[1])
path_output = sys.argv[2]

sequences = dataset['seq']
response = dataset['response']

