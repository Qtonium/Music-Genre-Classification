import keras as k
from keras.layers import Dense, Dropout, Activation, Flatten, BatchNormalization

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt
from tensorflow.keras import layers, regularizers
import tensorflow as tf
from keras.models import Sequential
df = pd.read_csv("data.csv")
df=df.drop(labels='filename',axis=1)
print(df)
list=df.iloc[:,-1]
convertor = LabelEncoder()

y=convertor.fit_transform(list)

fit = StandardScaler()
npar=df.iloc[:,:-1]
print(npar)
X=fit.fit_transform((np.array(df.iloc[:,:-1], dtype=float)))

X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.33)


def KNN(X,y):
    print("KNN ------------------------------------------------------------------------")
    from sklearn.neighbors import KNeighborsClassifier

    neigh = [1, 3, 5, 7, 11, 15, 21, 25, 35, 43, 45, 67, 79, 81, 93, 105]
    for n in neigh:
        knn_cv = KNeighborsClassifier(n_neighbors=n)
        cv_scores = cross_val_score(knn_cv, X, y, cv=5, scoring='accuracy')
        print(np.mean(cv_scores), "at n = ", n)



def Logistic(X,y):
    print("Logistic with ------------------------------------------------------------------------")
    from sklearn.linear_model import LogisticRegression

    C = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10,  100]
    for c in C:
        log_cv = LogisticRegression(C=c, random_state=0, max_iter=10000, multi_class='multinomial', solver = 'lbfgs')
        cv_scores = cross_val_score(log_cv, X, y, cv=5, scoring='accuracy')
        print(np.mean(cv_scores), "at c = ", c)

KNN(X,y)
Logistic(X,y)

clf = RandomForestClassifier(
    n_estimators=100,
    criterion='gini',
    max_depth=50,
    min_samples_split=2,
    min_samples_leaf=1,
    min_weight_fraction_leaf=0.0,
    max_leaf_nodes=None,
    min_impurity_decrease=0.0,
    bootstrap=True,
    oob_score=False,
    n_jobs=-1,
    random_state=0,
    verbose=0,
    warm_start=False,
    class_weight='balanced'
)

cv_scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print(np.mean(cv_scores))





