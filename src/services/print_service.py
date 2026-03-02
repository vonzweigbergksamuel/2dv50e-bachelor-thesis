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
  print("TN: ", scores['tn'])
  print("FP: ", scores['fp'])
  print("FN: ", scores['fn'])
  print("TP: ", scores['tp'])
  print("--------------------------------")
  
def show_progress(current: int, total: int):
  """
  Shows the progress of the preprocesssing.
  """
  print(f"Progress: {int(current / total * 100)}%")
  

# TODO: Add a function to print result to a file.