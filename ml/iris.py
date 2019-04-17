from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
import pandas as pd


csv = pd.read_csv('./data/iris.csv')
cdata = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
cret = csv['Name']


trainData, testData, trainLabel, testLabel = train_test_split(cdata, cret) 

clf = svm.SVC(gamma='auto')  
clf.fit(trainData, trainLabel)
pred = clf.predict(testData)
score = metrics.accuracy_score(testLabel, pred)


