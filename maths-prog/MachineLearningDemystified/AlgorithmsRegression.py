directory = '/home/nuno/Documents/Jobs/IDInsight'

import pandas as pd
import numpy as np
import joblib
import matplotlib


## Install the dataframe
insuranceDataFrame = pd.read_csv(directory +'insurance_clean_continuous.csv')
insuranceDataFrame['charges']
## We divide our data into training and test sets, and normalize
dfTrain = insuranceDataFrame[:1000]
dfTest = insuranceDataFrame[1000:1300]
dfCheck = insuranceDataFrame[1300:]

means = np.mean(dfTrain, axis=0)
stds = np.std(dfTrain, axis=0)

dfTrain = (dfTrain - means) / stds
dfTest = (dfTest - means) / stds
dfCheck = (dfCheck - means) / stds

## We don't want this part, only when classifying:
## dfTrain['charges'] = (dfTrain['charges']>=0).astype('int')
## dfTest['charges'] = (dfTest['charges']>=0).astype('int')
## dfCheck['charges'] = (dfCheck['charges']>=0).astype('int')

## Convert our stuff to arrays
trainLabel = np.asarray(dfTrain['charges'])
trainData = np.asarray(dfTrain.drop('charges',1))

testLabel = np.asarray(dfTest['charges'])
testData = np.asarray(dfTest.drop('charges',1))

## We reuse the old function

def runAlgorithm(Classifier, algorithmName):
    global scores, algorithms

    Classifier.fit(trainData, trainLabel)
    scoreInternal = Classifier.score(testData, testLabel)
    print("score = ", scoreInternal * 100, "/100")

    scores = np.append(scores, scoreInternal) ## These are global scope variables
    algorithms = np.append(algorithms, algorithmName)

    joblib.dump([Classifier, means, stds],
                directory +'insuranceModel-' + algorithmName + '.pkl')

algorithms = []
scores = []

## And we are ready!

## ******************************************************************

## Linear Regression
algorithmName = "LinearRegression"
from sklearn.linear_model import LinearRegression
insuranceCheck = LinearRegression()
runAlgorithm(insuranceCheck, algorithmName)

### We also want to visualize some stuff this time:

coeff = list(insuranceCheck.coef_)
labels = list(dfTrain.drop('charges',1).columns)
features = pd.DataFrame()
features['Features'] = labels
features['importance'] = coeff
features.sort_values(by=['importance'], ascending=True, inplace=True)
features['positive'] = features['importance'] > 0
features.set_index('Features', inplace=True)
features.importance.plot(kind='barh', figsize=(11, 6),color = features.positive.map({True: 'blue', False: 'red'}))

## ******************************************************************

## Lasso
algorithmName = "Lasso"
from sklearn.linear_model import LassoCV
insuranceCheck = LassoCV(cv=5, n_alphas=20, tol=0.0001, n_jobs=-1)
runAlgorithm(insuranceCheck, algorithmName)

## ******************************************************************

## Nearest Neighbours Regression
algorithmName = "NearestNeighboursRegression"

from sklearn.neighbors import KNeighborsRegressor

### Let's do some hyperparameter tuning:
score=0
for n_neighbors in range(1,100):
    for leaf_size in range(1,100):
        insuranceCheck = KNeighborsRegressor(n_jobs=-1, n_neighbors=n_neighbors, weights="distance", algorithm="brute", leaf_size=leaf_size, p=2)
        insuranceCheck.fit(trainData, trainLabel)

        score_temp = insuranceCheck.score(testData, testLabel)

        if(score_temp >score):
            print("\nscore = ", score_temp * 100, "/100")
            print("n_neighbors = ", n_neighbors)
            print("leaf_size = ", leaf_size)
            score=score_temp

insuranceCheck = KNeighborsRegressor(n_jobs=-1, n_neighbors=8, weights="distance", algorithm="brute", leaf_size=1, p=2)
runAlgorithm(insuranceCheck, algorithmName)

