import pathlib
from services.preprocess_service import pre_process
from lib.clean_up import clean_up
from services.print_service import print_scores
import time
from services.deepface_service import run_experiment
from config import MODELS, TRIALS
from dotenv import load_dotenv
from lib.generate_random_state import generate_random_state
import os
from services.scores_service import calculate_scores

load_dotenv()

def main():
    data_path = pathlib.Path(__file__).parent.parent / "data"
    datasets = os.listdir(data_path)
    
    for dataset in datasets:
        print(f"Running experiments for dataset: {dataset}")
        for index in range(TRIALS):
            random_state = generate_random_state()
            path = data_path / dataset
            
            for model in MODELS:
                pre_process(path, model, random_state)
            
                actual, predicted = run_experiment(model)
                
                accuracy, sensitivity, specificity, precision, f1_score = calculate_scores(actual, predicted)
                
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
                    "f1_score": f1_score
                }
                
                print_scores(scores)
                
                # time.sleep(5)
                # clean_up()
            
if __name__ == "__main__":
    main()
