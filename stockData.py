import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation
import pandas_datareader.data as web

# this is path to txt of csv data
path = ""

print("Getting Stock Data...")
style.use('ggplot')

# get ticker data

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2020, 12, 31)

df = web.DataReader('TSLA', 'yahoo', start, end)
df['100ma'] = df['Adj Close'].rolling(window = 100).mean() # create 100 day moving average
df.dropna(inplace=True)

# create TSLA stock graph

#df = df['Close']
print(df.tail())
df.plot()

ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan = 1, colspan = 1, sharex = ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()

#######################################################################

# graph real-time stock chart (or even live sensor data)

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# read a csv in form:
"""
a, b
c, d
e, f
"""

def animate(i):
    graph_data =open(path, 'r').read()
    lines = graph_data.split('\n') # delimiter is new line char
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',') # delimiter within a line
            xs.append(x)
            ys.append(y)

    ax1.clear()
    ax1.plot(xs, ys)

"""
ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()    
"""