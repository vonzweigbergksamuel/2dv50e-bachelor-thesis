#######################################
# Configuration
#######################################
# Models to benchmark
MODELS = ["Facenet", "ArcFace"]

# The face detector model to be used
DETECTOR_BACKEND = "retinaface"

# Number om trial on each model with the same dataset
TRIALS = 10

# File names
RESULTS_FILE = "results.txt"
GOOGLE_SHEET_FILE = "google_sheet.txt"
