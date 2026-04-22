#######################################
# Configuration
#######################################

# Models to benchmark
# MODELS = [
#     "VGG-Face", "Facenet", "Facenet512", "OpenFace",
#     "DeepID", "ArcFace", "SFace", "GhostFaceNet",
#     "Buffalo_L", "Dlib",
# ]
MODELS = ["Facenet512"]

# The face detector model to be used
DETECTOR_BACKEND = "retinaface"

# Number om trial on each model with the same dataset
TRIALS = 10

# File names
RESULTS_FILE = "results.txt"
GOOGLE_SHEET_FILE = "google_sheet.txt"


# Constants
UNKNOWN = "Unknown"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
