# Cathedral Hello‑World Container (Skeleton)

This is a minimal, offline‑friendly container that demonstrates the reproducibility pattern for the benchmark.

## Build
```bash
docker build -t cathedral-hello .
```

## Run
```bash
docker run --rm -it -v "$PWD/out":/app/out cathedral-hello
```

Outputs will appear in `./out/`:
- `logs.json` — a toy trace with 10 seeds
- `theme.wav` — a one‑second tone (placeholder for THEME artifact)
- `MANIFEST.json` — file hashes and versions

Notes:
- This does not include the full simulator/VM; it is a skeleton to standardize packaging and logs for v1.0.
- v1.1 will ship a full containerized runner using the same entrypoint (`run_eval.sh`).
