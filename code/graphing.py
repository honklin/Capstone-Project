#type: ignore
import matplotlib.pyplot as plt
import numpy as np
import csv

length = list()
data = list()

with open('C:/Users/hconkli10/Downloads/data.csv', newline='') as file:
    points = list(csv.reader(file))
    for val in points:
        val = str(val).strip("[]''(),")
        data.append(float(val))
        length.append(float(len(data)))


plt.title("Pressure Sensor Map")
plt.xlabel("time(s)")
plt.ylabel("pressure(gF)")
plt.plot(data)
plt.show()
