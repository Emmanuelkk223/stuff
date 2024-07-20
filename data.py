# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import seaborn as sns

# Generate example data (make_moons dataset)
X, y = make_moons(n_samples=300, noise=0.1, random_state=0)

# Applying DBSCAN
epsilon = 0.2
min_samples = 5
db = DBSCAN(eps=epsilon, min_samples=min_samples)
clusters = db.fit_predict(X)

# Adding cluster labels to the dataframe
df = pd.DataFrame(X, columns=['Feature 1', 'Feature 2'])
df['Cluster'] = clusters

# Plotting the clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Feature 1', y='Feature 2', hue='Cluster', palette='Set1', data=df)
plt.title('DBSCAN Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
