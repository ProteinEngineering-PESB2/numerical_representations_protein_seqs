import pandas as pd
import os
import sys

config = pd.read_csv(sys.argv[1])

for i in range(len(config)):
    command = "python exploring_random_forest.py {} {} {} {} {}".format(config['input'][i], config['path'][i], config['response'][i], config['discrete'][i], config['suffix'][i])
    print(command)
    os.system(command)
