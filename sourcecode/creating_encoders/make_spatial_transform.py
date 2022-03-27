import pandas as pd
import sys
from sklearn.decomposition import PCA
import plotly.express as px

def create_dataset_transform(transform):

    header = ["p_{}".format(i) for i in range(len(transform[0]))]
    df = pd.DataFrame(transform, columns=header)
    return df

path_input = sys.argv[1]

first_componet = []
df_with_properties = pd.DataFrame()

list_df = []

for i in range(8):
    data_read = "{}Group_{}\\dataset.csv".format(path_input, i)
    print(data_read)
    df = pd.read_csv(data_read)
    residues = df.residue
    df = df.drop(columns=['residue'])

    print("Apply PCA")
    pca = PCA()
    pca.fit(df)
    #first_componet.append(pca.explained_variance_ratio_[0])
    transform = pca.transform(df)
    print(transform.shape)
    df_transform = create_dataset_transform(transform)
    print(df_transform.shape)
    df_with_properties['residue'] = residues
    df_with_properties['Group_{}'.format(i)] = df_transform['p_0']

    df_to_insert = pd.DataFrame()
    df_to_insert['residues'] = residues
    df_to_insert['Component 1'] = df_transform['p_1']
    df_to_insert['Component 2'] = df_transform['p_0']
    df_to_insert['label'] = 'Group {}'.format(i)

    list_df.append(df_to_insert)


print("Export matrix")
df_with_properties.to_csv("{}encoders_generated.csv".format(path_input), index=False)

print("Making plot")
df_join = pd.concat(list_df)

size_value = [1 for i in range(len(df_join))]
fig = px.scatter(df_join, x="Component 1", y="Component 2", color="label", size=size_value, hover_data=['label'])
fig.write_image("demo.svg")