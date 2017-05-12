import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
from scipy.stats import mode


df = pd.DataFrame.from_csv('/Users/wingify/PycharmProjects/CricFun/mostruns.csv')
df = df.set_index('Player')
#From the 2008-201
#print df.head()

print df.dtypes









# #
# #
# # web_stats = {'Day':[1,2,3,4,5,6],
# #              'Visitors':[43,34,65,56,29,76],
# #              'Bounce Rate':[65,67,78,65,45,52]}
# #
# # df = pd.DataFrame(web_stats)
# # print(df['Visitors'])
# #
# # df.plot()
# # plt.show()
#
# print from_json


