#coding:utf-8
import pandas as pd
datafile = 'D:/WorkSpace/data/analyze/chapter7/demo/data/air_data.csv'
datafile2 = 'D:/WorkSpace/data/analyze/chapter7/demo/data/zscoredata.xls'
resultfile = 'D:/WorkSpace/data/analyze/chapter7/results/air_explore.xls'
cleanedfile = 'D:/WorkSpace/data/analyze/chapter7/results/data_cleaned.xls'
zscoredfile = 'D:/WorkSpace/data/analyze/chapter7/results/zscoreddata.xls'
outputfile = 'D:/WorkSpace/data/analyze/chapter7/results/resultdata.xls'
# data = pd.read_csv(datafile,encoding='utf-8')
# data = pd.read_excel(datafile2)
# explore = data.describe(percentiles=[],include='all')
# explore = explore.T
# print(data)
# print(explore)
# print(explore.T['count'])
# explore['null'] = len(data) - explore['count']
# print(explore)
# explore = explore[['null','max','min']]
# explore.columns = [u'空值数',u'最大值',u'最小值']
# explore.to_excel(resultfile)

# data = data[(data['SUM_YR_1'].notnull()) * (data['SUM_YR_2'].notnull())]
#
# index1 = data['SUM_YR_1'] != 0
# index2 = data['SUM_YR_2'] != 0
# index3 = ((data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0))
#
# data = data[index1 | index2 | index3]
#
# data.to_excel(cleanedfile)

# data = (data - data.mean(axis = 0))/(data.std(axis = 0))
# data.columns=['Z'+i for i in data.columns]
# data.to_excel(zscoredfile,index=False)

from sklearn.cluster import KMeans

k = 5
data = pd.read_excel(zscoredfile)

kmodel = KMeans(n_clusters=k,n_jobs=1)
kmodel.fit(data)
# print(kmodel.cluster_centers_)
# data = kmodel.cluster_centers_
# columns=['L','R','F','M','C']
# output = pd.DataFrame(data=data,columns=columns)
# output.to_excel(outputfile)
print(kmodel)
