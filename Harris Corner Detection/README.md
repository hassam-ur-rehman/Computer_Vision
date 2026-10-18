# Computer Vision Assignment 1 — Harris Corner Detection

A consolidated, **executed** Jupyter notebook implementing all five assignment tasks using a custom NumPy Harris detector, together with a **three-page** experiment report, locally inspectable image assets, and generated result files.

## Deliverables

- `Harris_Corner_Detection_Complete.ipynb` — the **unchanged approved** Phase 1 notebook, including executed outputs for all five tasks.
- `report.pdf` — exactly 3 pages, written from the approved notebook's measured outputs and selected figures.
- `requirements.txt` — installation requirements.
- `images/` — the exact prepared grayscale test arrays as PNGs, included for inspection and completeness.
- `results/` — the approved execution's CSVs, visualizations, and `experiment_summary.json`. A new run regenerates these results.

## Tasks covered

1. **Filtering foundations:** custom odd-sized correlation/convolution; zero/reflect padding; Gaussian generation, Sobel and central differences, separability verification, timing versus 2D filtering, and OpenCV verification.
2. **Harris detector:** custom Sobel gradients, Gaussian structure tensor, response `R = det(M) - k * trace(M)^2`, relative threshold, fully vectorized 3x3 non-maximum suppression, and grayscale corner overlays.
3. **Eigenvalues:** closed-form tensor eigenvalues, determinant/trace consistency checks, response classes, and ratio boundaries for `k = 0.04` and `k = 0.06`.
4. **Invariance:** coordinate-mapped repeatability within 2 px under rotation, scaling, brightness, contrast, and noise, plus fixed-versus-relative threshold comparisons.
5. **Parameter study/comparison:** 360 sigma/k/threshold combinations; box-versus-Gaussian windows; custom-versus-OpenCV agreement and timings; checkerboard localization failure case.

## Quick start

Use **Python 3.11+** (run verified on Python 3.13.5).

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m ipykernel install --user --name cv-assignment-1 --display-name "CV Assignment 1"
jupyter lab
```

Open `Harris_Corner_Detection_Complete.ipynb`, select the **CV Assignment 1** kernel, and choose **Run All Cells**.

**Important:** launch Jupyter from the folder containing the notebook so that the notebook creates/refreshes `./results/` in this folder. No internet image downloads or previous task notebooks are needed. The notebook loads the sample datasets provided by the installed `scikit-image` package (rather than reading the included `images/` copies), which is intentional and preserves the approved implementation.

For headless reruns (optional):

```bash
jupyter nbconvert --to notebook --execute --inplace Harris_Corner_Detection_Complete.ipynb
```

This updates the notebook's stored results and run timings; keep a copy of the approved original if a byte-identical record is required.

## Tested run and reproducibility

The approved execution used Python **3.13.5**, NumPy **2.3.5**, OpenCV **4.13.0**, scikit-image **0.26.0**, Matplotlib **3.10.8**, seed `20261018`, default `sigma=1.5`, `k=0.04`, `relative_threshold=0.01`, Sobel derivatives, and reflect padding. The checkerboard is 10 x 10 squares (400 x 400 px) and contains 81 true interior corners. All 24 code cells executed successfully and the notebook reports 81/81 corner recovery within 1 px.

Re-executing on different hardware or package versions can change wall-clock timings; all run-specific benchmarks in `report.pdf` are from the supplied approved execution. The notebook is preserved without code changes. Its final markdown statement describing Phase 2 as 'not yet generated' is a historical Phase 1 note, not the status of this packaged deliverable.

## Image datasets, reuse, and attribution

The test images are not reused from the original five task notebooks:

| Filename | Dataset source and preparation | License / provenance |
|---|---|---|
| `structured_image.png` | `skimage.data.brick()` resized to grayscale 256 x 256 | Original brick texture from CC0Textures, CC0 (per scikit-image docstring) |
| `natural_image.png` | `skimage.data.grass()` resized to grayscale 256 x 256 | Grass artwork from DeviantArt, CC0 (per scikit-image docstring) |
| `low_contrast_image.png` | `skimage.data.coffee()` → grayscale → resize 256 x 256 → `clip(round(112 + .23 * image), 0, 255)` | Rachel Michetti / Pikolo Espresso Bar, CC0 (per scikit-image docstring) |
| `checkerboard.png` | 10 x 10 synthetic grayscale checkerboard with 40 px square width, values 30 and 170 | Generated from the assignment's checkerboard specification |

Dataset documentation: https://scikit-image.org/docs/stable/api/skimage.data.html

The PNGs are supplied as inspectable copies; the notebook directly reloads the matching scikit-image samples in its setup section. No web requests occur during notebook execution after the dependencies are installed.

## Directory structure

```text
Computer_Vision_Assignment_1/
├── Harris_Corner_Detection_Complete.ipynb
├── report.pdf
├── README.md
├── requirements.txt
├── images/
│   ├── structured_image.png
│   ├── natural_image.png
│   ├── low_contrast_image.png
│   └── checkerboard.png
└── results/
    ├── experiment_summary.json
    ├── task1_filtering/       # CSV + Gaussian speed plot
    ├── task2_harris/          # dataset and corner overlays
    ├── task3_eigenvalues/     # eigenvalue scatter plot
    ├── task4_invariance/      # curves and repeatability CSVs
    └── task5_comparison/      # parameter grid, windows, OpenCV/runtime CSVs
```

## Key findings from the approved run

- Gaussian checkerboard: **81/81** true corners found within 1 pixel (mean offset **0.707 px**).
- Identically sized 11 x 11 box window: **162** detected peaks, yet **0/81** true intersections matched within 2 pixels — a real localization failure discussed in `report.pdf`.
- Brightness +80: reference-corner repeatability remained **98.1–100%** across the three photo datasets; low-contrast noise sigma 30: **28.3%**.
- Relative detector agrees 100% with OpenCV when the custom implementation uses the same box aggregation on the three photographic images, under the stated directional matching procedure. Gaussian aggregation yields a different peak set and must not be interpreted as an implementation error.

### Implementation guardrails

The custom detector does **not** call `cv2.filter2D`, `cv2.GaussianBlur`, `cv2.Sobel`, `cv2.cornerHarris`, or SciPy filtering functions, and it does not iterate over individual image pixels. OpenCV filtering is confined to Task 1 verification, and `cv2.cornerHarris` to Task 5 comparison. Image loading, conversion, resizing and affine test transformations may use OpenCV.
