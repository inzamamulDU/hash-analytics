#import modules
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score

#Read file
df = pd.read_csv("Iris.csv", index_col = 'Id')

#Renaming axis to nan
df=df.rename_axis('')

#select features attribute
X=df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]

#Select target
Y = df[['Species']]

#encoding the target using dummies
y = pd.get_dummies(Y)

#spitting train = 70 % and test = 30% in size
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size =0.7, test_size = 0.3, random_state=1)

#Decision Tree Classifire
DC = DecisionTreeClassifier(criterion = "entropy", max_depth=10, random_state=50, max_features=4, min_samples_leaf=8)
DC.fit(X_train, y_train)

#Predict the test
y_pred = DC.predict(X_test)

#show the accuraccy
train_accuracy = accuracy_score(y_train, DC.predict(X_train))
test_accuracy = accuracy_score(y_test, y_pred)
print('Train Accuracy:', train_accuracy)
print('Test Accuracy:',test_accuracy)
print('-----------------------------------------')
print('Confusion Matrix')
print('-----------------------------------------')
print(confusion_matrix(y_test.values.argmax(axis=1), y_pred.argmax(axis=1)))
print('-----------------------------------------')
print('classification_report')
print('-----------------------------------------')
print(classification_report(y_test.values.argmax(axis=1), y_pred.argmax(axis=1)))