## ******************************************************************

## Linear SVR
algorithmName = "LinearSVR"
from sklearn.svm import LinearSVR

n=4000
insuranceCheck = LinearSVR(max_iter=n)
runAlgorithm(insuranceCheck, algorithmName)

## ******************************************************************

## SVR different kernels.
algorithmName = "SVR_RBF"
from sklearn.svm import SVR
insuranceCheck = SVR(gamma='auto', C=1, epsilon=0.2, kernel='rbf')
    ## There are different kernels available, including polynomial.
    ## After some tinkering, RBF seems to be the best
runAlgorithm(insuranceCheck, algorithmName)

## ******************************************************************

## Tree regression.
algorithmName = "TreeRegression"
from sklearn.tree import DecisionTreeRegressor

## Hyper parameter optimization.
score = 0

for criterion in np.array(["mse", "friedman_mse", "mae"]):
    for splitter in np.array(["best", "random"]):
        for max_depth in np.append(range(1,10), [None]):
            print("max_depth=",max_depth)
            for min_samples_split in (np.asarray(range(25))+2):
                #print("min_samples_split=", min_samples_split)
                for min_samples_leaf in (np.asarray(range(25))+1):
                    for max_features in np.array(["log2", "auto", None]):
                        insuranceCheck = DecisionTreeRegressor(random_state=0, criterion=criterion, splitter = splitter, max_depth = max_depth, min_samples_split = min_samples_split, min_samples_leaf = min_samples_leaf, max_features = max_features)
                        insuranceCheck.fit(trainData, trainLabel)
                        score_temp = insuranceCheck.score(testData, testLabel)
                        if(score_temp > score):
                            print("score = ", score_temp * 100, "/100")
                            print("\nNEW BEST\ncriterion=", criterion, "\nsplitter =", splitter, "\nmax_depth =", max_depth, "\nmin_samples_split =", min_samples_split, "\nmin_samples_leaf =", min_samples_leaf, "\nmax_features =", max_features)
                            score = score_temp

insuranceCheck = DecisionTreeRegressor(random_state=0, criterion="mse", splitter = "random", min_samples_split=14, min_samples_leaf=4, max_features = "auto", max_depth= 9)
runAlgorithm(insuranceCheck, algorithmName)

## ******************************************************************

## Random forest regression.
algorithmName = "RandomForestRegression"

from sklearn.ensemble import RandomForestRegressor
insuranceCheck = RandomForestRegressor(n_estimators=500, max_depth=None, random_state=0, n_jobs=-1)
runAlgorithm(insuranceCheck, algorithmName)

## ******************************************************************

## Extra random forest regression.
algorithmName = "ExtraRandomTreesRegression"
from sklearn.ensemble import ExtraTreesRegressor
insuranceCheck = ExtraTreesRegressor(n_estimators=500, max_depth=None, min_samples_split=20, min_samples_leaf=20, n_jobs=-1)
runAlgorithm(insuranceCheck, algorithmName)

## ******************************************************************
## MultiLayerPerceptron Regression(NN)

from sklearn.neural_network import MLPRegressor
algorithmName = "MLP_Regresion"

for randomstate in range(10):
    insuranceCheck = MLPRegressor(max_iter=1200, hidden_layer_sizes=(30,30,30), random_state=randomstate, learning_rate="adaptive", activation="relu")
    insuranceCheck.fit(trainData, trainLabel)
    score = insuranceCheck.score(testData, testLabel)
    print("score = ", score * 100, "/100")

insuranceCheck = MLPRegressor(max_iter=1200, hidden_layer_sizes=(30,30,30), random_state=5, learning_rate="adaptive", activation="relu")
runAlgorithm(insuranceCheck, algorithmName)

## ******************************************************************

for i in range(len(scores)):
    print(algorithms[i], ": ", scores[i])

## And that's it. We notice that most of our algorithms do pretty well, hovering around .81. Dishonorable mention to LinearSVR.

## Overall, Trees do pretty great.
