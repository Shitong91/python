import numpy as np
import operator
import matplotlib.pyplot as plt
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines()) #readlines 一次读取所有内容按行返回list
    #len 用len()函数可以获得list元素的个数，这里返回文件的行数
    returnMat = np.zeros((numberOfLines,3))
    classLabelVector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip() #去除字符串首尾的空格
        listFromLine = line.split('\t') #以横向制表符分开
        returnMat [index,:] = listFromLine[0:3]
        labels = {'didntLike':1, 'smallDoses':2, 'largeDoses':3}
        classLabelVector.append(labels[listFromLine[-1]]) #-1表示切片中的最后一个元素
        index +=1
    return returnMat, classLabelVector

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0] # shape[0]返回矩阵的行数
    diffMat=np.tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat =diffMat**2   #差值求平方
    sqDistances =np.sum(sqDiffMat,axis=1) #按列求和
    distances = sqDistances**0.5
    sortedDistIndicies =np.argsort(distances)
    classCout={}   #定义一个dict
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCout[voteIlabel] = classCout.get(voteIlabel,0) + 1
    sortedClassCout = sorted(classCout.items(),
            key=operator.itemgetter(1), reverse=True)
    return sortedClassCout[0][0]

#group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
#lables = ['A','A', 'B', 'B']
#result=classify0([0,0], group, lables, 3)
#print(result)
datingDataMat,datingLabels = file2matrix('datingTestSet.txt')
print(datingDataMat)
print(datingLabels[0:10])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*np.array(datingLabels), 15.0*np.array(datingLabels)) #这种画图的方式值得借鉴
plt.show()


