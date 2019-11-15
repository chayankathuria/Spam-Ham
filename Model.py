# Step 7: Training the Model

# Creating a logistic regression model with very low regularization of e10-5
clf = linear_model.LogisticRegression(C=1e5)

# train the model using X_train_dtm (timing it with an IPython "magic command")
%time clf.fit(X_train_dtm, y_train)

# Step 8: Running the model on test data

# make class predictions for X_test_dtm
y_pred_class = clf.predict(X_test_dtm)

# Predict probability
y_pred_prob_clf = clf.predict_proba(X_test_dtm)

# This is not testing the model. It is just checking how the model peroforms on unseen data. 
# Testing is checking its accuracy and other metric which is added in the next file.
