# 3: Exploratory Data Analysis

# examine the shape
data.shape

# examine the first 10 rows
data.head(10)

# examine the class distribution
data.label.value_counts()

# 4: Transforming labels

# convert label to a numerical variable# conve 
data['label_num'] = data.label.map({'ham':0, 'spam':1})

# check that the conversion worked
data.head(10)

# Generate input (X) and output (y) pair
X = data.message
y = data.label_num
print(X.shape)
print(y.shape)

total_len = len(data['label'])
percentage_labels = (data['label'].value_counts()/total_len)*100
percentage_labels

# sns.countplot(data.label)

# Graphical representation of the target label percentage.

sns.set()
sns.countplot(data.label).set_title('Data Distribution')
ax = plt.gca()
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width()/2.,
            height + 2,
            '{:.2f}%'.format(100*(height/total_len)),
            fontsize=14, ha='center', va='bottom')
sns.set(font_scale=1.5)
ax.set_xlabel("Labels")
ax.set_ylabel("Numbers of records")
plt.show()

# 5: Split data set into training and testing

# split X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)



