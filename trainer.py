# Importing the dependencies
from main_data import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# Data Collection and Pre Processing
X=X_data()
Y =Y_data()

# Splitting the data into training data and test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=1)

# Feature Extraction
# transform the text data to feature vectors that can be used as input to the logistic regression
feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

# convert Y_train and Y_test values as integers
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

# Training the Model
model = LogisticRegression()
model.fit(X_train_features, Y_train)

# Evaluating the model
prediction_on_training_model = model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_model)
print("Accuracy on training data: ", accuracy_on_training_data)
prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)
print("Accuracy on test data: ", accuracy_on_test_data)

#exporting models using pickle
import pickle
filename_model='trained_model.sav'
filename_features='feature_extraction.sav'
pickle.dump(model,open(filename_model,'wb'))
pickle.dump(feature_extraction,open(filename_features,'wb'))

# saving accuracy details in database for future use
save_acc(int(accuracy_on_training_data*100),int(accuracy_on_test_data*100),X_train.shape[0],X_test.shape[0])