# calculate accuracy of class predictions
from sklearn import metrics

# metrics.accuracy_score(y_test, y_pred_class)
print("Accuracy: " + '{:.5f}%'.format(metrics.accuracy_score(y_test, y_pred_class)*100))

# print the confusion matrix
metrics.confusion_matrix(y_test, y_pred_class)

#Confusion matrix heat plot
ax= plt.subplot()
sns.heatmap(metrics.confusion_matrix(y_test, y_pred_class), annot=True, ax = ax,fmt=".1f")

# labels, title and ticks
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix'); 
ax.xaxis.set_ticklabels(['Ham_0', 'Spam_1']); ax.yaxis.set_ticklabels(['Ham_0', 'Spam_1'])

# print message text for the false positives (ham incorrectly classified as spam)
X_test[y_test < y_pred_class]

# print message text for the false negatives (spam incorrectly classified as ham)
X_test[y_test > y_pred_class]
