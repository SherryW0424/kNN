from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

def getDistance(labeledData,inputData):
	distance = sqrt((labeledData[0]-inputData[0])*(labeledData[0]-inputData[0])+(labeledData[1]-inputData[1])*(labeledData[1]-inputData[1]))
	return distance

def kNN(inputData,k):
	group,labels = createDataSet()
	dist = []
	label_dict ={}
	for tData in group:
		dist.append(getDistance(tData,inputData))
	index = argsort(dist)
	i = 0
	while i<k:
		if label_dict.has_key(labels[index[i]]):
			label_dict[labels[index[i]]] += 1
		else:
			label_dict.setdefault(labels[index[i]],1)
		i += 1
	max_count = 0
	for key,values in label_dict.items():
		if values>max_count:
			label = key
			max_count = values

	return label

inputData = [1.0,1.1]
k=2
print kNN(inputData,k)





