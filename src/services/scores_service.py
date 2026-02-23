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


def calculate_scores(
    tp: int, tn: int, fp: int, fn: int
) -> tuple[float, float, float, float, float]:
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

    accuracy = calculate_accuracy(tp, tn, fp, fn)
    sensitivity = calculate_sensitivity(tp, fn)
    specificity = calculate_specificity(tn, fp)
    precision = calculate_precision(tp, fp)
    f1_score = calculate_f1_score(precision, sensitivity)
    return accuracy, sensitivity, specificity, precision, f1_score
