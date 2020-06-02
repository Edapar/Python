"""Linear Regression
Looks at the scatter of data points and look for the best fit line to the data
When not good to use: Randomized data
When good to use: Strong correlation"""

import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pylab as pyplot
import pickle
from matplotlib import style


#load data via pandas
data = pd.read_csv("student-mat.csv", sep=";")

#print data to see the attributes associated
print(data.head())

#determing attributes wanted to test
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

#predicting final grade
predict = "G3"

#attributes == column catagory
#labels == what you're looking for

#set attribute
X = np.array(data.drop([predict], 1))
Y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

"""
#Find Best Model and Save It
best = 0
for n in range(10000):
    #Spit into four different arrays, _test are to test accuracy of the model to data
    #split test data to 10% of actual data to see accuracy of before and after test data.
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)
 
    #Code best fit line
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)

    #Print out accuracy of test
    acc = linear.score(x_test, y_test)
    print(acc)

    #Saving model inside of Pickle
    #Pickling is for serializing and de-serializing (Marshalling or flattening)
    #python object structures.
    #Serializing = process of converting an object in memory to a byte stream that can be 
    #stored on disk
    #Pickling != compression
    #Good for: Storing Python Objects in Data Base
    #Not good for: Data across different programming languages
    if acc > best:
        best = acc
        with open("studentmodel.pickle", "wb") as f: #wb = write binary
            pickle.dump(linear, f)

print(best)
"""

pickle_in = open("studentmodel.pickle", "rb") #rb = read binary
linear = pickle.load(pickle_in)

#print Coefficient
print("Co: \n", linear.coef_)
#print Intercept
print("Intercept: \n", linear.intercept_)

"""Use data to predict the data on a real student
Print out all predictions and show what the input data was for that prediction"""
predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

#graphing correlations
p = 'absences'
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()

