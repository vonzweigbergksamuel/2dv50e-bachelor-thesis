from scipy.stats import wilcoxon

facenet512 = {
    "LFW": {
        "Sensitivity": [0.81, 0.80, 0.81, 0.77, 0.80, 0.77, 0.80, 0.80, 0.80, 0.81],
        "Specificity": [0.91, 0.87, 0.92, 0.94, 0.90, 0.89, 0.90, 0.92, 0.89, 0.90],
        "Accuracy": [0.85, 0.83, 0.86, 0.86, 0.85, 0.83, 0.84, 0.85, 0.84, 0.85],
        "Precision": [0.93, 0.89, 0.94, 0.92, 0.90, 0.87, 0.91, 0.93, 0.89, 0.93],
        "F1 Score": [0.86, 0.84, 0.87, 0.84, 0.85, 0.82, 0.85, 0.86, 0.84, 0.87],
        "time": [
            1.570776066,
            1.570776066,
            1.570776066,
            1.570776066,
            1.570776066,
            1.570776066,
            1.570776066,
            1.570776066,
            1.570776066,
            1.570776066,
        ],
    },
    "RFW": {
        "Sensitivity": [0.39, 0.40, 0.39, 0.40, 0.40, 0.40, 0.40, 0.40, 0.41, 0.39],
        "Specificity": [0.52, 0.51, 0.52, 0.52, 0.51, 0.51, 0.52, 0.51, 0.51, 0.52],
        "Accuracy": [0.45, 0.44, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45],
        "Precision": [0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.54, 0.53, 0.54, 0.53],
        "F1 Score": [0.45, 0.45, 0.45, 0.45, 0.45, 0.46, 0.46, 0.46, 0.46, 0.45],
        "time": [
            1.549803364,
            1.549803364,
            1.549803364,
            1.549803364,
            1.549803364,
            1.549803364,
            1.549803364,
            1.549803364,
            1.549803364,
            1.549803364,
        ],
    },
}

facenet = {
    "LFW": {
        "Sensitivity": [0.87, 0.86, 0.87, 0.83, 0.86, 0.84, 0.85, 0.86, 0.86, 0.86],
        "Specificity": [0.51, 0.46, 0.50, 0.50, 0.48, 0.44, 0.49, 0.46, 0.46, 0.46],
        "Accuracy": [0.72, 0.69, 0.72, 0.65, 0.68, 0.64, 0.70, 0.68, 0.66, 0.71],
        "Precision": [0.71, 0.68, 0.71, 0.60, 0.65, 0.60, 0.69, 0.66, 0.63, 0.72],
        "F1 Score": [0.78, 0.76, 0.78, 0.69, 0.74, 0.70, 0.76, 0.75, 0.72, 0.78],
    },
    "RFW": {
        "Sensitivity": [0.44, 0.44, 0.44, 0.44, 0.43, 0.43, 0.45, 0.44, 0.44, 0.43],
        "Specificity": [0.18, 0.18, 0.18, 0.18, 0.17, 0.17, 0.19, 0.18, 0.18, 0.18],
        "Accuracy": [0.33, 0.33, 0.33, 0.33, 0.32, 0.32, 0.34, 0.33, 0.33, 0.33],
        "Precision": [0.43, 0.42, 0.42, 0.43, 0.42, 0.42, 0.43, 0.43, 0.43, 0.42],
        "F1 Score": [0.43, 0.43, 0.43, 0.43, 0.43, 0.43, 0.44, 0.43, 0.44, 0.43],
    },
}

sFace = {
    "LFW": {
        "Sensitivity": [0.79, 0.78, 0.79, 0.74, 0.78, 0.76, 0.77, 0.79, 0.78, 0.79],
        "Specificity": [0.44, 0.42, 0.46, 0.43, 0.47, 0.40, 0.45, 0.43, 0.36, 0.44],
        "Accuracy": [0.64, 0.62, 0.65, 0.57, 0.64, 0.58, 0.63, 0.63, 0.58, 0.65],
        "Precision": [0.66, 0.64, 0.67, 0.53, 0.63, 0.56, 0.64, 0.63, 0.57, 0.69],
        "F1 Score": [0.72, 0.70, 0.73, 0.62, 0.70, 0.64, 0.70, 0.70, 0.66, 0.73],
        "time": [
            1.107519728,
            1.107519728,
            1.107519728,
            1.107519728,
            1.107519728,
            1.107519728,
            1.107519728,
            1.107519728,
            1.107519728,
            1.107519728,
        ],
    },
    "RFW": {
        "Sensitivity": [0.36, 0.36, 0.36, 0.36, 0.36, 0.36, 0.36, 0.36, 0.36, 0.36],
        "Specificity": [0.20, 0.20, 0.20, 0.21, 0.20, 0.20, 0.20, 0.19, 0.20, 0.20],
        "Accuracy": [0.29, 0.29, 0.29, 0.29, 0.29, 0.29, 0.29, 0.29, 0.29, 0.29],
        "Precision": [0.38, 0.39, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38],
        "F1 Score": [0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37],
        "time": [
            1.057181974,
            1.057181974,
            1.057181974,
            1.057181974,
            1.057181974,
            1.057181974,
            1.057181974,
            1.057181974,
            1.057181974,
            1.057181974,
        ],
    },
}

