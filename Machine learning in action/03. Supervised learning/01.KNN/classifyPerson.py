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

# normalization
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(dataSet.shape)
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m,1))
    normDataSet = normDataSet/np.tile(ranges,(m,1))
    return normDataSet, ranges, minVals

#classifyPeson
def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier milier earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = np.array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)
    print("you will probably like this person:", resultList[classifierResult-1])

classifyPerson()

