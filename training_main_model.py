import keras as k
from keras.layers import Conv2D, MaxPooling2D, LeakyReLU
from keras.layers import Dense, Dropout, Activation, Flatten, BatchNormalization

import numpy as np
import pandas as pd
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import keras.optimizers
from tensorflow.keras import layers, regularizers
import tensorflow as tf
from keras.models import Sequential
df = pd.read_csv("data.csv")
df=df.drop(labels='name',axis=1)
df=df.drop(labels='Unnamed: 0',axis=1)
print(df)
list=df.iloc[:,-1]
convertor = LabelEncoder()

y=convertor.fit_transform(list)
print(y)
fit = StandardScaler()
npar=df.iloc[:,:-1]
print(npar)
X=fit.fit_transform((np.array(df.iloc[:,:-1], dtype=float)))

X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.30)
print(len(Y_train))
print(len(Y_test))

def trainModel(model, epochs, optimizer):
    batch_size=128
    model.compile(optimizer=optimizer,loss='sparse_categorical_crossentropy',metrics='accuracy')
    return model.fit(X_train,Y_train,validation_data=(X_test,Y_test),epochs=epochs,batch_size=batch_size)
def plotV(history):
    print("Validation Accuracy",max(history.history["val_accuracy"]))
    pd.DataFrame(history.history).plot(figsize=(12,6),)
    plt.xlabel('epoch')
    plt.show()


model = k.models.Sequential([
    k.layers.Dense(512, activation = "relu", input_shape=(X_train.shape[1],)),
    k.layers.Dropout(0.2),

    k.layers.Dense(256, activation = "relu"),
    k.layers.Dropout(0.2),

    k.layers.Dense(128, activation="relu"),
    k.layers.Dropout(0.2),

    k.layers.Dense(128, activation="relu"),
    k.layers.Dropout(0.2),

    k.layers.Dense(10, activation="softmax"),
])

opt = keras.optimizers.Adam(learning_rate=0.0001)
model_history = trainModel(model = model, epochs = 60, optimizer=opt)

print(model.summary())
preds = model.predict(X_train)
y_pred = np.argmax(preds, axis=1)
y_train1 = Y_train
print(classification_report(y_train1, y_pred)
)
print(confusion_matrix(y_train1, y_pred)
)
preds = model.predict(X_test)
y_pred = np.argmax(preds, axis=1)
y_test1 = Y_test
print(classification_report(y_test1, y_pred)
)
print(confusion_matrix(y_test1, y_pred)
)
plotV(model_history)