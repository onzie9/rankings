import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
import pylab as pl
from colour import Color

red = Color("red")
colors = list(red.range_to(Color("black"),20))
print(colors[5])

df = pd.read_csv('allrounds.csv')

#for i in range(34):
 #   print(df.iat[0,i])

lines1 = []
for i in range(2, 33):
    lines1.append([(-1,-df.iat[0,0]-1),(0,-df.iat[0,0]-1)])
    lines1.append([(i-2, -df.iat[0, i]), (i-1, -df.iat[0, i+1])])

lines2 = []
for i in range(2, 33):
    lines2.append([(-1, -df.iat[1, 0] - 1), (0, -df.iat[1, 0] - 1)])
    lines2.append([(i-2, -df.iat[1, i]), (i-1, -df.iat[1, i+1])])

lines3 = []
for i in range(2, 33):
    lines3.append([(-1, -df.iat[2, 0] - 1), (0, -df.iat[2, 0] - 1)])
    lines3.append([(i-2, -df.iat[2, i]), (i-1, -df.iat[2, i+1])])

lines4 = []
for i in range(2, 33):
    lines4.append([(-1, -df.iat[3, 0] - 1), (0, -df.iat[3, 0] - 1)])
    lines4.append([(i-2, -df.iat[3, i]), (i-1, -df.iat[3, i+1])])

lines5 = []
for i in range(2, 33):
    lines5.append([(-1, -df.iat[4, 0] - 1), (0, -df.iat[4, 0] - 1)])
    lines5.append([(i-2, -df.iat[4, i]), (i-1, -df.iat[4, i+1])])

lines6 = []
for i in range(2, 33):
    lines6.append([(-1, -df.iat[5, 0] - 1), (0, -df.iat[5, 0] - 1)])
    lines6.append([(i-2, -df.iat[5, i]), (i-1, -df.iat[5, i+1])])

lines7 = []
for i in range(2, 33):
    lines7.append([(-1, -df.iat[6, 0] - 1), (0, -df.iat[6, 0] - 1)])
    lines7.append([(i-2, -df.iat[6, i]), (i-1, -df.iat[6, i+1])])

lines8 = []
for i in range(2, 33):
    lines8.append([(-1, -df.iat[7, 0] - 1), (0, -df.iat[7, 0] - 1)])
    lines8.append([(i-2, -df.iat[7, i]), (i-1, -df.iat[7, i+1])])

lines9 = []
for i in range(2, 33):
    lines9.append([(-1, -df.iat[8, 0] - 1), (0, -df.iat[8, 0] - 1)])
    lines9.append([(i-2, -df.iat[8, i]), (i-1, -df.iat[8, i+1])])

lines10 = []
for i in range(2, 33):
    lines10.append([(-1, -df.iat[9, 0] - 1), (0, -df.iat[9, 0] - 1)])
    lines10.append([(i-2, -df.iat[9, i]), (i-1, -df.iat[9, i+1])])

lines11 = []
for i in range(2, 33):
    lines11.append([(-1, -df.iat[10, 0] - 1), (0, -df.iat[10, 0] - 1)])
    lines11.append([(i-2, -df.iat[10, i]), (i-1, -df.iat[10, i+1])])

lines12 = []
for i in range(2, 33):
    lines12.append([(-1, -df.iat[11, 0] - 1), (0, -df.iat[11, 0] - 1)])
    lines12.append([(i-2, -df.iat[11, i]), (i-1, -df.iat[11, i+1])])

lines13 = []
for i in range(2, 33):
    lines13.append([(-1, -df.iat[12, 0] - 1), (0, -df.iat[12, 0] - 1)])
    lines13.append([(i-2, -df.iat[12, i]), (i-1, -df.iat[12, i+1])])

lines14 = []
for i in range(2, 33):
    lines14.append([(-1, -df.iat[13, 0] - 1), (0, -df.iat[13, 0] - 1)])
    lines14.append([(i-2, -df.iat[13, i]), (i-1, -df.iat[13, i+1])])

lines15 = []
for i in range(2, 33):
    lines15.append([(-1, -df.iat[14, 0] - 1), (0, -df.iat[14, 0] - 1)])
    lines15.append([(i-2, -df.iat[14, i]), (i-1, -df.iat[14, i+1])])

lines16 = []
for i in range(2, 33):
    lines16.append([(-1, -df.iat[15, 0] - 1), (0, -df.iat[15, 0] - 1)])
    lines16.append([(i-2, -df.iat[15, i]), (i-1, -df.iat[15, i+1])])

lc1 = mc.LineCollection(lines1, color=str(colors[0]), linewidths=.5)
lc2 = mc.LineCollection(lines2, color=str(colors[1]), linewidths=.5)
lc3 = mc.LineCollection(lines3, color=str(colors[2]), linewidths=.5)
lc4 = mc.LineCollection(lines4, color=str(colors[3]), linewidths=.5)
lc5 = mc.LineCollection(lines5, color=str(colors[4]), linewidths=.5)
lc6 = mc.LineCollection(lines6, color=str(colors[5]), linewidths=.5)
lc7 = mc.LineCollection(lines7, color=str(colors[6]), linewidths=.5)
lc8 = mc.LineCollection(lines8, color=str(colors[7]), linewidths=.5)
lc9 = mc.LineCollection(lines9, color=str(colors[8]), linewidths=.5)
lc10 = mc.LineCollection(lines10, color=str(colors[9]), linewidths=.5)
lc11 = mc.LineCollection(lines11, color=str(colors[10]), linewidths=.5)
lc12 = mc.LineCollection(lines12, color=str(colors[11]), linewidths=.5)
lc13 = mc.LineCollection(lines13, color=str(colors[12]), linewidths=.5)
lc14 = mc.LineCollection(lines14, color=str(colors[13]), linewidths=.5)
lc15 = mc.LineCollection(lines15, color=str(colors[14]), linewidths=.5)
lc16 = mc.LineCollection(lines16, color=str(colors[15]), linewidths=.5)

fig, ax = pl.subplots()

ax.add_collection(lc1)
ax.add_collection(lc2)
ax.add_collection(lc3)
ax.add_collection(lc4)
ax.add_collection(lc5)
ax.add_collection(lc6)
ax.add_collection(lc7)
ax.add_collection(lc8)
ax.add_collection(lc9)
ax.add_collection(lc10)
ax.add_collection(lc11)
ax.add_collection(lc12)
ax.add_collection(lc13)
ax.add_collection(lc14)
ax.add_collection(lc15)
ax.add_collection(lc16)
ax.autoscale()
ax.margins(0.1)

plt.show()