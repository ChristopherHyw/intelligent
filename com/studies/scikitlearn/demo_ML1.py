import numpy as np
import pandas as pd

x1 = np.random.randn(100000,2)
datas = pd.DataFrame({'x1':x1[:,0],'x2':x1[:,1],'y':x1[:,0]+x1[:,1]})
data = datas.ix[:,0:2]
label = datas.ix[:,2]

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(data,label,test_size=0.2)

# from sklearn.neural_network import MLPClassifier
# ml = MLPClassifier()
# ml.fit(X_train,Y_train)

from sklearn.linear_model import LinearRegression
mod = LinearRegression()
mod.fit(X_train,Y_train)

from sklearn.metrics import confusion_matrix
y_true = list(map(int,Y_test))
print(type(y_true))
print(y_true)
y_pred = list(map(int,mod.predict(X_test)))
print(type(y_pred))
print(y_pred)
cm = confusion_matrix(y_true,y_pred)
print(cm)
