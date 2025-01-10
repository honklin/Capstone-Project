#type: ignore
from sklearn.cluster import KMeans #Kmeans library
import matplotlib.pyplot as plt #library for graphing
import numpy as np #polynomial function library
import math #math library
import csv #data file library

#global variables
rlen = list()
rdata1 = list()
rdata2 = list()
rdata3 = list()

llen = list()
ldata1 = list()
ldata2 = list()
ldata3 = list()

clus = 0 #number of clusters


#sort sensor data for right shoe
with open('C:/Users/hconkli10/Downloads/datar.csv', newline='') as file: #access right shoe file
    rdata = list(csv.reader(file))
    for rline in rdata: #takes each line with data from 3 sensors
        rline = list(str(rline).split(", "))
        s = 1
        for val in rline: #isolates individual sensor data
            if (s == 1):
                rdata1.append(float(val.strip("[]''(),"))) #adds sensor 1 data
                s = 2
            elif (s == 2):
                rdata2.append(float(val.strip("[]''(),"))) #adds sensor 2 data
                s = 3
            elif (s == 3):
                rdata3.append(float(val.strip("[]''(),"))) #adds sensor 3 data
                s = 1
                rlen.append(float(len(rdata1))) #add length --> x-axis coordinates

#sort sensor data for left shoe
with open('C:/Users/hconkli10/Downloads/datal.csv', newline='') as file: #access left shoe file
    ldata = list(csv.reader(file))
    for lline in ldata: #takes each line with data from 3 sensors
        lline = list(str(lline).split(", "))
        s = 1
        for val in lline: #isolates individual sensor data
            if (s == 1):
                ldata1.append(float(val.strip("[]''(),"))) #adds sensor 1 data
                s = 2
            elif (s == 2):
                ldata2.append(float(val.strip("[]''(),"))) #adds sensor 2 data
                s = 3
            elif (s == 3):
                ldata3.append(float(val.strip("[]''(),"))) #adds sensor 3 data
                s = 1
                llen.append(float(len(ldata1))) #add length --> x-axis coordinates


#combine x-axis and y-axis data sets
rtotal1 = list(zip(rlen,rdata1))
rtotal2 = list(zip(rlen,rdata2))
rtotal3 = list(zip(rlen,rdata2))

ltotal1 = list(zip(llen,ldata1))
ltotal2 = list(zip(llen,ldata2))
ltotal3 = list(zip(llen,ldata2))


def elbow(total,length): #elbow method
    inertia = []
    ilen = []
    for i in range(1,len(length)+1): #tries all possible amounts of clusters
        k = KMeans(n_clusters=i)
        k.fit(total)
        inertia.append(k.inertia_)
        ilen.append(len(inertia))
    return inertia, ilen #returns elbow method graph

def clusters(inertias,length): #finds accurate number of clusters
    cl = -1
    old = 0
    diff = "0"
    oldiff = "0"
    for ft in range(1,len(inertias)): #isolates each coordinate in elbow method graph
        slope, intercept = np.polyfit(length, inertias, 1) #finds line of fit
        slope = round(slope)
        diff = str(slope - old)
        if (len(oldiff) == len(diff)): #graph becomes linear when slope first has the same number of digits
            cl = ft - 2 #cluster number is how many coordinates the graph took to become linear
            break
        else: #check next coordinates if graph is not linear
            length.pop(0)
            inertias.pop(0)
        old = slope
        oldiff = str(diff)
    return cl #return number of clusters

def centers(total): #finds the center of all clusters
    kmeans = KMeans(n_clusters=clus) #fits data with correct clusters
    kmeans.fit(total)
    centx = []
    centy = []
    centroids = kmeans.cluster_centers_ #finds list of all centroids
    for cent in centroids: #isolates centroid coordinates
        cent = str(cent).strip("[]")
        cent = cent.split()
        centx.append(float(cent[0].strip("[]''(),")))
        centy.append(float(cent[1].strip("[]''(),")))
    centt = list(zip(centx,centy)) #combine x and y data
    return centt

def analyze(right,left): #compares shoe data to find inconsistencies
    prob = ""
    for x in range(clus): #isolates each cluster
        rightt = str(right[x]).split()
        rightx = float(rightt[0].strip("[]''(),")) #right x coordinate
        righty = float(rightt[1].strip("[]''(),")) #right y coordinate
        leftt = str(left[x]).split()
        leftx = float(leftt[0].strip("[]''(),")) #left x coordinate
        lefty = float(leftt[1].strip("[]''(),")) #left y coordinate
        error = math.dist([leftx,lefty],[rightx,righty]) #finds distance between centers of the two shoes 
        if (error > 75): #return a problem if shoes are too uneven
            prob = "uneven pressure"
        else:
            prob = "even pressure"
    return prob


#find elbow method graph for each sensor
rinert1,irlen1 = elbow(rtotal1,rlen)
rinert2,irlen2 = elbow(rtotal2,rlen)
rinert3,irlen3 = elbow(rtotal3,rlen)

linert1,illen1 = elbow(ltotal1,llen)
linert2,illen2 = elbow(ltotal2,llen)
linert3,illen3 = elbow(ltotal3,llen)

#find correct number of clusters for each sensor
rclus1 = clusters(rinert1,irlen1)
rclus2 = clusters(rinert2,irlen2)
rclus3 = clusters(rinert3,irlen3)

lclus1 = clusters(linert1,illen1)
lclus2 = clusters(linert2,illen2)
lclus3 = clusters(linert3,illen3)

rclus = round((rclus1+rclus2+rclus3)/3)
lclus = round((lclus1+lclus2+lclus3)/3)
clus = round((rclus+lclus)/2)

#find centers of clusters for each sensor
rcent1 = centers(rtotal1)
rcent2 = centers(rtotal2)
rcent3 = centers(rtotal3)

lcent1 = centers(ltotal1)
lcent2 = centers(ltotal2)
lcent3 = centers(ltotal3)

#compare both shoes sensor data
prob1 = analyze(rcent1,lcent1)
prob2 = analyze(rcent2,lcent2)
prob3 = analyze(rcent3,lcent3)
print("Sensor 1:")
print(prob1)
print("Sensor 2:")
print(prob2)
print("Sensor 3:")
print(prob3)

#graph left and right shoe sensor data
plt.title("Pressure Sensor Map")
plt.xlabel("Time(s)")
plt.ylabel("Pressure(gF)")
plt.plot(rdata1,color = "firebrick")
plt.plot(rdata2,color = "firebrick")
plt.plot(rdata3,color = "firebrick")
plt.plot(ldata1,color = "darkblue")
plt.plot(ldata2,color = "firebrick")
plt.plot(ldata3,color = "darkviolet")
plt.show()
