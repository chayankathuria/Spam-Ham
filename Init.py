# 1. Import dependencies

import pandas as pd
import numpy as np


# split X and y into training and testing sets
from sklearn.model_selection import train_test_split

# import and instantiate CountVectorizer (with the default parameters)
from sklearn.feature_extraction.text import CountVectorizer

# Import sklearn linear model
from sklearn import linear_model

# calculate accuracy of class predictions
from sklearn import metrics

# Visualization
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# 2. Load data

# read file into pandas using a relative path
path = 'data/sms.tsv'
data = pd.read_table(path, header=None, names=['label', 'message'])
