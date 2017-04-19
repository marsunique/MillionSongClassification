Obviously need some preprocessing

LassoCV(alphas=None, copy_X=True, cv=None, eps=0.001, fit_intercept=True,
    max_iter=1000, n_alphas=100, n_jobs=1, normalize=False, positive=False,
    precompute='auto', random_state=None, selection='cyclic', tol=0.0001,
    verbose=False)
0.00538659641752
[0.0064310633110783453, 0.0052268509281643283, 0.0052112503886134753, 0.005561912648078593, 0.0045019048116804461]


GaussianNB(priors=None)
0.992801999806
[0.99277441659464127, 0.99279170267934314, 0.99306816021020239, 0.99296444190910815, 0.99241127763660564]

NORMAL INPUT
GaussianNB(priors=None)
[{'tn': 57417, 'fp': 0, 'fn': 433, 'tp': 0}, {'tn': 57425, 'fp': 0, 'fn': 425, 'tp': 0}, {'tn': 57424, 'fp': 0, 'fn': 425, 'tp': 0}, {'tn': 57462, 'fp': 0, 'fn': 387, 'tp': 0}, {'tn': 57437, 'fp': 0, 'fn': 412, 'tp': 0}]

UNDERSAMPLING
GaussianNB(priors=None)
[{'tn': 26608, 'fp': 30843, 'fn': 183, 'tp': 216}, {'tn': 26186, 'fp': 31258, 'fn': 195, 'tp': 211}, {'tn': 26958, 'fp': 30483, 'fn': 176, 'tp': 232}, {'tn': 27229, 'fp': 30212, 'fn': 199, 'tp': 209}, {'tn': 25819, 'fp': 31569, 'fn': 180, 'tp': 281}]
LassoCV(alphas=None, copy_X=True, cv=None, eps=0.001, fit_intercept=True,
    max_iter=1000, n_alphas=100, n_jobs=1, normalize=False, positive=False,
    precompute='auto', random_state=None, selection='cyclic', tol=0.0001,
    verbose=False)
[{'tn': 0, 'fp': 0, 'fn': 57850, 'tp': 0}, {'tn': 0, 'fp': 0, 'fn': 57850, 'tp': 0}, {'tn': 0, 'fp': 0, 'fn': 57849, 'tp': 0}, {'tn': 0, 'fp': 0, 'fn': 57849, 'tp': 0}, {'tn': 0, 'fp': 0, 'fn': 57849, 'tp': 0}]
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
[{'tn': 0, 'fp': 57412, 'fn': 0, 'tp': 438}, {'tn': 0, 'fp': 57461, 'fn': 0, 'tp': 389}, {'tn': 0, 'fp': 57433, 'fn': 0, 'tp': 416}, {'tn': 0, 'fp': 57414, 'fn': 0, 'tp': 435}, {'tn': 0, 'fp': 57445, 'fn': 0, 'tp': 404}]
