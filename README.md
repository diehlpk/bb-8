# bb-8 [![DOI](https://zenodo.org/badge/710565770.svg)](https://zenodo.org/doi/10.5281/zenodo.10045857)

Small Python tool to extract time stamps from images using OCR

## Installation

The code requires [EasyOCR](https://github.com/JaidedAI/EasyOCR) to extract the text from the image.

```bash
python3 -m venv deps
source deps/bin/activate
pip install -r requirements.txt
```

## Usage

To extract the time stamp of a single image

```bash
source deps/bin/activate
python3 extract.py image.jpeg
```

To extract time stamps of multiple images

```bash
source deps/bin/activate
find . -name "*.jpg" -exec python3 extract.py "{}" ";" >> found.dat 
```

## Reference

Please cite the work as follow

Diehl, P. (2023). bb-8: Python tool to extract time stamps from images (v0.1.0). Zenodo. https://doi.org/10.5281/zenodo.10045858
