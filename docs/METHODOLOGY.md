# Methodology

We will perform a controlled scientific experiement to evaluate face-recognition models in the DeepFace framework.

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

### 3. Perform experiments

- Run the experiment for every face-recognition model supported by the DeepFace framework.
- For each model perform 10 independent trials. For every trial:
  - Shuffle the dataset, then split it into training and test sets (record the random seed).
  - Run the model on the test set and save the model's prediction, the correct label and the metric scores (mentioned later) to a Google Spreadsheet.
  - After completing 10 trials for a model, compute the average and standard deviation for each metric.

**Notes:**

- Maybe save raw scores (probabilities, similarity scores or distance metric) and each trial's confusion matrix. Raw scores could be useful if we decide to change/play around with thresholds/cutoffs.
- Use consistent splitting and seeding so results are reproducible.

### 4. Evaluate result

We evaluate per-trial performance using a confusion matrix, then aggregate metrics across trials.

Classes:

- A class is a category the model predicts for a sample.
- In this project the two classes are:
  - Known, the model recognizes the person.
  - Unknown, the model does not recognize the person.
- Class imbalance means one class appears much more often than the other (for example, many Known samples but few Unknown samples).

Confusion matrix layout:

|                | Predicted Known | Predicted Unknown |
| -------------- | --------------- | ----------------- |
| Actual Known   | TP              | FN                |
| Actual Unknown | FP              | TN                |

Definitions:

- TP = True Positive
- TN = True Negative
- FP = False Positive
- FN = False Negative

- Sensitivity / Recall
  - Sensitivity = TP / (TP + FN)

- Specificity
  - Specificity = TN / (TN + FP)

- Accuracy
  - Accuracy = (TP + TN) / (TP + TN + FP + FN)

- Precision
  - Precision = TP / (TP + FP)

- F1 score
  - F1 = 2 _ (Precision _ Sensitivity) / (Precision + Sensitivity)

Evaluation procedure:

1. For each trial compute the confusion matrix and the metrics above.
2. Report the average and standard deviation of each metric across the 10 trials.
3. Save the results to a Google Spreadsheet.
4. If one class is much rarer than the other (class imbalance), prefer reporting precision, recall, and F1 instead of accuracy.
5. Use scikit-learn for `confusion_matrix`.

## Controlled Scientific Experiment

### Independent variables

What models we will compare.

- Facenet512
- Facenet
- Dlib
- VGG Face
- ArcFace
- GhostFaceNet
- SFace
- OpenFace
- DeepFace
- DeepID

### Dependent variables

We will report metrics like precision, sensitivity/recall, accuracy, F1 and confusion-matrix.

### Controlled variables

- Dataset versions and normalized folder structure
- Face detector and preprocessing pipeline, MTCNN, alignment, normalization (DeepFace internal)
- Split method and proportions (50/50 known/unknown, record random seeds)
- Number of trials (10) and the procedure per trial (shuffle -> split -> test)
- Software and model versions (DeepFace version, model weights, scikit-learn version, python version)
- Evaluation code (same scripts/calculations)
- Reporting format (Google Spreadsheet, saved logs to file?)
- Hardware specs (CPU, GPU & OS) for reproducibility

### Partially-controlled

- Random seed per trial (allowed randomness but record seed)
- Non-determinism from library implementations? Implement calculations ourselves?

### Uncontrolled variables

- Label errors in dataset
- Data leakage (same identity in train and test data due to faulty splitting)
- Class imbalance (many Known vs few Unknown)
- Correlated samples (near-duplicates, same scene/lighting)
- Demographic biases (age, ethnicity, gender distribution differences across classes)
- Image quality variation
