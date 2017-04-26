import numpy as np
import neural_network as nn
import trainer as tr
#import oldStatsReader
#import pylab as plt
import os
import scipy
import datetime


'''
IF THIS FALLS TO SHIT, MAYBE TAKE THE PERCENTAGES OUT.  THEY MIGHT BE CAUSING SOMETHING FISHY IN THE CALCULATION.
'''


# Input Layer size, Hidden Layer size, lambda size
def readTrainingCsv():
    # Data sets
    #training_target = []
    TRAINING = "train_sample_III.csv"

    trainingData = np.empty([16])
    
    with open(TRAINING) as inFile:
        count = 0
        for line in inFile:
            splitLine = line.split(",")
            '''
            print splitLine
            temp = int(splitLine[len(splitLine)-1])
            print temp
            splitLine[len(splitLine)-1] = temp
            '''
            
            if count % 50000 == 0:
                print str(count) + "  training records done."
            count = count + 1
            #splitLineSplit = splitLine[:-1]
            
            #trainingData.append(splitLineSplit)
            tempNPArray = np.asarray(splitLine, dtype = float )
            #print splitLineSplit
            trainingData = np.vstack((trainingData, tempNPArray))

        # get rid of empty first row

        trainingData = trainingData[1:]
        target = trainingData[:,-1]
        trainingData = np.delete(trainingData, 15, axis=1)
        
        #print trainingData
            
        #print target
        #print len(trainingData)
        print target.shape
    print "training data done"
    return trainingData, target

    '''
    testData = []
    with open("train.csv") as inFile:
    for line in inFile:
    splitLine = line.split(",")
    testData.append(splitLine)
    
    test_set = np.asarray(testData, dtype=np.float64)
    '''

def readTestingCsv():
    TESTING = "test_sample_III.csv"
    
    testingData = np.empty([16])
    
    with open(TESTING) as inFile:
        count = 0
        for line in inFile:
            #if count > 100000:
            #    break
            count = count + 1
            splitLine = line.split(",")

            if count % 50000 == 0:
                print str(count) + "  test records done."
        
            #trainingData.append(splitLineSplit)
            tempNPArray = np.asarray(splitLine, dtype = float )
            #print splitLineSplit
            testingData = np.vstack((testingData, tempNPArray))

    # get rid of empty first row
    testingData = testingData[1:]
    target = testingData[:,-1]
    testingData = np.delete(testingData, 15, axis=1)
    
    print testingData.shape
    #print target
    #print len(trainingData)
    print target.shape

    print "testing data done"
    return testingData, target



def todo():
    for index in range(0,1):
        
            
        NN = nn.neuralNetwork(15, 30, .1)
        T = tr.trainer(NN)
        #X = np.array(([3.0,5.0],[5.0,1.0],[10.0,2.0]), dtype = float)
        #y = np.array(([75.0],[82.0], [93.0]), dtype = float)



        #!X, y = oldStatsReader.readOldStats(teams[index])#<<<<<<<
        size = X.shape[0]
        X = X/np.amax(X, axis=0) #<---- Check this value out....
        #y = y/100
        trainSize = int(.7 * size)
        testSize = int(.3 * size)

        # training matrices
        trainX = X[np.arange(testSize, size),:]
        trainY = y[np.arange(testSize, size),:]
        trainX = trainX/np.amax(trainX, axis=0)
        print trainX.shape

        # testing matrices
        testX = X[np.arange(0, testSize),:]
        testY = y[np.arange(0, testSize),:]
        testX = testX/np.amax(testX, axis=0)
        #print testX.shape

        #print 'training...'
        T.train(trainX, trainY, testX, testY)
        '''
        #plot the test vs train 
        plt.plot(T.J)
        plt.plot(T.testJ)
        plt.grid(1)
        plt.xlabel('Iterations')
        plt.ylabel('Cost')
        plt.show()
        '''
        '''
        print X.shape
        print y.shape
        print NN.W1.shape
        print NN.W2.shape
        '''
        NN.forward(X)
        #print 'first forward done. \n'
        #print '\n'
        #T.train(trainX, trainY, testX, testY)


        print teamFullNames[index] 
        if os.path.exists('gameData/'+teamFullNames[index]+'/2-25-2015.csv'):
            gameProgressionArray = np.empty([36])
            openFile = open('gameData/' + teamFullNames[index] + '/2-25-2015.csv').read()
            fileData = openFile.split('\n')
            for line in fileData:
                temp = np.fromstring(line, dtype=float, count = 36, sep=',')
                gameProgressionArray = np.vstack((gameProgressionArray, temp))
            gameProgressionArray = gameProgressionArray[1:] 

        #gameProgressionArray = gameProgressionArray[:, [0,2,3,5,6,8,9,11,12,13,14,15,16,17,18]]
            #print gameProgressionArray.shape
            #print gameProgressionArray[3]



            result = NN.forward(gameProgressionArray)
            fileOut = open('gameData/' + teamFullNames[index] + '/NN_Result.csv', 'w')
            for item in result:
                fileOut.write(str(item[0]) + ", ")
                #print item
            fileOut.close()


            #for item in result:
            #    print '%.10f' %item

            #print 'sum: ' + str (sum(result))

        '''
        plt.plot(result)
        plt.xlim(0.,150)
        plt.ylim(0.,1.0)
        plt.xlabel('iteration')
        plt.ylabel('Win Probability')
        plt.title('Dallas mavericks 2-25-2015')
        plt.grid(True)
        #plt.savefig("result" + str(j)+ "index" +str(i)+"node.png")
        plt.show()
        '''


        #END TEST BLOCK
startTime = datetime.datetime.now()
NN = nn.neuralNetwork(15, 30, .0005)
T = tr.trainer(NN)
testTime = datetime.datetime.now()

diff = testTime - startTime

trainingSet, trainingTarget = readTrainingCsv()
trainReadTime = datetime.datetime.now()
testingSet, testingTarget = readTestingCsv()
testReadTime = datetime.datetime.now()

T.train(trainingSet, trainingTarget, testingSet, testingTarget)
trainTime = datetime.datetime.now()

diff1 = trainReadTime - startTime
print "Train read time:  " + str(diff1.seconds / 60) + " minutes"

diff1 = testReadTime - trainReadTime
print "Test read time:  " + str(diff1.seconds / 60) + " minutes"

diff1 = trainTime - testReadTime
print "Train time:   " + str(diff1.seconds) + " seconds"

tp = 0
tn = 0
fp = 0
fn = 0

with open("resultsOfNN.csv", "w+") as ootFile:
    for i in range(0,30):
        j = .0001
        while j < 1:
            
            startTime = datetime.datetime.now()
            NN = nn.neuralNetwork(15, i, j)
            T = tr.trainer(NN)
            T.train(trainingSet, trainingTarget, testingSet, testingTarget)
            endTime = datetime.datetime.now()
            
            trainTime = (startTime - endTime).seconds
            ootFile.write("i = " + str(i) + " j = " + str(j) + " " + str(trainTime) + " seconds")
            
            for k in range(0,5):
                result = NN.forward(testingSet[k])
                ootFile.write(str(result) + " , " + str(testingTarget[k]))
                ootFile.write("\n")
            ootFile.write("\n")
            j = j * 5






