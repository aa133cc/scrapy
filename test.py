# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from pylab import mpl
# mpl.rcParams['font.sans-serif'] = ['SimHei']
#
# path = open(r'C:\Users\宽\Desktop\bzhan.csv')
# data = pd.read_csv(path)
#
# play = []
# pl = list(data.play_num)
# for i in pl:
#     if i[-1] == "亿":
#         play.append((i[:-1] * 10000))
#     else:
#         play.append(i)
# print(play)
#
# danmu = []
# dm = list(data.ping_lun)
# for i in dm:
#     if i[-1] == "万":
#         danmu.append(eval(i[:-1]) * 10000)
#     else:
#         danmu.append(i)
# print(danmu)
#
# print(data.corr())
# print(data.describe() )
#
# plt.plot()


str = 'k'

mystr = 'kkkk'


print(mystr.join('royu'))