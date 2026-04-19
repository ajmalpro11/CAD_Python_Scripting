# RetroPad - build123d CAD Scripts

This repository contains Python scripts using **build123d** to recreate the 3D geometry of the [RetroPad](https://github.com/jtgans/RetroPad) case parts.

## 📁 Project Structure

```
retropad-build123d/
│
├── parts/
│   ├── button.py            # Script for the Button part
│   ├── dpad.py              # Script for the D-Pad part
│   ├── top_shell.py         # Script for the Top Shell part
│   └── bottom_shell.py      # Script for the Bottom Shell part
│
├── assembly/
│   └── assembly.py          # Complete assembly with all parts
│
├── validation/
│   └── validate.py          # Symmetric difference validation script
│
├── generated/
│   ├── button_generated.stl
│   ├── button_generated.step
│   └── ...                  # Other exported files
│
└── README.md
```

## 🔧 Requirements

- Python 3.11
- build123d
- ocp-vscode (for visualization)

Install dependencies:
```bash
py -3.11 -m pip install build123d
py -3.11 -m pip install ocp-vscode
```

## 📦 Parts Overview

| Part | Dimensions (mm) | Volume (mm³) |
|------|----------------|--------------|
| Button | 11.83 x 11.83 x 15.47 | 1150.78 |
| D-Pad | 32.06 x 28.41 x 15.47 | 7947.73 |
| Top Shell | 135.00 x 53.00 x 14.82 | 24154.49 |
| Bottom Shell | 135.00 x 53.00 x 19.42 | 27602.85 |

## ▶️ How to Run

**Run individual part scripts:**
```bash
py -3.11 parts/button.py
py -3.11 parts/dpad.py
py -3.11 parts/top_shell.py
py -3.11 parts/bottom_shell.py
```

**Run the full assembly:**
```bash
py -3.11 assembly/assembly.py
```

**Run validation:**
```bash
py -3.11 validation/validate.py
```

## ✅ Validation Method

Validation is performed using the **symmetric difference method**:

1. Generate the part using the build123d script
2. Import the reference STL file
3. Compute **A - B** (generated minus reference)
4. Compute **B - A** (reference minus generated)
5. Both volumes must be **zero or within negligible tolerance**

This ensures the geometries are truly identical, not just equal in volume.

## 🎮 About RetroPad

RetroPad is an open-source retro gamepad project by [jtgans](https://github.com/jtgans/RetroPad).
This repository recreates the case geometry using build123d for evaluation and educational purposes.

## 📝 Progress

- [x] Button
- [ ] D-Pad
- [ ] Top Shell
- [ ] Bottom Shell
- [ ] Assembly
- [ ] Validation Script
