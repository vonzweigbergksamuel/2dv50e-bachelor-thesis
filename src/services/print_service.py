# This service is used to print the results of the model to the console.
def print_scores(scores: dict):
  """
  Prints the scores to the console.
  """
  print("")
  print("--------------------------------")
  print("Trial: ", scores['trial'])
  print("Model: ", scores['model'])
  print("Seed: ", scores['seed'])
  print("Dataset: ", scores['dataset'])
  print("Accuracy: ", scores['accuracy'])
  print("Sensitivity: ", scores['sensitivity'])
  print("Specificity: ", scores['specificity'])
  print("Precision: ", scores['precision'])
  print("F1 Score: ", scores['f1_score'])
  print("--------------------------------")