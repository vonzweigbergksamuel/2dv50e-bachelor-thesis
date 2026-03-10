import os
import pathlib
import time

from dotenv import load_dotenv

from config import MODELS, TRIALS
from lib.download_models import download_models
from services.deepface_service import build_embedding_cache, run_experiment
from services.preprocess_service import (
    load_dataset,
    pre_process,
    set_up_directories,
)
from services.print_service import (
    export_to_google_sheet,
    print_scores,
    save_dataset_to_file,
    save_results_to_file,
    show_progress,
)
from services.scores_service import calculate_scores

load_dotenv()


def main():
    download_models()
    data_path = pathlib.Path(__file__).parent.parent / "data"
    datasets = sorted(
        dataset for dataset in os.listdir(data_path) if (data_path / dataset).is_dir()
    )

    set_up_directories()

    total_runs = len(datasets) * TRIALS * len(MODELS)
    completed_runs = 0

    print("Running experiments")

    for dataset in datasets:
        results = []
        save_dataset_to_file(dataset)
        dataset_path = data_path / dataset
        dataset_images = load_dataset(dataset_path)

        for model in MODELS:
            cache_start = time.perf_counter()
            embedding_cache = build_embedding_cache(dataset_images, model)
            embedding_cache_time = time.perf_counter() - cache_start

            for index in range(TRIALS):
                # random_seed = generate_random_state()
                random_seed = 42

                preprocess_start = time.perf_counter()
                split = pre_process(dataset_images, random_seed)
                preprocess_time = time.perf_counter() - preprocess_start

                (
                    actual,
                    predicted,
                    avg_time,
                    gallery_build_time,
                    search_time,
                ) = run_experiment(model, split, embedding_cache)

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
                    "trial": index + 1,
                    "seed": random_seed,
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
                    "embedding_cache_time": embedding_cache_time,
                    "preprocess_time": preprocess_time,
                    "gallery_build_time": gallery_build_time,
                    "search_time": search_time,
                    "cleanup_time": 0.0,
                }

                results.append(scores)

                completed_runs += 1
                show_progress(completed_runs, total_runs)

        results.sort(key=lambda x: (x["model"], x["trial"]))
        for result in results:
            print_scores(result)
            save_results_to_file(result)

        export_to_google_sheet(results)


if __name__ == "__main__":
    main()
