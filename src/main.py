import pathlib
from services.preprocess_service import pre_process
from lib.clean_up import clean_up
import time

def main():
    print("Hello from 2dv50e-bachelor-thesis!")
    path = pathlib.Path(__file__).parent.parent / "data" / "dataset"
    seed = pre_process(path)
    
    print("Random state: ", seed)
    
    time.sleep(5)
    clean_up()


if __name__ == "__main__":
    main()
