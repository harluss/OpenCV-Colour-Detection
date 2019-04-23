# OpenCV Colour Detection in Python

A python scrypt using OpenCV library to detect blobs of selected colour in webcam's feed.

The purpose of this project was to get familiar with OpenCV's color detection and filtering.

### Usage

"HSV Values" window provides sliders to change Low and High values of Hue, Saturation and Value (default set to Red-ish, but results may vary depending on lighting conditions).

### Requires
```
python_version = "3.6.6"
```
### Packages
```
numpy = "*"
opencv-python = "*"
```

To install packages and create virtual environment via [Pipenv](https://github.com/pypa/pipenv), go to the folder containing the scrypt and run:
```
pipenv install
```
And then to run the script:
```
pipenv run python colour_detect.py
```