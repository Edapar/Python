#K(integer) Nearest Neighbors, k is best prime or odd
#Nearest Neighbor (only 1 neighbor)
#Good for: Irregular Data

import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

#loading data into python
data = pd.read_csv("car.data")
#print(data.head())

#transform non-numerical data into numerical data then storing into lists
#make sure to give it list value instead of np.array or pandas data frame
le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

predict = "class"

#zip() put all different features into one list
#Creates a bunch of tuple objects with all corresponding values with list we give it
#Tuples is a collection of python obj seprated by commas
#Similar to: Indexing, Nesting Objects, and Repetition
#Tuple == immutable

X = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

model = KNeighborsClassifier(n_neighbors=7)
model.fit(x_train, y_train)
acc = model.score(x_test, y_test)

print(acc)

predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]

for x in range(len(x_test)):
    print("Predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])

    #testing Kneighbors(R^2 array, number of neighbors,
    n = model.kneighbors([x_test[x]], 7, True)
    print("N: ", n)
