import os
import pathlib
import time

from dotenv import load_dotenv

from config import MODELS, TRIALS
from lib.download_models import download_models
from lib.generate_random_state import get_random_seeds
from services import database_service
from services.experiment import run_experiment
from services.preprocess_service import (
    pre_process,
    set_up_directories,
)
from services.print_service import (
    export_model_to_google_sheet,
    export_to_google_sheet,
    print_current_status,
    print_scores,
    print_to_files,
    save_dataset_to_file,
    save_results_to_file,
    show_progress,
    show_taken_time,
)
from services.scores_service import calculate_scores
from services.splitting_service import splitting_service

load_dotenv()


def main():
    download_models()
    data_path = pathlib.Path(__file__).parent.parent / "data"
    datasets = sorted(
        d for d in os.listdir(data_path)
        if (data_path / d).is_dir()
    )

    set_up_directories()

    completed_datasets = 0

    for dataset in datasets:
        print_current_status(f"Processing dataset: {dataset}")
        path = data_path / dataset
        save_dataset_to_file(dataset)
        seeds = get_random_seeds(TRIALS)

        completed_models = 0

        for model in MODELS:
            start_time = time.perf_counter()
            print_current_status(f"Processing model: {model}")

            try:
                export_model_to_google_sheet(model)
                subjects, avg_time_per_embedding = pre_process(path, model)

                if not subjects:
                    print_current_status(f"  [SKIP] No valid subjects for {model} on {dataset}")
                    completed_models += 1
                    continue

                for trial, seed in enumerate(seeds):
                    try:
                        known_subjects, unknown_subjects = splitting_service(subjects, seed)

                        for subject in known_subjects:
                            database_service.insert_subject(
                                subject["identity"], subject["known_images"]
                            )

                        actual, predicted = run_experiment(
                            model, known_subjects, unknown_subjects
                        )
                        
                        print(f"Actual: {actual}")
                        print(f"Predicted: {predicted}")

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

                        scores = {
                            "trial": trial + 1,
                            "seed": seed,
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
                            "avg_time": avg_time_per_embedding,
                        }

                        print_scores(scores)
                        save_results_to_file(scores, model)
                        export_to_google_sheet(scores)

                    except Exception as e:
                        print_current_status(
                            f"  [ERROR] Trial {trial + 1} failed for {model}: {e}"
                        )
                        print_to_files(f"  [ERROR] Trial {trial + 1} failed for {model}: {e}")
                    finally:
                        database_service.clear_database()

            except Exception as e:
                print_current_status(f"  [ERROR] Model {model} failed on {dataset}: {e}")
                print_to_files(f"  [ERROR] Model {model} failed on {dataset}: {e}")

            completed_models += 1
            show_progress("Models", completed_models, len(MODELS))

            end_time = time.perf_counter()
            show_taken_time(start_time, end_time)

        completed_datasets += 1
        show_progress("Datasets", completed_datasets, len(datasets))

    print_current_status("Experiment completed!")


if __name__ == "__main__":
    main()
