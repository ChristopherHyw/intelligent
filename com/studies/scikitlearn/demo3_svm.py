from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target
print(y)
# print('data shape: {0}; no.positive: {1}; no.negative: {2}'.format(X.shape,y[y==1].shape[0],y[y==0].shape[0]))

# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
#
# from sklearn.svm import SVC
#
# clf = SVC(C=1.0,kernel='rbf',gamma=0.0001)
# clf.fit(X_train,y_train)
# train_score = clf.score(X_train,y_train)
# test_score = clf.score(X_test,y_test)
# print('train score: {0}; test score: {1}'.format(train_score,test_score))
