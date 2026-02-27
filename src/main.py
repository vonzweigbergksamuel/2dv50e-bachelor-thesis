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
                
                print(f"Actual: {actual}")
                print(f"Predicted: {predicted}")
                
                scores = {
                    "trial": index + 1,
                    "seed": random_state,
                    "model": model,
                    "dataset": dataset
                }
                
                print_scores(scores)
                
                # time.sleep(5)
                # clean_up()
            
    # print("Hello from 2dv50e-bachelor-thesis!")
    # random_state = generate_random_state()
    # ###################### Preprocessing ######################
    # print("Starting preprocessing...")
    # path = pathlib.Path(__file__).parent.parent / "data" / "dataset"
    # pre_process(path, MODEL, random_state)
    # print("Preprocessing complete!")
    
    # ###################### Experiment ######################
    # print("Starting experiment...")
    # run_experiment(MODEL)
    
    # ###################### Results ######################
    # scores = {
    #     "seed": random_state
    # }
    
    # print_scores(scores)
    
    # time.sleep(5)
    # clean_up()


if __name__ == "__main__":
    main()
