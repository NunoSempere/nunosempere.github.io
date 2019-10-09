# Machine Learning Demystified

Several friends encouraged me to apply to a Data Scientist position at ID Insights, an organization I greatly admire, and for a position which I would be passionate about.

Unfortunately, they require Python, and I'm more of a R programmer. I decided to apply anyways, but before, I familiarized myself throrougly with numpy, pandas and sklearn, three of the most important libraries for machine learning in Python.

I used a dataset from Kaggle [Health Care Cost Analysis](https://www.kaggle.com/flagma/health-care-cost-analysys-prediction-python/data), referenced as insurance.csv thoughout the code. The reader will also have to change the variable directory to fit their needs.

Otherwise, the current files in this directory are:

- [CleaningUpData.py](https://github.com/NunoSempere/nunosempere.github.io/blob/master/maths-prog/MachineLearningDemystified/CleaningUpData.py). I couldn't work with the dataset directly, so I tweaked it somewhat.
- [AlgorithmsClassification.py](https://github.com/NunoSempere/nunosempere.github.io/blob/master/maths-prog/MachineLearningDemystified/AlgorithmsClassification.py). As a first exercise, I try to predict whether the medical bills of a particular individual are higher than the mean of the dataset. Some algorithms, like Naïve Bayes, are not really suitable for regression, but are great for predicting classes.
- [AlgorithmsRegression,py](https://github.com/NunoSempere/nunosempere.github.io/blob/master/maths-prog/MachineLearningDemystified/AlgorithmsRegression,py). I try to predict the healthcare costs of a particular individual, using all the features in the dataset.

