# This service is used to print the results of the model to the console.
import os

from dotenv import load_dotenv

from services.preprocess_service import GOOGLE_SHEET_FILE, RESULTS_FILE

load_dotenv()
GOOGLE_SHEET_ID = os.getenv("GOOGLE")


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
    print("Embedding Cache Time: ", scores["embedding_cache_time"])
    print("Preprocess Time: ", scores["preprocess_time"])
    print("Gallery Build Time: ", scores["gallery_build_time"])
    print("Search Time: ", scores["search_time"])
    print("Cleanup Time: ", scores["cleanup_time"])
    print("--------------------------------")


def show_progress(current: int, total: int):
    """
    Shows the progress of the preprocesssing.
    """
    print(f"Progress: {int(current / total * 100)}%")


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


def save_results_to_file(scores: dict):
    """
    Saves the results to a file.
    """
    with open(RESULTS_FILE, "a", encoding="utf-8") as f:
        f.write("--------------------------------\n")
        f.write(f"Trial: {scores['trial']}\n")
        f.write(f"Model: {scores['model']}\n")
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
        f.write(f"Embedding Cache Time: {scores['embedding_cache_time']}\n")
        f.write(f"Preprocess Time: {scores['preprocess_time']}\n")
        f.write(f"Gallery Build Time: {scores['gallery_build_time']}\n")
        f.write(f"Search Time: {scores['search_time']}\n")
        f.write(f"Cleanup Time: {scores['cleanup_time']}\n")
        f.write(
            f"Excel format: {scores['tp']}, {scores['fn']}, {scores['fp']}, {scores['tn']}, {scores['seed']}, {scores['avg_time']}\n"
        )
        f.write("--------------------------------\n")


def export_to_google_sheet(scores: list[dict]):
    """
    Exports the results to a google sheet.
    """
    LAST_MODEL = ""
    with open(GOOGLE_SHEET_FILE, "a", encoding="utf-8") as f:
        for score in scores:
            if score["model"] != LAST_MODEL:
                LAST_MODEL = score["model"]
                f.write("--------------------------------\n")
                f.write(f"- Model: {LAST_MODEL}\n")
                f.write("--------------------------------\n")

            f.write(
                f"{score['tp']}, {score['fn']}, {score['fp']}, {score['tn']}, {score['seed']}, {score['avg_time']}\n"
            )
