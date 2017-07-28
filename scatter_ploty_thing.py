import matplotlib.mlab as mlab
from os import chdir
import matplotlib as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


chdir("/home/ece411c/Documents")

file = r'shorter_test.csv'
df = pd.read_csv(file)
# print df.head()

# reader = csv.reader(df.splitlines, delimiter=',')
# for row in reader:
#     print('\t'.join(row))

matrix = df.as_matrix()
#latitude = matrix[:, 0]
power = matrix[:, 7]
freq = matrix[:, 9]
event_time = matrix[:, 3]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].

xs = freq.tolist()
ys = event_time.tolist()
zs = power.tolist()
ax.scatter(xs, ys, zs, c='b', marker='o')


ax.set_zlabel('Power')
ax.set_ylabel('Sample Number')
ax.set_xlabel('Frequency')
# ax.set_xlim3d(-110, -175)
# ax.set_ylim3d(1000, 50000)
# ax.set_zlim3d(680e6, 890e6)

plt.show()