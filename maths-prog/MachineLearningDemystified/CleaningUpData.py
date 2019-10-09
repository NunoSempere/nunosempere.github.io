directory = '/home/nuno/Documents/Jobs/IDInsight'

import pandas as pd
import numpy as np

## Install the dataframe
insuranceDataFrame = pd.read_csv(directory + '/insurance.csv')

## Some functions for cleaning up, inspired by R's ifelse function

def ifelse1(x, listOfChecks, yesLabel, noLabel):
    if x in listOfChecks:
        return (yesLabel)
    else:
        return (noLabel)

def ifelse2(x,listOfChecks, listOfLabels):
    n = len(listOfChecks)
    for i in range(n):
        if x == listOfChecks[i]:
            return (listOfLabels[i])
    return None

insuranceDataFrame['sex_numeric'] =insuranceDataFrame['sex'].apply(lambda x: ifelse1(x, np.array(['male']),1,0))

insuranceDataFrame['smoker_numeric'] =insuranceDataFrame['smoker'].apply(lambda x: ifelse1(x, np.array(['yes']),1,0))

insuranceDataFrame['region_numeric'] =insuranceDataFrame['region'].apply(lambda x: ifelse2(x, np.unique(insuranceDataFrame['region']), np.array([0,1,2,3])))

insuranceDataFrame = insuranceDataFrame.drop(["sex", "smoker", "region"],axis=1)

## We save the database

insuranceDataFrame.to_csv(directory +'insurance_clean_continuous.csv', index=False)


