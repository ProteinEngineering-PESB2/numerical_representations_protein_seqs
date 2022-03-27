import sys
import pandas as pd

path_input = sys.argv[1]

type_encoding = ["encoding_FFT", "encoding_properties"]

matrix_config = []

for encoding in type_encoding:
    if encoding == "encoding_FFT":
        for i in range(8):
            dataset = "{}{}\\Group_{}_fft_encoding_v2.csv".format(path_input, encoding, i)
            path_export = "{}{}\\".format(path_input, encoding)
            row = [dataset, path_export, 'doc', 1, 'Group_{}'.format(i)]
            matrix_config.append(row)
    elif encoding == "encoding_properties":
        for i in range(8):
            dataset = "{}{}\\Group_{}_properties.csv".format(path_input, encoding, i)
            path_export = "{}{}\\".format(path_input, encoding)
            row = [dataset, path_export, 'doc', 1, 'Group_{}'.format(i)]
            matrix_config.append(row)
df = pd.DataFrame(matrix_config, columns=['input', 'path', 'response', 'discrete', 'suffix'])
df.to_csv("function_class_config.csv", index=False)