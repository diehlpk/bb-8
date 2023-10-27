# bb-8

small Python tool to extract time stamps from images using OCR

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
