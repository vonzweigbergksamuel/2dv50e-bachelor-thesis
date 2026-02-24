# Methodology

We will complete these tests with the following face detection model: MTCNN. That is the same our related work article uses.

## Related Work

One of the related work articles have split the data set into 50/50 for training and testing. The second article of the related work uses 5,000 images out of 13,000 images. However it is still unknown if they trained on 13,000 images and tested on 5,000 images.

## Plan

### 1. Normalize dataset structure

For DeepFace to be able to properly use the datasets they need to adhere to the following structure:

- 📁 dataset
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

### 2. Splitting the dataset

To fully and properly test the capabilitys of the face recognition models we need to split the dataset into different groups. The splitting will be done on a copy of a normalized dataset and in two stages, one for splitting into a _Known_ and _Unknown_ group, and then a split of each persons images belonging to the _Known_ group. We will use a 50/50 ratio for both splits, selecting 50% of people to be _Known_ and 50% of the images of _Known_ people to train the models on. All splitting will be done at random and we will use SciKit Learn for it.

- **Known**
  - People that the models should know, at least 1 image exists in the training data
  - Select some of each known persons images to train the model on, the rest needs to be reserved for testing
  - Selection of which people should be known and which of those peoples images should be trained on should be random
- **Unknown**
  - People that the models should have no knowledge about, no image exists in the training data
  - None of these peoples images should be used to train the models
  - 50% of their images should however be used to test the models (expecting an "Unknown" result)

**For example:**

- After the first split, Brad Pitt gets put in the _known_ group.
  - There exists 10 images of Brad Pitt. The second split selects which 5 of the 10 images that will be used to train the models, the remaining images will be used to run the tests.
- After the first split, Will Smith gets put in the _unknown_ group.
  - There exists 10 images of Will Smith. 5 of the 10 images will be choosen at random and used to test the models.

### 3. Run the experiment on all models.

We will run the experiment on all face recognition models that are supported by the DeepFace framework. After each prediction we will save the result and store it until all tests are done for that model, Then for each model we will evaluate the results.

We will run the experiment 10 times for each model to get a better average result. For each run the dataset will be reseted and split again.

After a complete run we will calculate the scores.

### 4. Evaluate the results.

We will use a confusion matrix to evaluate the results. This will help us to get a better and comparable result on the models.

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
