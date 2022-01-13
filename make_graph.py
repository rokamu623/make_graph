from matplotlib import pyplot
from numpy import average
from sys import argv

### グラフのためのデータ取得 ###

# x軸の設定
xlabel = ["node=20", "node=40", "node=60", "node=80", "node=100"]
x = [1,2,3,4,5]

# 色の準備
colors = ["blue", "red", "green", "yellow"]
y = {}
# それぞれの棒要素の設定
y["Wait-suff"] = []
y["Al-avail"] = []
y["Dec-method"] = []

# それぞれの手法について
for key, value in y.items():
    # node=20, node=40...に対して
    for i in xlabel:
        # ./DATA/node=20_Wait-suff.txt のようなファイルを開く
        f = open("./DATA/"+i+"_"+key+".txt")
        # ファイルに書き込まれたメイクスパン列を配列として取得
        tmp = f.read().split("\n")
        arr = [int(n) for n in tmp if n != ""]
        y[key].append(average(arr))

"""
y =
{
    "Wait-suff": [node=20の値, node=40の値...node=100の値]
    "Al-avail": [node=20の値, node=40の値...node=100の値]
    "Dec-method": [node=20の値, node=40の値...node=100の値]
}
"""

### ここからグラフの描画処理 ###

fig = pyplot.figure()

i = 0
# 0.3ずつずらして棒グラフを3つ作る
for key, value in y.items():
    print(key+str(value))
    pyplot.bar([n-0.15+i*0.3 for n in x], value, width=0.3, color=colors[i], align="center", label=key)
    i += 1
pyplot.xticks(x, xlabel)
pyplot.legend()

fig.savefig("./output.png")
fig.savefig("./output.eps")