ghostFaceNet = {
    "LFW": {
        "Sensitivity": [0.76, 0.74, 0.75, 0.70, 0.73, 0.72, 0.74, 0.76, 0.75, 0.75],
        "Specificity": [0.29, 0.28, 0.31, 0.30, 0.33, 0.29, 0.30, 0.30, 0.26, 0.30],
        "Accuracy": [0.56, 0.54, 0.57, 0.49, 0.55, 0.50, 0.55, 0.55, 0.51, 0.58],
        "Precision": [0.60, 0.57, 0.61, 0.47, 0.56, 0.50, 0.58, 0.57, 0.52, 0.63],
        "F1 Score": [0.67, 0.65, 0.67, 0.57, 0.63, 0.59, 0.65, 0.65, 0.61, 0.69],
    },
    "RFW": {
        "Sensitivity": [0.36, 0.36, 0.35, 0.35, 0.36, 0.35, 0.36, 0.36, 0.36, 0.36],
        "Specificity": [0.12, 0.11, 0.12, 0.12, 0.12, 0.12, 0.11, 0.12, 0.12, 0.12],
        "Accuracy": [0.26, 0.26, 0.25, 0.26, 0.25, 0.26, 0.26, 0.26, 0.26, 0.26],
        "Precision": [0.36, 0.36, 0.35, 0.36, 0.36, 0.36, 0.36, 0.36, 0.36, 0.36],
        "F1 Score": [0.36, 0.36, 0.35, 0.35, 0.36, 0.36, 0.36, 0.36, 0.36, 0.36],
    },
}


def wilcoxon_test(model1, model2, type="greater"):
    _, p = wilcoxon(model1, model2, alternative=type)
    return p


cases = {
    "LFW": {
        "Facenet512 vs SFace": {
            "Accuracy": wilcoxon_test(
                facenet512["LFW"]["Accuracy"], sFace["LFW"]["Accuracy"]
            ),
            "F1 Score": wilcoxon_test(
                facenet512["LFW"]["F1 Score"], sFace["LFW"]["F1 Score"]
            ),
        },
        "SFace vs GhostFaceNet": {
            "Accuracy": wilcoxon_test(
                facenet512["LFW"]["Accuracy"], ghostFaceNet["LFW"]["Accuracy"]
            ),
            "F1 Score": wilcoxon_test(
                facenet512["LFW"]["F1 Score"], ghostFaceNet["LFW"]["F1 Score"]
            ),
        },
        "Facenet512 vs Facenet": {
            "Accuracy": wilcoxon_test(
                facenet512["LFW"]["Accuracy"], facenet["LFW"]["Accuracy"]
            ),
            "F1 Score": wilcoxon_test(
                facenet512["LFW"]["F1 Score"], facenet["LFW"]["F1 Score"]
            ),
        },
        "SFace vs Facenet512": {
            "time": wilcoxon_test(
                sFace["LFW"]["time"], facenet512["LFW"]["time"], type="less"
            ),
        },
    },
    "RFW": {
        "Facenet512 vs SFace": {
            "Accuracy": wilcoxon_test(
                facenet512["RFW"]["Accuracy"], sFace["RFW"]["Accuracy"]
            ),
            "F1 Score": wilcoxon_test(
                facenet512["RFW"]["F1 Score"], sFace["RFW"]["F1 Score"]
            ),
        },
        "Facenet512 vs GhostFaceNet": {
            "Accuracy": wilcoxon_test(
                facenet512["RFW"]["Accuracy"], ghostFaceNet["RFW"]["Accuracy"]
            ),
            "F1 Score": wilcoxon_test(
                facenet512["RFW"]["F1 Score"], ghostFaceNet["RFW"]["F1 Score"]
            ),
        },
        "Facenet512 vs Facenet": {
            "Accuracy": wilcoxon_test(
                facenet512["RFW"]["Accuracy"], facenet["RFW"]["Accuracy"]
            ),
            "F1 Score": wilcoxon_test(
                facenet512["RFW"]["F1 Score"], facenet["RFW"]["F1 Score"]
            ),
        },
        "SFace vs Facenet512": {
            "time": wilcoxon_test(
                sFace["RFW"]["time"], facenet512["RFW"]["time"], type="less"
            ),
        },
    },
}

for dataset in cases:
    for model in cases[dataset]:
        if "time" in cases[dataset][model]:
            print(f"{dataset} | {model} | Time: {cases[dataset][model]['time']}")
        else:
            print(
                f"{dataset} | {model} | Accuracy: {cases[dataset][model]['Accuracy']}"
            )
            print(
                f"{dataset} | {model} | F1 Score: {cases[dataset][model]['F1 Score']}"
            )
        print("--------------------------------")
