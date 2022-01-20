import pandas as pd
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

print("Get inputs data")
dataset = pd.read_csv(sys.argv[1])

print("Vectorize the descriptions")
vectorizer = TfidfVectorizer(stop_words={'english'})
X = vectorizer.fit_transform(dataset['description'])

Sum_of_squared_distances = []
K = range(2,10)
for k in K:
   km = KMeans(n_clusters=k, max_iter=300, n_init=10)
   km = km.fit(X)
   Sum_of_squared_distances.append(km.inertia_)

plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()

true_k = 8
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=300, n_init=10)
model.fit(X)
labels=model.labels_
data_Result=pd.DataFrame(list(zip(dataset['description'],labels)),columns=['description','cluster'])
print(data_Result.sort_values(by=['cluster']))
