# Data Requirements and Adapters

This project does not include full LFW/RFW datasets. Add datasets under `data/` before running experiments.

## Dataset Requirements

- One folder per identity.
- At least 2 valid images per identity.
- Supported extensions: `.jpg`, `.jpeg`, `.png`, `.webp`.
- Non-image files are removed by adapters.

The experiment runner reads datasets from:

```text
data/
  <dataset_name>/
    <identity_name>/
      image1.jpg
      image2.jpg
```

## LFW Structure and Adapter

Expected raw LFW placement:

```text
data/
  LFW/
    lfw-deepfunneled/
      lfw-deepfunneled/
        <identity_name>/
          image1.jpg
          image2.jpg
```

Run:

```bash
uv run .\adapters\lfw-adapter.py
```

What it does:
- removes non-image files inside identity folders
- removes identities with fewer than 2 images

## RFW Structure and Adapter

Expected raw RFW placement:

```text
data/
  RFW/
    <group_folder>/
      <identity_name>/
        image1.jpg
        image2.jpg
```

Run:

```bash
uv run .\adapters\rfw-adapter.py
```

What it does:
- removes non-image files
- removes identities with fewer than 2 images
- flattens group folders so identities end up directly under `data/RFW/`

