from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','C']
	return group,labels

def getDistance(labeledData,inputData):
	distance = sqrt((labeledData[0]-inputData[0])*(labeledData[0]-inputData[0])+(labeledData[1]-inputData[1])*(labeledData[1]-inputData[1]))
	return distance

def kNN(inputData,k):
	group,labels = createDataSet()

	#use mat to calculate distance
	temp = tile(k,(len(group),1))
	distance = temp-group
	distance = distance**2
	dist = distance.sum(axis=1)
	index = argsort(dist)

	label_dict = {}
	i = 0
	while i<k:
		if label_dict.has_key(labels[index[i]]):
			label_dict[labels[index[i]]] += 1
		else:
			label_dict.setdefault(labels[index[i]],1)
		i += 1

	sortedClassCount = sorted(label_dict.iteritems(),key=operator.itemgetter(1),reverse=True)

	return sortedClassCount[0][0]

inputData = [1.0,1.1]
k=4
print kNN(inputData,k)





