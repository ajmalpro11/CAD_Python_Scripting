# RetroPad - build123d CAD Scripts

Python scripts using **build123d** to recreate the 3D geometry 
of the [RetroPad](https://github.com/jtgans/RetroPad) case parts.

## Parts
| Part | Dimensions (mm) | Volume (mm³) | Status |
|------|----------------|--------------|--------|
| Button | 11.83 x 11.83 x 15.47 | 1150.78 | ✅ Done |
| D-Pad | 32.06 x 28.41 x 15.47 | 7947.73 | 🔄 In Progress |
| Top Shell | 135.00 x 53.00 x 14.82 | 24154.49 | ⏳ Pending |
| Bottom Shell | 135.00 x 53.00 x 19.42 | 27602.85 | ⏳ Pending |

## Requirements
- Python 3.11
- build123d
- ocp-vscode

## Install
pip install build123d
pip install ocp-vscode

## Run
py -3.11 button.py
py -3.11 dpad.py
py -3.11 validate.py

## Validation Method
Symmetric difference between generated and reference STL.
Both A-B and B-A volumes must be zero or near zero.
