import os
import pathlib
from dotenv import load_dotenv
from config import MODELS, TRIALS
from lib.clean_up import clean_up_database, clean_up_folder
from lib.download_models import download_models
from lib.generate_random_state import generate_random_state
from services.deepface_service import run_experiment
from services.preprocess_service import (
    insert_into_database,
    pre_process,
    set_up_directories,
)
from services.print_service import export_to_google_sheet, print_scores, save_results_to_file, show_progress, save_dataset_to_file
from services.scores_service import calculate_scores

load_dotenv()


def main():
    download_models()
    data_path = pathlib.Path(__file__).parent.parent / "data"
    datasets = os.listdir(data_path)

    set_up_directories()

    total_runs = len(datasets) * TRIALS * len(MODELS)
    completed_runs = 0

    print("Running experiments")

    for dataset in datasets:
        results = []
        save_dataset_to_file(dataset)
        for index in range(TRIALS):
            random_state = generate_random_state()
            path = data_path / dataset

            images_to_db = pre_process(path, random_state)

            for model in MODELS:
                insert_into_database(images_to_db, model)

                actual, predicted, avg_time = run_experiment(model)

                (
                    accuracy,
                    sensitivity,
                    specificity,
                    precision,
                    f1_score,
                    tn,
                    fp,
                    fn,
                    tp,
                ) = calculate_scores(actual, predicted)

                print(f"Actual: {actual}")
                print(f"Predicted: {predicted}")

                scores = {
                    "trial": index + 1,
                    "seed": random_state,
                    "model": model,
                    "dataset": dataset,
                    "accuracy": accuracy,
                    "sensitivity": sensitivity,
                    "specificity": specificity,
                    "precision": precision,
                    "f1_score": f1_score,
                    "tn": tn,
                    "fp": fp,
                    "fn": fn,
                    "tp": tp,
                    "avg_time": avg_time,
                }

                results.append(scores)

                completed_runs += 1
                show_progress(completed_runs, total_runs)

                clean_up_database()
            
            clean_up_folder()

        results.sort(key=lambda x: x["model"])
        for result in results:
            print_scores(result)
            save_results_to_file(result)
        
        export_to_google_sheet(results)


if __name__ == "__main__":
    main()
