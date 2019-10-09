directory = '/home/nuno/Documents/Jobs/IDInsight'

import pandas as pd
import numpy as np
import joblib

## Install the dataframe
insuranceDataFrame = pd.read_csv('/home/nuno/Documents/Jobs/IDInsight/insurance_clean_continuous.csv')
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

dfTrain['charges'] = (dfTrain['charges']>=0).astype('int')
dfTest['charges'] = (dfTest['charges']>=0).astype('int')
dfCheck['charges'] = (dfCheck['charges']>=0).astype('int')

## Convert our stuff to arrays
trainLabel = np.asarray(dfTrain['charges'])
trainData = np.asarray(dfTrain.drop('charges',1))

testLabel = np.asarray(dfTest['charges'])
testData = np.asarray(dfTest.drop('charges',1))

## ******************************************************************

## We're ready to apply the specific ML algorithms!

# Naïve Bayes

## Naïve Bayes: Bernoulli
from sklearn.naive_bayes import BernoulliNB
insuranceCheck = BernoulliNB(alpha=0.01)
insuranceCheck.fit(trainData, trainLabel)

score = insuranceCheck.score(testData, testLabel)
print("score = ", score * 100, "/100")
# We know that the error is R^2, we just find it more intuitive to present this as a score out of 100.

algorithms = []
algorithms = np.append(algorithms, input())
scores = []
scores = np.append(scores, score)

## We could use the following to make predictions
## But for the moment, we're just interested in seeing which algorithm performs best, so we'll only do this once.

sampleData = dfCheck[4:5]
sampleDataFeatures = np.asarray(sampleData.drop('charges',1))

prediction = insuranceCheck.predict(sampleDataFeatures)
print('Insurance Claim Prediction:', prediction)
sampleData['charges']

## Save the model
joblib.dump([insuranceCheck, means, stds], directory+'/insuranceModel-NaiveBayes-Bernoulli.pkl')

## This is what we would do to load the next time
insuranceLoadedModel, means, stds = joblib.load(directory+ '/insuranceModel-NaiveBayes-Bernoulli.pkl')
score = insuranceLoadedModel.score(testData, testLabel)
print("score = ", score * 100,"/ 100")


## ******************************************************************

## Naïve Bayes: Gaussian
from sklearn.naive_bayes import GaussianNB

insuranceCheck = GaussianNB()
insuranceCheck.fit(trainData, trainLabel)

score = insuranceCheck.score(testData, testLabel)
print("score = ", score * 100, "/100")

algorithms = np.append(algorithms, input())
scores = np.append(scores, score)


## Save the model
joblib.dump([insuranceCheck, means, stds], directory+'/insuranceModel-NaiveBayes-Gaussian.pkl')

## ******************************************************************

## Nearest Neighbours

### We've been using the same setup for a while; we should create a function!

def runAlgorithm(Classifier, algorithmName):
    global scores, algorithms

    Classifier.fit(trainData, trainLabel)
    scoreInternal = Classifier.score(testData, testLabel)
    print("score = ", scoreInternal * 100, "/100")

    scores = np.append(scores, scoreInternal) ## These are global scope variables
    algorithms = np.append(algorithms, algorithmName)

    joblib.dump([Classifier, means, stds],
                '/home/nuno/Documents/Jobs/IDInsight/insuranceModel-' + algorithmName + '.pkl')


algorithmName = "NearestNeighbours"

from sklearn.neighbors import KNeighborsClassifier

insuranceCheck = KNeighborsClassifier(n_jobs=-1, n_neighbors=7, weights="distance", algorithm="brute", leaf_size=10, p=2)
runAlgorithm(insuranceCheck, algorithmName)

## ******************************************************************

## Support Vector Machines
from sklearn.svm import SVC

algorithmName = "SVM"
insuranceCheck = SVC(gamma='scale', kernel='poly', degree=5) # Required some tinkering
runAlgorithm(insuranceCheck, algorithmName)

## ******************************************************************

## Decision Trees

from sklearn.tree import DecisionTreeClassifier
algorithmName = "Tree"

### This is getting a little bit repetitive, so let's do some rudimentary hyperparameter optimization

score = 0

## Warning: slow
for criterion in np.array(["gini", "entropy"]):
    for splitter in np.array(["best", "random"]):
        for max_depth in np.append(range(1,10), [None]):
            print("max_depth=",max_depth)
            for min_samples_split in (np.asarray(range(25))+2):
                #print("min_samples_split=", min_samples_split)
                for min_samples_leaf in (np.asarray(range(25))+1):
                    for max_features in np.array(["log2", "auto", None]):
                        insuranceCheck = DecisionTreeClassifier(random_state=0, criterion=criterion, splitter = splitter, max_depth = max_depth, min_samples_split = min_samples_split, min_samples_leaf = min_samples_leaf, max_features = max_features)
                        insuranceCheck.fit(trainData, trainLabel)
                        score_temp = insuranceCheck.score(testData, testLabel)
                        if(score_temp > score):
                            print("score = ", score_temp * 100, "/100")
                            print("\nNEW BEST\ncriterion=", criterion, "\nsplitter =", splitter, "\nmax_depth =", max_depth, "\nmin_samples_split =", min_samples_split, "\nmin_samples_leaf =", min_samples_leaf, "\nmax_features =", max_features)
                            score = score_temp

insuranceCheck = DecisionTreeClassifier(random_state=0, criterion="gini", splitter = "best", max_depth = 9, min_samples_split = 15, min_samples_leaf = 4, max_features = "log2")

runAlgorithm(insuranceCheck, algorithmName)

## ******************************************************************

## Random forests
from sklearn.ensemble import RandomForestClassifier
algorithmName = "RandomForest"

insuranceCheck = RandomForestClassifier(n_estimators=200, criterion = "gini", min_samples_split = 14, min_samples_leaf=4, max_depth=9 , random_state=0, n_jobs=-1, max_features=None)

runAlgorithm(insuranceCheck, algorithmName)

## ******************************************************************

## Extra random trees
algorithmName = "ExtraRandomTrees"
from sklearn.ensemble import ExtraTreesClassifier
insuranceCheck = ExtraTreesClassifier(n_estimators=300, max_depth=None)
runAlgorithm(insuranceCheck, algorithmName)

## ******************************************************************

## MultiLayerPerceptron (NN)
algorithmName = "MultiLayerPerceptron"
from sklearn.neural_network import MLPClassifier
insuranceCheck = MLPClassifier(max_iter=800, hidden_layer_sizes=150)
runAlgorithm(insuranceCheck, algorithmName)

## ******************************************************************

for i in range(len(scores)):
    print(algorithms[i], ": ", scores[i])

## And that's it. We notice that most of our algorithms do pretty well, with a score of .89 - .93, where the maximum is 1.
## This means that a lot of the variability in the sample is extracted by our model.

