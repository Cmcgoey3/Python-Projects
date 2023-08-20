import matplotlib
import matplotlib.pyplot as plt
import random
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold, cross_val_score
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import math


#######################################################################
#######################################################################
# TEST ON DATA SET 5
#######################################################################
#######################################################################

xValues=[]
yValues=[]
classes=[]

numGreen = 150
numBlack = 100
numRed = 150
numPink = 100
greenFull = False
blackFull = False
redFull = False
pinkFull = False

while (numGreen > 0) or (numBlack > 0) or (numRed > 0) or (numPink > 0):
    x = random.randint(1,100)
    y = random.randint(1,100)

    if (numGreen == 0): greenFull = True
    if (numBlack == 0): blackFull = True
    if (numRed == 0): redFull = True
    if (numPink == 0): pinkFull = True
  
    if ((x > 10) and (x < 90)) and ((y > 65) and (y < 70) and (not greenFull)):
        numGreen -= 1
        xValues.append(x)
        yValues.append(y)
        classes.append(0)
    
    if ((x > 30) and (x < 60)) and ((y > 45) and (y < 50) and (not blackFull)):
        numBlack -= 1
        xValues.append(x)
        yValues.append(y)
        classes.append(1)
        
    if ((x > 10) and (x < 90)) and ((y > 30) and (y < 35) and (not redFull)):
        numRed -= 1
        xValues.append(x)
        yValues.append(y)
        classes.append(2)
        
    if ((x > 30) and (x < 60)) and ((y > 10) and (y < 15) and (not pinkFull)):
        numPink -= 1
        xValues.append(x)
        yValues.append(y)
        classes.append(3)

data = list(zip(xValues, yValues))

plt.scatter(xValues, yValues, c=classes)
plt.show()

dtree = DecisionTreeClassifier()
dtree = dtree.fit(data, classes)

tree.plot_tree(dtree, feature_names=["X", "Y"])

plt.show()

k_folds = KFold(n_splits = 3)
scores = cross_val_score(dtree, data, classes, cv = k_folds)
print("TEST FOLDS FOR DATA SET 5. DECISION TREE CLASSIFIER. K=3 FOLDS")
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))
print("\n")

k_folds = KFold(n_splits = 5)
scores = cross_val_score(dtree, data, classes, cv = k_folds)
print("TEST FOLDS FOR DATA SET 5. DECISION TREE CLASSIFIER. K=5 FOLDS")
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))
print("\n")

#######################################################################
#######################################################################
# TEST ON DATA SET 1
#######################################################################
#######################################################################

xValues=[]
yValues=[]
classes=[]

numGreen = 30
numBlack = 150
numRed = 150
greenFull = False
blackFull = False
redFull = False

while (numGreen > 0) or (numBlack > 0) or (numRed > 0):
    x = random.randint(1,100)
    y = random.randint(1,100)

    if (numGreen == 0): greenFull = True
    if (numBlack == 0): blackFull = True
    if (numRed == 0): redFull = True

    distanceToCenter = ((50 - x) ** 2) + ((50 - y) ** 2)
    distanceToCenter = math.sqrt(distanceToCenter)

    if((distanceToCenter < 3) and (not greenFull)):
        numGreen -= 1
        xValues.append(x)
        yValues.append(y)
        classes.append(0)
    
    if((distanceToCenter > 9) and (distanceToCenter < 12) and (not blackFull)):
        numBlack -= 1
        xValues.append(x)
        yValues.append(y)
        classes.append(1)
    
    if((distanceToCenter > 28) and (distanceToCenter < 31) and (not redFull)):
        numRed -= 1
        xValues.append(x)
        yValues.append(y)
        classes.append(2)

data = list(zip(xValues, yValues))

plt.scatter(xValues, yValues, c=classes)
plt.show()

dtree = DecisionTreeClassifier()
dtree = dtree.fit(data, classes)

tree.plot_tree(dtree, feature_names=["X", "Y"])

plt.show()

k_folds = KFold(n_splits = 3)
scores = cross_val_score(dtree, data, classes, cv = k_folds)
print("TEST FOLDS FOR DATA SET 1. DECISION TREE CLASSIFIER. K=3 FOLDS")
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))
print("\n")

k_folds = KFold(n_splits = 5)
scores = cross_val_score(dtree, data, classes, cv = k_folds)
print("TEST FOLDS FOR DATA SET 1. DECISION TREE CLASSIFIER. K=5 FOLDS")
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))
print("\n")

#######################################################################
#######################################################################
# TEST ON DATA SET 2
#######################################################################
#######################################################################

xValues=[]
yValues=[]
classes=[]

numGreen = 100
numBlack = 200
numRed = 100
greenFull = False
blackFull = False
redFull = False

while (numGreen > 0) or (numBlack > 0) or (numRed > 0):
    x = random.randint(1,100)
    y = random.randint(1,100)

    if (numGreen == 0): greenFull = True
    if (numBlack == 0): blackFull = True
    if (numRed == 0): redFull = True

    if((x > 55) and (x < 60) and (y > 40) and (y < 45) and (not greenFull)):
        numGreen -= 1
        xValues.append(x)
        yValues.append(y)
        classes.append(0)
    elif ((x > 65) and (x < 70) and (y > 60) and (y < 65) and (not redFull)):
        numRed -= 1
        xValues.append(x)
        yValues.append(y)
        classes.append(1)
    elif (not blackFull):
        numBlack -= 1
        xValues.append(x)
        yValues.append(y)
        classes.append(2)

data = list(zip(xValues, yValues))

plt.scatter(xValues, yValues, c=classes)
plt.show()

dtree = DecisionTreeClassifier()
dtree = dtree.fit(data, classes)

tree.plot_tree(dtree, feature_names=["X", "Y"])

plt.show()

k_folds = KFold(n_splits = 3)
scores = cross_val_score(dtree, data, classes, cv = k_folds)
print("TEST FOLDS FOR DATA SET 2. DECISION TREE CLASSIFIER. K=3 FOLDS")
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))
print("\n")

k_folds = KFold(n_splits = 5)
scores = cross_val_score(dtree, data, classes, cv = k_folds)
print("TEST FOLDS FOR DATA SET 2. DECISION TREE CLASSIFIER. K=5 FOLDS")
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))
print("\n")