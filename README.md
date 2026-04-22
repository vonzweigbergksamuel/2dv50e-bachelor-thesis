# Face Identification Experiments (Bachelor Thesis)

This repository contains experimental work for a bachelor thesis at Linnaeus University.  
The project evaluates face recognition models from the DeepFace framework in a face identification setting.

- Samuel von Zweigbergk (sv222rr)
- Ludwig Wittenberg (lw223cq)

## Thesis

Add your thesis link here: `[Thesis title](https://example.com)`

## Repository Structure

- `src/main.py`: entrypoint for running all dataset/model/trial experiments.
- `src/config.py`: experiment settings (models, trials, detector backend, output files).
- `src/services/`: preprocessing, splitting, running, scoring, DB operations, and output writing.
- `src/lib/`: DB connection, model download, and seed generation helpers.
- `adapters/`: scripts for adapting external datasets into the expected folder format, including adapters for LFW and RFW.
- `data/`: datasets used during experiments (one dataset per subfolder).
- `compose.yaml`: PostgreSQL service used during experiments.
- `results.txt` and `google_sheet.txt`: output artifacts written during each run.

## Prerequisites

- Python 3.11+
- `uv`
- Docker + Docker Compose (for PostgreSQL)

## Quick Start

1. Install dependencies:

```bash
uv sync
```

1. Configure environment variables in `.env`:

```env
DEEPFACE_POSTGRES_URI="postgresql://postgres:postgres@localhost:5432/deepface"
```

1. Start PostgreSQL:

```bash
docker compose up -d postgres
```

1. Run the experiment:

```bash
uv run ./src/main.py
```

1. Stop PostgreSQL when done:

```bash
docker compose down
```

## Environment Variables

- `DEEPFACE_POSTGRES_URI` (required): connection string for PostgreSQL used by the experiment.
- If missing, the app raises an error during startup (`DEEPFACE_POSTGRES_URI is not set`).

## Configuration (`src/config.py`)

All settings currently defined in `src/config.py`:

- `MODELS`: list of DeepFace model identifiers to benchmark (for example `["Facenet512"]`).
- `DETECTOR_BACKEND`: face detector backend used by DeepFace (for example `"retinaface"`).
- `TRIALS`: number of trials per model and dataset.
- `RESULTS_FILE`: filename for detailed run output (`results.txt`).
- `GOOGLE_SHEET_FILE`: filename for export-friendly output (`google_sheet.txt`).
- `UNKNOWN`: label used for unknown identities.
- `IMAGE_EXTENSIONS`: allowed image file extensions when loading dataset images.

## Outputs

- Results are written to `results.txt` and `google_sheet.txt` in the project root.
- At startup, both files are recreated/cleared.
- During execution, dataset headers, model headers, metrics, and export rows are appended.

## Test Data Recommendation

- This repository does not provide the full [LFW](https://www.kaggle.com/datasets/jessicali9530/lfw-dataset/data) or [RFW](http://whdeng.cn/RFW/testing.html) datasets.
- Download LFW/RFW separately and use the adapters in `adapters/` to prepare them.
- For easier testing, a very small sample dataset is provided in `data/dataset`.
- If you include real face images, verify dataset/license redistribution terms first.

## Lint and Format

Lint:

```bash
uvx ruff check
```

Format:

```bash
uvx ruff format
```

