import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.width', 1000)
data_train=pd.read_csv('/Users/yiliu/lllyeeData/all/train.csv')
print(data_train)
print(data_train['SalePrice'].describe())
sns.distplot(data_train['SalePrice'])#kde=False去掉曲线

'''
峰度：峰度（Kurtosis）是描述某变量所有取值分布形态陡缓程度的统计量。它是和正态分布相比较的。
Kurtosis=0 与正态分布的陡缓程度相同。
Kurtosis>0 比正态分布的高峰更加陡峭——尖顶峰
Kurtosis<0 比正态分布的高峰来得平台——平顶峰计算公式：β = M_4 /σ^4 偏度：
偏度：偏度（Skewness）是描述某变量取值分布对称性的统计量。
Skewness=0 分布形态与正态分布偏度相同
Skewness>0 正偏差数值较大，为正偏或右偏。长尾巴拖在右边。
Skewness<0 负偏差数值较大，为负偏或左偏。长尾巴拖在左边。 计算公式： S= (X^ - M_0)/δ Skewness 越大，分布形态偏移程度越大。
'''
print("Skewness: %.2f" %data_train['SalePrice'].skew())#.2表示定义小数点精度，f：float
print("Kurtosis: %.2f" %data_train['SalePrice'].kurt())
'''var = 'CentralAir'
data = pd.concat([data_train['SalePrice'], data_train[var]], axis=1)#axis=1横向合并
fig = sns.boxplot(x=var, y="SalePrice", data=data)
fig.axis(ymin=0, ymax=800000)
'''
'''
var1='OverallQual'
data1=pd.concat([data_train['SalePrice'],data_train[var1]],axis=1)
fig1=sns.boxplot(x=var1,y="SalePrice",data=data1)
fig1.axis(ymin=0,ymax=800000)

var2='YearBuilt'
data2=pd.concat([data_train['SalePrice'],data_train[var2]],axis=1)
f, ax = plt.subplots(figsize=(26, 12))#设置画布尺寸大小
fig2=sns.boxplot(x=var2,y='SalePrice',data=data2)
fig2.axis(ymin=0,ymax=8000000)

var = 'YearBuilt'
data = pd.concat([data_train['SalePrice'], data_train[var]], axis=1)
data.plot.scatter(x=var, y="SalePrice", ylim=(0, 800000))


# Neighborhood
var = 'Neighborhood'
data = pd.concat([data_train['SalePrice'], data_train[var]], axis=1)
f, ax = plt.subplots(figsize=(26, 12))
fig = sns.boxplot(x=var, y="SalePrice", data=data)
fig.axis(ymin=0, ymax=800000)'''
corrmat = data_train.corr()#协方差
f, ax = plt.subplots(figsize=(20, 9))
sns.heatmap(corrmat, vmax=0.8, square=True)
plt.show()