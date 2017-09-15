#cd e:/document/ids/data sets

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
#1
processed = pd.read_csv("./processed.csv")
processed_noid = processed.drop(["PassengerId"],axis=1)
processed_noid.describe()
average_joe = np.array([int(processed_noid["Survived"].mode()),
                        int(processed_noid["Pclass"].mode()),
                        int(processed_noid["Sex"].mode()),
                        processed_noid["Age"].mean(),
                        int(processed_noid["SibSp"].mode()),
                        int(processed_noid["Parch"].mode()),
                        processed_noid["Fare"].mean(),
                        int(processed_noid["Embarked"].mode()),
                        int(processed_noid["Deck"].mode())])

survived = processed_noid[processed_noid["Survived"]==1]
survived_jane = np.array([1,int(survived["Pclass"].mode()),
                        int(survived["Sex"].mode()),
                        int(survived["Age"].mean()),
                        int(survived["SibSp"].mean()),
                        int(survived["Parch"].mean()),
                        survived["Fare"].mean(),
                        int(survived["Embarked"].mode()),
                        int(survived["Deck"].mode())])

dead = processed_noid[processed_noid["Survived"]==0]
dead_joe = np.array([0,int(dead["Pclass"].mode()),
                        int(dead["Sex"].mode()),
                        int(dead["Age"].mean()),
                        int(dead["SibSp"].mean()),
                        int(dead["Parch"].mean()),
                        dead["Fare"].mean(),
                        int(dead["Embarked"].mode()),
                        int(dead["Deck"].mode())]);

survived_similarity = np.square(np.array(survived)-survived_jane).sum(1)
dead_similarity = np.square(np.array(dead)-dead_joe).sum(1)
np.array(survived)[survived_similarity.argmin()]
survived_jane
np.array(dead)[dead_similarity.argmin()]
dead_joe

sns.countplot(survived["Sex"])
sns.countplot(dead["Sex"])

sns.distplot(survived["Age"],hist=False)
sns.distplot(dead["Age"],hist=False)

with plt.style("default"):
	plt.plot(np.array(survived["Age"]),np.array(survived["SibSp"]),"bo")
	plt.show()


