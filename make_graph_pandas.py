from matplotlib import pyplot
from numpy import average
from sys import argv
import pandas
import numpy
import seaborn

xlabel = ["node=20", "node=40", "node=60", "node=80", "node=100"]
methods = ["Wait-suff", "Al-avail"]

data = pandas.DataFrame({"method": [], "parameter": [], "makespan": []})

idx = 0
for method in methods:
    for x in xlabel:
        f = open("./DATA/"+x+"_"+method+".txt") # node=20_Wait-suff.txt のようなファイルを開く
        tmp = f.read().split("\n")
        for i in [int(n) for n in tmp if n != ""]:
            data.loc[str(idx)] = [method, x, i] # 手法、パラメータ、データ
            idx += 1

#print(data)
fig = pyplot.figure()

seaborn.boxplot(x="parameter", y="makespan", hue="method", data=data, palette="Blues") #横軸parameter、縦軸makespanのグラフをmethodごとに並べる

fig.savefig("./output.png")
fig.savefig("./output.eps")