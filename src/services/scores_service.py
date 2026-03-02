from sklearn.metrics import confusion_matrix
from services.preprocess_service import UNKNOWN

# This service is used to calculate the following scores of a model: Accuracy, Sensitivity/Recall, Specificity, Precision, F1-score.

# tp = True Positive
# when the model predicts the right person

# tn = True Negative
# when the model correctly predicts "Unknown", ie. the person doesn't exist in the training set

# fp = False Positive
# when the model wrongly predicts a person when it should be "Unknown"

# fn = False Negative
# when the model predicts either "Unknown" when the person actually exists, or the wrong person


def calculate_accuracy(tp: int, tn: int, fp: int, fn: int) -> float:
    """Calculates the percentage of correct predictions."""
    return (tp + tn) / (tp + tn + fp + fn)


def calculate_sensitivity(tp: int, fn: int) -> float:
    """Calculates the percentage of correct predictions when the person actually exists."""
    return tp / (tp + fn)


def calculate_specificity(tn: int, fp: int) -> float:
    """Calculates the percentage of correct predictions when the person doesn't exist in the training set."""
    return tn / (tn + fp)


def calculate_precision(tp: int, fp: int) -> float:
    """Calculates the percentage of correct predictions when the model predicts a person."""
    return tp / (tp + fp)


def calculate_f1_score(precision: float, sensitivity: float) -> float:
    """Calculates the harmonic mean of precision and sensitivity."""
    return 2 * (precision * sensitivity) / (precision + sensitivity)


def calculate_confusion_matrix(
    actual: list[str], predicted: list[str]
) -> tuple[int, int, int, int]:
    """Calculates the confusion matrix."""
    tn = 0
    fp = 0
    fn = 0
    tp = 0

    for i in range(len(actual)):
        if actual[i] != UNKNOWN:
            if predicted[i] == actual[i]:
                tp += 1
            else:
                fn += 1
        else:
            if predicted[i] == UNKNOWN:
                tn += 1
            else:
                fp += 1

    return tn, fp, fn, tp


def calculate_scores(
    actual: list[str], predicted: list[str]
) -> tuple[float, float, float, float, float, int, int, int, int]:
    """
    Calculates the scores for the model.

    Args:
        tp: True Positive
        tn: True Negative
        fp: False Positive
        fn: False Negative

    Returns:
        A tuple with the following scores: accuracy, sensitivity, specificity, precision, f1-score.
    """
    tn, fp, fn, tp = calculate_confusion_matrix(actual, predicted)

    accuracy = calculate_accuracy(tp, tn, fp, fn)
    sensitivity = calculate_sensitivity(tp, fn)
    specificity = calculate_specificity(tn, fp)
    precision = calculate_precision(tp, fp)
    f1_score = calculate_f1_score(precision, sensitivity)
    return accuracy, sensitivity, specificity, precision, f1_score, tn, fp, fn, tp
