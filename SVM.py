#SVM Support Vector Machines
#Classifications and performing classifications for large dimensional data
#SVM creates a Hyperplane(Linear way to

#To bring 2D data to 3D use kernal
#f(a,b) = (a, b, a^2 + b^2) via the inner product

import sklearn
from sklearn import datasets, metrics, svm

cancer = datasets.load_breast_cancer()

#print(cancer.feature_names)
#print(cancer.target_names)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)

#print(x_train)
#print(y_train)

classes = ['malignant' 'benign']

clf = svm.SVC(kernel="linear", C=2)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

acc = metrics.accuracy_score(y_test, y_pred)

print(acc)