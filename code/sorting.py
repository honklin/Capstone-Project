#type: ignore
import matplotlib.pyplot as plt
import numpy as np
import csv

length = list()
data1 = list()
data2 = list()
data3 = list()

with open('C:/Users/hconkli10/Downloads/datar.csv', newline='') as file:
    data = list(csv.reader(file))
    for line in data:
        line = list(str(line).split(", "))
        s = 1
        for val in line:
            if (s == 1):
                data1.append(float(val.strip("[]''(),")))
                s = 2
            elif (s == 2):
                data2.append(float(val.strip("[]''(),")))
                s = 3
            elif (s == 3):
                data3.append(float(val.strip("[]''(),")))
                s = 1
                length.append(float(len(data2)))



plt.title("Pressure Sensor Map")
plt.xlabel("time(s)")
plt.ylabel("pressure(gF)")
plt.plot(data1,color = "firebrick")
plt.plot(data2,color = "darkblue")
plt.plot(data3,color = "darkviolet")
plt.show()
