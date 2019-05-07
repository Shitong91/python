import numpy as np
import operator

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
