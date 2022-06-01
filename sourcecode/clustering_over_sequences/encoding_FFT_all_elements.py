import sys
import os

import pandas as pd

path_input = sys.argv[1]
path_output = sys.argv[2]

list_encoders = os.listdir(path_input)

for element in list_encoders:
    dataset = pd.read_csv(path_input+element)

    break