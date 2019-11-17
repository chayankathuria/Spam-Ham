# Spam-Ham
A simple text classification without nltk
---------------------------------------------------------------------------------------------------------------

Dataset used: https://www.kaggle.com/ishansoni/sms-spam-collection-dataset

---------------------------------------------------------------------------------------------------------------

Steps used:

        Step 1: Import dependencies
    
        Step 2: Load data
    
        Step 3: Exploratory Data Analysis
    
        Step 4: Transforming labels
    
        Step 5: Split data set into training and testing
    
        Step 6: Generating Features using CountVectorizer
    
        Step 7: Train model
    
        Step 8: Test model 
    
            Step 8.1: Measure Accuracy
    
            Step 8.2: Confusion Matrix 
            
            Step 8.3 Area Under Curve
            
--------------------------------------------------------------------------------------------------------------
     
TP = Correct hit

TN = Correct rejection

FP = False alarm 

FN = Miss the situation     

ROC and AUC
TPR: This is our Y-axis

This metric corresponds to the proportion of positive data points that are correctly considered as positive, with respect to all positive data points.

In other words, higher TPR, the fewer positive data points we will miss.

FPR: This is our X-axis

This metric corresponds to the proportion of negative data points that are mistakenly considered as positive, with respect to all negative data points.

In other words, the higher FPR, the more negative data points will be 

------------------------------------------------------------------------------------------------------------
