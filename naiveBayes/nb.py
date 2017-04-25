from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
from sklearn.linear_model import LassoCV
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest
from random import shuffle
from timeit import default_timer
from math import isnan

def readInput(file):
      """This file is for reading in my formatted input
      INPUT:    filename
      OUTPUT:   t1 - list containing features
                t2 - list containing class labels which correspond to respective features lists in t1
      """
      #scriptDir = os.path.dirname(__file__)
      #with open(os.path.join(scriptDir, file), 'r') as temp_file:
      with open(file) as temp_file:
            temp_file.readline()
            data = []
            temp_file.readline() # this shouldn't be needed, but an extra blank line was added at beginning by my data conversion
            for cin in temp_file:
                  try:
                        tmp = [float(r) for r in cin.strip('\n').strip().split(',')]
                        data.append(tmp)
                  except:
                        tmp = [r for r in cin.strip("\n").strip().split(',')]
                        if tmp[-1] == 'no':
                              tmp[-1] = 0
                        if isinstance(tmp[-1], str):
                              if tmp[-1].strip() == 'yes':
                                    tmp[-1] = 1
                        data.append([float(r) for r in tmp])


      #split data into features and classes
      t1, t2=[], []
      
      maxs = [-100 for _ in data[0]]
      for k in data:
            for j in range(len(k)):
                  if k[j] > maxs[j]:
                        maxs[j] = deepcopy(k[j])
      
      # check for NaNs that got through preprocessing
      for k in range(len(data)):
            for j in range(len(data[k])):
                  if isnan(data[k][j]):
                        data[k][j] = maxs[j]*10
            t1.append(data[k][:-1])
            t2.append(data[k][-1])

      return t1, t2


def classificationBig(fpath, d, splits=5, times=1, testing=False, under=False):
    """
    Basic classification with 5-fold cross-validation
    """
    kf = KFold(n_splits=splits, shuffle=True)
    # Use smaller dataset for testing (10,000 picked by dataset creators as representative number)
    XX, yy = readInput(fpath+d+".txt") if not testing else readInput(fpath+d+".txt")[:10000]
    
    
    lassocv = LassoCV()
    svm = SVC()
    nb = GaussianNB()
    
    #methods = [svm, nb, lassocv]
    methods = [nb, svm]
    results = {m.__class__.__name__:[] for m in methods}
    
    for train_index, test_index in kf.split(XX):
        training, tests = [XX[i] for i in train_index], [XX[j] for j in test_index]
        classes, actuals = [yy[i] for i in train_index], [yy[j] for j in test_index]

        if under:
            training, classes = undersampling(training, classes, times)

        
        # LASSO Regression
        #print("lasso")
        #lassocv.fit(training, classes)
        
        # Support Vector Machines
        print("svm")
        svm.fit(training, classes)
  
        # Naive Bayes
        print("nb")
        nb.fit(training, classes)
        
        
        """
        # use this one for lasso
        start_time = default_timer()
        for m in methods:
            tmp = {'tp':0, 'tn':0, 'fp':0, 'fn':0}
            for t in range(len(tests)):
                pred = m.predict(tests[t])
                if 1 == actuals[t]:
                    if pred > 0.5:
                        tmp['tp'] += 1
                    else:
                        tmp['fn'] += 1
                else:
                    if pred >= 0.5:
                        tmp['fp'] += 1
                    else:
                        tmp['tn'] += 1
            results[m.__class__.__name__].append(tmp)
        """
        for m in methods:
            tmp = {'tp':0, 'tn':0, 'fp':0, 'fn':0}
            for t in range(len(tests)):
                pred = m.predict(tests[t])
                if pred == actuals[t]:
                    if pred == 1:
                        tmp['tp'] += 1
                    else:
                        tmp['tn'] += 1
                else:
                    if pred == 1:
                        tmp['fp'] += 1
                    else:
                        tmp['fn'] += 1
            results[m.__class__.__name__].append(tmp)
            #results[m.__class__.__name__].append(m.score(tests, actuals))
        
            
            
      
    for m in methods:
        print(m)
        #print(avg(results[m.__class__.__name__]))
        print(results[m.__class__.__name__])
        print("\n")


def undersampling(biased, answers, times=1):
      tmp, tmp1, tmp2, first, second, ans = [], [], [], [], [], []
      for k in range(len(biased)):
            if answers[k] == 0:
                  tmp1.append(biased[k])
                  first.append(k)
            else:
                  tmp2.append(biased[k])
                  second.append(k)
      shuffle(tmp1)
      shuffle(tmp2)
      for k in range(len(second)):
            tmp.append(tmp1[k])
            ans.append(answers[first[k]])
            tmp.append(tmp2[k])
            ans.append(answers[second[k]])
      for k in range(len(second)*(times-1)):
            tmp.append(tmp1[k+len(second)])
            ans.append(answers[first[k+len(second)]])
      return tmp, ans    

def outlierDetection(fpath, d, splits=10, testing=False):
    """ Outlier Detection.  This uses One-Class SVM and Isolation Forest techniques in the sklearn library.
    """
    kf = KFold(n_splits=splits, shuffle=True)
    XX, yy = readInput(fpath+d+".txt") if not testing else readInput(fpath+d+".txt")[:10000]
    results = {'tp':0, 'fp':0, 'tn':0, 'fn':0}
    totesFeatures = []
    totesClasses = []

    for train_index, test_index in kf.split(XX):
        print("start")
        training, tests = [XX[i] for i in train_index], [XX[j] for j in test_index]
        classes, actuals = [yy[i] for i in train_index], [yy[j] for j in test_index]
        
        # Isolation Forest ran out of memory during all experimental runs on the full dataset
        # Random (Isolation) Forest
        #isoFor = IsolationForest()
        #isoFor.fit(training)
        #isoForOut = isoFor.predict(training if testing is None else testing)
        #isoForOut = isoFor.predict(training)
        #isoForTest = isoFor.predict(tests)
        
        start_time = default_timer()
        ocs = OneClassSVM()
        ocs.fit(training)
        elapsed = default_timer() - start_time
        print('classification time' + str(elapsed))
        
        start_time = default_timer()
        ocsOut = ocs.predict(tests)
        elapsed = default_timer() - start_time
        print('prediction time' + str(elapsed))
        print("done classifying")
        
        normal = [i for i,x in enumerate(ocsOut) if x == 1]
        outlier = [i for i,x in enumerate(ocsOut) if x == -1]
        print("Normal " + str(len(normal)))
        print("Outlier " + str(len(outlier)))
        
        for t in range(len(ocsOut)):
            if 1 == actuals[t]:
                if ocsOut[t] == -1: # 1 is the minority class in the data, outlier predicts -1 for outlier
                    results['tp'] += 1
                else:
                    results['fn'] += 1
            else:
                if ocsOut[t] != -1:
                    results['tn'] += 1
                else:
                    results['fp'] += 1
    
    print(results)
      
fpath = './'
file = 'millionSongString'
#file = 'millionSongs3'
outlierDetection(fpath, file)
classificationBig(fpath, file, testing=True, under=True)
