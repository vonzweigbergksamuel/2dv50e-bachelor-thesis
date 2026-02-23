# Methodology

We will complete these tests with the following face detection model: MTCNN. That is the same our related work article uses.

## Related Work

One of the related work articles have split the data set into 50/50 for training and testing. The seccond article of the related work uses 5,000 images out of 13,000 images. However it is still unkown if they trained on 13,000 images and tested on 5,000 images.

## Plan

### 1. Prepaire and normalize the datasets

First we need to normalize the datasets to a unified structure. 

For example:

- We have 10 images of Brad Pitt and he is in the known group. 5 of the 10 images will be in the database and 5 of them will be in the test set.
- We have 10 images of Will Smith and he is in the unknown group. 5 of the 10 images will be in the test set.

DeepFace want to have the following structure on the data in their databse:

- 📁 database
  - 📁 person-name
    - 📷 001.jpg
    - 📷 002.jpg
    - 📷 003.jpg
    - 📷 ...
  - 📁 person-name
    - 📷 001.jpg
    - 📷 002.jpg
    - 📷 003.jpg
    - 📷 ...

_We need to place the images in the correct folder structure for the DeepFace framework to work. Known and unkown persons in the correct folder. The above is an example of how the known persons are placed in the database._

When our datasets is normalized we can split the dataset into know and unknown persons. We will use a 50/50 split for both the groups and the image selection. SciKit will be used for doing the splitting.

### 2. Run the experiment on all models.

We wil run the experiment on all models that are supported by the DeepFace framework. After each prediction we will save the result and store it until all tests are done for that model, Then for each model we will evaluate the results.

### 3. Evaluate the results.

We will use a confusion matrix to evaluate the results. This will help us to get a better and compareable result on the models.

|                | Predicted Known | Predicted Unknown |
| -------------- | --------------- | ----------------- |
| Actual Known   | TP              | FN                |
| Actual Unknown | FP              | TN                |

For each test run we will compare different key figures and metrics. We will use the following metrics:

- Sensitivity / Recall
- Specificity
- Accuracy
- Precision
- F1-score

To be able to calculate the scores correct we need to save every result in an array which we later can send to the confusion matrix. The confusion matrix is a needed to calculate the scores correct.

_We can use scikit-learn to get the training and testing set. We can also use the confusion matrix from scikit-learn. And also for some scores._

TP = True Positive
TN = True Negative
FP = False Positive
FN = False Negative

[Read more about the Confusion Matrix](https://www.geeksforgeeks.org/machine-learning/confusion-matrix-machine-learning/)

### Sensitivity / Recall

Hur ofta systemet korrekt igenkänner när ansiktet tillhör någon i databasen.

```markdown
Sensitivity=TP/(TP+FN)
```

### Specificity

Hur ofta systemet korrekt nekar igenkänning när ansiktet inte tillhör någon i databasen.

```markdown
Specificity=TN/(TN+FP)
```

### Accuracy

Om det finns många fler negativa än positiva fall kan accuracy vara hög även om modellen är dålig på det viktiga.

```markdown
Accuracy=(TP+TN)/(TP+TN+FP+FN)
```

### Precision

Hur ofta systemet har rätt när det säger att två ansikten matchar.

```markdown
Precision=TP/(TP+FP)
```

### F1-score

Den visar hur väl modellen presterar överlag, utan att gynna bara precision eller bara sensitivity.

```markdown
F1=2∗(Precision∗Sensitivity)/(Precision+Sensitivity)
```
