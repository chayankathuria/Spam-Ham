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

# calculate AUC

# metrics.roc_auc_score(y_test, y_pred_prob)
print("AUC Score: " + '{:.5f}%'.format(metrics.roc_auc_score(y_test, y_pred_prob)*100))

preds = y_pred_prob_clf[:,1]
fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
roc_auc = metrics.auc(fpr, tpr)

plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
