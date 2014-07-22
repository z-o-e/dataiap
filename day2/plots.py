import matplotlib.pyplot as plt
import sys
sys.path.append('resources/util/')
from map_util import *
import json
import random
random.seed(0)

fig = plt.figure(figsize=(50, 30))

N = 100
xs = range(N)
y1 = [random.randint(50,100) for i in xs]
y2 = [random.randint(0,50) for i in xs]


# bar
import numpy as np
left = np.arange(len(xs))
width = 1 
subplot = fig.add_subplot(3,2,1)
subplot.bar(left, y1, width=width, color='red')
subplot.bar(left, y2, width=width, bottom=xs, color='green')

# line
subplot = fig.add_subplot(3,2,2)
subplot.plot(xs, y1, xs, y2)

# box
subplot = fig.add_subplot(3,2,3)
boxdata1=[random.randint(0,30) for i in xrange(10)]
boxdata2=[random.randint(20,50) for i in xrange(10)]
boxdata3=[random.randint(40,70) for i in xrange(10)]
data = [boxdata1,boxdata2,boxdata3,]
subplot.plot(data)

# scatter
subplot = fig.add_subplot(3,2,4)
subplot.scatter(xs, y1, c='blue',marker='o', alpha=None)

# maps
# map of countries
subplot = fig.add_subplot(3,2,5)
data = json.load(file('../datasets/geo/id-countries.json'))
for fips in data:
    draw_country(subplot.fips)
# map of states
subplot = fig.add_subplot(3,2,6)
data = json.load(file('../datasets/geo/id-countries.json'))
for state in data:
    draw_state(subplot,state)
