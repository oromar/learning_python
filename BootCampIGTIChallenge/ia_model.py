import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import joblib

df = pd.read_csv('./pima-indians-diabetes.csv', header=None)

print(df.dtypes)

entradas = df.iloc[:, 0:-1]
saida = df.iloc[:, 8:]

normaliza = MinMaxScaler()
entradas_normalizadas = normaliza.fit_transform(entradas)
X_train, X_test, y_train, y_test = train_test_split(
    entradas_normalizadas, saida, test_size=0.30, random_state=42)

clf_KNN = KNeighborsClassifier(n_neighbors=5)
clf_KNN.fit(X_train, y_train)
y_pred = clf_KNN.predict(X_test)

print("KNN Score: {}".format(classification_report(y_test, y_pred)))

clf_arvore = DecisionTreeClassifier(random_state=1)
clf_arvore.fit(X_train, y_train)
y_pred = clf_arvore.predict(X_test)

print("ARVORE Score: {}".format(classification_report(y_test, y_pred)))

clf_mlp = MLPClassifier(solver='lbfgs', alpha=1e-5,
                        max_iter=2000, hidden_layer_sizes=(5, 10), random_state=1)
clf_mlp.fit(X_train, y_train)
y_pred = clf_mlp.predict(X_test)

print("MLP Score: {}".format(classification_report(y_test, y_pred)))

file_name = 'melhor_modelo.sav'
# joblib.dump(clf_mlp, file_name)
