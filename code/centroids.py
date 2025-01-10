from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import csv

length = list()
data = list()
inertias = []
centx = list()
centy = list()

with open('C:/Users/hconkli10/Downloads/data.csv', newline='') as file:
    points = list(csv.reader(file))
    for val in points:
        val = str(val).strip("[]''(),")
        data.append(float(val))
        length.append(float(len(data)))

total = list(zip(length,data))

kmeans = KMeans(n_clusters=3)
kmeans.fit(total)
centroids = kmeans.cluster_centers_
for cent in centroids:
    cent = str(cent).split()
    print(cent)
    centa = cent[1]
    centb = cent[2].strip("]")
    centx.append(float(centa))
    centy.append(float(centb))
    
print(centroids)
plt.title("Pressure Sensor Map")
plt.xlabel("Time(s)")
plt.ylabel("Pressure(gF)")
plt.scatter(length, data, c=kmeans.labels_)
plt.scatter(centx,centy)
plt.show()
