import pandas as pd
import sys
import clustering_algorithms
import plotly.express as px

print("Get input data")
data_properties = pd.read_csv(sys.argv[1])
encoders_embedding = pd.read_csv(sys.argv[2])
path_export = sys.argv[3]

print("Processing best partitions")
k=8
#for k in range(5, 11):
command = "mkdir {}k_means_{}".format(path_export, k)
print(command)
#os.system(command)

clustering = clustering_algorithms.aplicateClustering(encoders_embedding)
clustering.aplicateKMeans(k)
label_values = ["Group {}".format(element) for element in clustering.labels]

data_properties['label'] = label_values
encoders_embedding['label'] = label_values
encoders_embedding['Component 1'] = encoders_embedding['p_1']
encoders_embedding['Component 2'] = encoders_embedding['p_0']

size_value = [1 for i in range(len(encoders_embedding))]

fig = px.scatter(encoders_embedding, x="Component 2", y="Component 1", color="label", size=size_value, hover_data=['label'])
fig.write_image("{}best_partitions\\scatter_plot.svg".format(path_export))
data_properties.to_csv("{}best_partitions\\properties_clustered.csv".format(path_export), index=False)

'''
print("Processing best partitions")
for k in range(5, 11):
    command = "mkdir {}birch_{}".format(path_export, k)
    #os.system(command)
    print(command)
    clustering = clustering_algorithms.aplicateClustering(encoders_embedding)
    clustering.aplicateBirch(k)
    data_properties['label'] = clustering.labels
    encoders_embedding['label'] = clustering.labels

    fig = px.scatter(encoders_embedding, x="p_0", y="p_1", color="label", symbol="label")
    fig.write_image("{}birch_{}\\scatter_plot.png".format(path_export, k))
    data_properties.to_csv("{}birch_{}\\properties_clustered.csv".format(path_export, k), index=False)

print("Processing best partition")
for linkage in ['ward', 'complete', 'average', 'single']:
    for affinity in ['euclidean']:
        for k in range(5, 11):
            clustering = clustering_algorithms.aplicateClustering(encoders_embedding)
            response = clustering.aplicateAlgomerativeClustering(linkage, affinity, k)

            params = "{}-{}-{}".format(linkage, affinity, k)
            command = "mkdir {}{}".format(path_export, params)
            os.system(command)
            print(command)
            clustering = clustering_algorithms.aplicateClustering(encoders_embedding)
            clustering.aplicateBirch(k)
            data_properties['label'] = clustering.labels
            encoders_embedding['label'] = clustering.labels

            fig = px.scatter(encoders_embedding, x="p_0", y="p_1", color="label", symbol="label")
            fig.write_image("{}{}\\scatter_plot.png".format(path_export, params))
            data_properties.to_csv("{}{}\\properties_clustered.csv".format(path_export, params), index=False)
'''