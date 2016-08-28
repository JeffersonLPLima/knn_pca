 
import csv
import random
import math
import operator
 

def euclideanDistance(instance1, instance2, length):
        distance = 0
        for x in range(length):
                distance += pow((float(instance1[x]) - float(instance2[x])), 2)
        return math.sqrt(distance)
 
def getNeighbors(trainingSet, testInstance, k):
        distances = []
        length = len(testInstance)-1
        for x in range(len(trainingSet)):
                dist = euclideanDistance(testInstance, trainingSet[x], length)
                distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for x in range(k):
                neighbors.append(distances[x][0])
        return neighbors
 
def getResponse(neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
                response = neighbors[x][-1]
                if response in classVotes:
                        classVotes[response] += 1
                else:
                        classVotes[response] = 1
        sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]
 
def getAccuracy(testSet, predictions):
        correct = 0
        for x in range(len(testSet)):
                if testSet[x][-1] == predictions[x]:
                        correct += 1
        return (correct/float(len(testSet))) * 100.0

def main():
        
        dataSetS=[]
        dataSetVi=[]
        dataSetVe=[]
        
        with open('setosa_data', 'rb') as csvfile:
            lines = csv.reader(csvfile)
            dataset1 = list(lines)
            for x in range(len(dataset1)):
                dataSetS.append(dataset1[x])
        with open('virginica_data', 'rb') as csvfile2:
            lines = csv.reader(csvfile2)
            dataset1 = list(lines)
            for x in range(len(dataset1)):
                dataSetVi.append(dataset1[x])

        with open('versicolor_data', 'rb') as csvfile2:
            lines = csv.reader(csvfile2)
            dataset1 = list(lines)
            for x in range(len(dataset1)):
                dataSetVe.append(dataset1[x])

        for x in range(len(dataSetS)):
                for y in range(2):
                    dataSetVe[x][y] = float(dataSetVe[x][y])
                    dataSetS[x][y] = float(dataSetS[x][y])
                    dataSetVi[x][y] = float(dataSetVi[x][y])

                del dataSetVe[x][1]
                del dataSetS[x][1]
                del dataSetVi[x][1]
                del dataSetVe[x][2]
                del dataSetS[x][2]
                del dataSetVi[x][2]
                    
                        
        for x in range(len(dataSetS)):
                 print dataSetS[x]   
        print 'set: ' + repr(len(dataSetS))
        print 'set: ' + repr(len(dataSetVi))
        print 'set: ' + repr(len(dataSetVe))
        
        taxa=0
        for i in range (10):
            training=[]
            test=[]
      
            for x in range(len(dataSetS)):
                   if((x>=(5*i)) & (x<(5*(i+1)))):
                       test.append(dataSetS[x])
                       test.append(dataSetVi[x])
                       test.append(dataSetVe[x])
                   else:
                       training.append(dataSetS[x])
                       training.append(dataSetVi[x])
                       training.append(dataSetVe[x])
                       
        #    print len(test)
         #   print len(training)
            # generate predictions
            predictions=[]
            k = 1
            for x in range(len(test)):
                    neighbors = getNeighbors(training, test[x], k)
                    result = getResponse(neighbors)
                    predictions.append(result)
                    #print('> predicted=' + repr(result) + ', actual=' + repr(test[x][-1]))
            accuracy = getAccuracy(test, predictions)
            taxa+=accuracy
            print("fold"+str(i)+'    Accuracy:' + repr(accuracy) + '%')
        print taxa/10
main()


