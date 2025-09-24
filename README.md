# Cathedral Over the Chasm (v1.0 Pilot)

**Published paper:** <public_url_to_come>

##### Supplementary public repo for the COtC v1.0 paper

The published paper can be found at the following link: [TBD]

**What is this?** A minimal, offline-friendly _hello‑world_ container that demonstrates
the packaging and hashing we’ll use for the full benchmark runner in v1.1.

## Quick start

```bash
cd cathedral_hello_world_container
docker build -t cathedral-hello .
mkdir -p out
docker run --rm -it -v "$PWD/out":/app/out cathedral-hello
# Outputs: out/logs.json, out/theme.wav, out/MANIFEST.json

```
