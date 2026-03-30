# This service is used to print the results of the model to the console.
from dotenv import load_dotenv

from config import GOOGLE_SHEET_FILE, RESULTS_FILE

load_dotenv()


def print_scores(scores: dict):
    """
    Prints the scores to the console.
    """
    print("")
    print("--------------------------------")
    print("Trial: ", scores["trial"])
    print("Model: ", scores["model"])
    print("Seed: ", scores["seed"])
    print("Dataset: ", scores["dataset"])
    print("Accuracy: ", scores["accuracy"])
    print("Sensitivity: ", scores["sensitivity"])
    print("Specificity: ", scores["specificity"])
    print("Precision: ", scores["precision"])
    print("F1 Score: ", scores["f1_score"])
    print("TN: ", scores["tn"])
    print("FP: ", scores["fp"])
    print("FN: ", scores["fn"])
    print("TP: ", scores["tp"])
    print("Avg Time: ", scores["avg_time"])
    print("--------------------------------")


def show_progress(task: str, current: int, total: int):
    """
    Shows the progress of the preprocesssing.
    """
    percentage = float(current / total * 100)
    print(f"{task} Progress: {round(percentage, 2)}%")


def save_dataset_to_file(dataset_name: str):
    """
    Saves the dataset to a file.
    """
    with open(RESULTS_FILE, "a", encoding="utf-8") as f:
        f.write("#################################\n")
        f.write(f"# Dataset: {dataset_name}\n")
        f.write("#################################\n")

    with open(GOOGLE_SHEET_FILE, "a", encoding="utf-8") as f:
        f.write("#################################\n")
        f.write(f"# Dataset: {dataset_name}\n")
        f.write("#################################\n")


def save_results_to_file(scores: dict, model: str):
    """
    Saves the results to a file.
    """
    with open(RESULTS_FILE, "a", encoding="utf-8") as f:
        f.write("--------------------------------\n")
        f.write(f"Trial: {scores['trial']}\n")
        f.write(f"Model: {model}\n")
        f.write(f"Seed: {scores['seed']}\n")
        f.write(f"Dataset: {scores['dataset']}\n")
        f.write(f"Accuracy: {scores['accuracy']}\n")
        f.write(f"Sensitivity: {scores['sensitivity']}\n")
        f.write(f"Specificity: {scores['specificity']}\n")
        f.write(f"Precision: {scores['precision']}\n")
        f.write(f"F1 Score: {scores['f1_score']}\n")
        f.write(f"TN: {scores['tn']}\n")
        f.write(f"FP: {scores['fp']}\n")
        f.write(f"FN: {scores['fn']}\n")
        f.write(f"TP: {scores['tp']}\n")
        f.write(f"Avg Time: {scores['avg_time']}\n")
        f.write(
            f"Excel format: {scores['tp']}, {scores['fn']}, {scores['fp']}, {scores['tn']}, {scores['seed']}, {scores['avg_time']}\n"
        )
        f.write("--------------------------------\n")

def export_model_to_google_sheet(model: str):
    """
    Exports the model to a google sheet.
    """
    with open(GOOGLE_SHEET_FILE, "a", encoding="utf-8") as f:
        f.write("--------------------------------\n")
        f.write(f"- Model: {model}\n")
        f.write("--------------------------------\n")

def export_to_google_sheet(score: dict):
    """
    Exports the results to a google sheet.
    """
    with open(GOOGLE_SHEET_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"{score['tp']}, {score['fn']}, {score['fp']}, {score['tn']}, {score['seed']}, {score['avg_time']}\n"
        )


def print_current_status(msg: str):
    """
    Prints the current status of the task.
    """
    print(f"{msg}")
    
def show_taken_time(start_time: float, end_time: float):
    """
    Shows the time taken for the task.
    """
    time_taken = (end_time - start_time) / 60
    print(f"Time taken: {round(time_taken, 2)} minutes")
    
def print_to_files(msg: str):
    """
    Prints the message to the files.
    """
    with open(RESULTS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{msg}\n")
    with open(GOOGLE_SHEET_FILE, "a", encoding="utf-8") as f:
        f.write(f"{msg}\n")