import pandas as pd
import numpy as np
import random as rnd

import seaborn as sns
import matplotlib.pyplot as plt


from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC,LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier


train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
combine = [train_df,test_df]

#必要のない特徴量を削除
train_df = train_df.drop(['Ticket','Cabin'],axis=1)
test_df = test_df.drop(['Ticket','Cabin'],axis=1)
combine = [train_df,test_df]

#名前に着目し、グループに分ける
for dataset in combine:
	dataset['Title']=dataset.Name.str.extract('([A-Za-z]+)\.',expand=False)


for dataset in combine:
	dataset['Title']=dataset['Title'].replace(['Lady','Countess','Capt','Col','Don','Dr','Major','Rev','Sir','Jonkheer','Dona'],'Rare')
	dataset['Title']=dataset['Title'].replace('Mlle','Miss')
	dataset['Title']=dataset['Title'].replace('Ms','Miss')
	dataset['Title']=dataset['Title'].replace('Mme','Mrs')	

print(train_df[['Title', 'Survived']].groupby(['Title'], as_index=False).mean())
