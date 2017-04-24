from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
from sklearn.linear_model import LassoCV
from random import shuffle

def classificationBig(fpath, d, splits=5):
    """
    Basic classification with 5-fold cross-validation
    """
    kf = KFold(n_splits=splits, shuffle=True)
    XX, yy = readInput(fpath+d+".txt")
    
    lassocv = LassoCV()
    svm = SVC()
    nb = GaussianNB()
    
    methods = [svm, nb, lassocv]
    results = {m.__class__.__name__:[] for m in methods}
    
    for train_index, test_index in kf.split(XX):
        training, tests = [XX[i] for i in train_index], [XX[j] for j in test_index]
        classes, actuals = [yy[i] for i in train_index], [yy[j] for j in test_index]

        training, classes = undersampling(training, classes)

        
        # LASSO Regression
        print("lasso")
        lassocv.fit(training, classes)
        
        #Support Vector Machines
        print("svm")
        svm.fit(training, classes)
  
        # Naive Bayes
        print("nb")
        nb.fit(training, classes)
        
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

def outlierDetection(fpath, d, splits=10):
    """ Outlier Detection.  This uses One-Class SVM and Isolation Forest techniques in the sklearn library.
    """
      kf = KFold(n_splits=splits, shuffle=True)
      XX, yy = readInput(fpath+d+".txt")
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
            
            start_time = timeit.default_timer()
            ocs = OneClassSVM()
            ocs.fit(training)
            elapsed = timeit.default_timer() - start_time
            print('classification time' + str(elapsed))
            
            start_time = timeit.default_timer()
            ocsOut = ocs.predict(tests)
            elapsed = timeit.default_timer() - start_time
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
      
fpath = './musicFiles/'
file = 'millionSongString'
#outlierDetection(fpath, file)
classificationBig(fpath, file)
