import pandas as pd
import os
import sys

config_data = pd.read_csv(sys.argv[1])

for i in range(len(config_data)):
    command = "python exploring_random_forest.py {} {} {} {} {}".format(config_data['input'][i],
                                                                        config_data['path_output'][i],
                                                                        config_data['response'][i],
                                                                        int(config_data['discrete'][i]),
                                                                        config_data['suffix'][i])
    print(command)
    os.system(command)
