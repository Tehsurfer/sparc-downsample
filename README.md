# sparcdownsample
[![PyPI version](https://badge.fury.io/py/sparcdownsample.svg)](https://badge.fury.io/py/sparcdownsample)
[![Maintainability](https://api.codeclimate.com/v1/badges/e56749ed3f48d58e09a7/maintainability)](https://codeclimate.com/github/Tehsurfer/sparc-downsample/maintainability)

### Sparc Downsample

A python tool for confirming downsample rates with researchers

## Installation 

`pip install sparcdownsample`

_sparcdownsample requires python 3.3+_

# Usage


The commands below will create and open a render of the data at 1/10th of original points
```
python -m sparcdownsample <my-file-name-or-path>
```
Modify the sample rate with:
```
python -m sparcdownsample <my-file-name-or-path> <downsample-factor>
```
_Example_
```
python -m sparcdownsample bigdata.csv 10
```
![image](https://user-images.githubusercontent.com/37255664/74894849-fbcf1680-53f4-11ea-92f4-c789c835176c.png)



