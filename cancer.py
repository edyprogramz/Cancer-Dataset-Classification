import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics


cancer = datasets.load_breast_cancer()
# print(cancer.feature_names)
# print(cancer.target_names)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# print(x_train, y_train)
classes = ['malignant', 'benign']

model = svm.SVC(kernel="linear")
# model = svm.SVC(kernel="poly")
model.fit(x_train, y_train)

prediction = model.predict(x_test)
accuracy = metrics.accuracy_score(y_test, prediction)
print(accuracy)
