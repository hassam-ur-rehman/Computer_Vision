
# Computer Vision

A lab-work repository covering image loading, filtering, and pixel/color
manipulation using OpenCV.

## Repository Structure

```
Computer_Vision/
├── Files/
│   └── images.py
├── Images/
│   └── cat 1.webp, cat 2.jpg, ...
├── lab3/
│   └── filtering.py
└── README.md
```

## `Files/images.py`

A minimal script that loads an image from the `Images/` folder with
`cv2.imread()`, prints its shape, and displays it in a window with
`cv2.imshow()`. It's the starting point for confirming OpenCV can read image
files correctly before any processing is applied.

## `Images/`

Contains the sample images used throughout `lab3/filtering.py` (cat photos), loaded
either from local paths or directly from this repository's raw GitHub URLs.

## `lab3/filtering.py`

A Python script covering the following exercises:

### Image Filtering
- **Load & display** — reads the image with `cv2.imread()` and converts
  BGR → RGB for correct display in Matplotlib.
- **Blur filter** — applies `cv2.blur()` to smooth the image by averaging
  neighboring pixels.
- **Gaussian filter** — applies `cv2.GaussianBlur()` for a smoother,
  weighted blur that better preserves edges than a plain mean blur.
- **Global thresholding** — converts the image to grayscale and applies
  `cv2.threshold()` to produce a binary (black/white) image.

### Lab Task: Pixel Manipulation

- **Task 1 — Pixel Value Modification:** loads a grayscale image and
  manually sets a specific pixel's intensity (e.g. pixel (50, 50) → 255) to
  observe how single-pixel edits affect the image.
- **Task 2 — Color Channel Manipulation:** splits an RGB image into its Red,
  Green, and Blue channels with `cv2.split()`, modifies one channel (e.g.
  zeroing Green), and recombines them with `cv2.merge()` to see how each
  channel contributes to the final color.
- **Task 3 — Sharpening Filter (unsharp masking):** blurs the image to get a
  smoothed version, subtracts it from the original to isolate the "details"
  (edges/fine texture), then adds those details back onto the original to
  enhance sharpness. Uses `cv2.subtract()`/`cv2.add()` rather than plain
  `-`/`+` so pixel values clip to the valid 0–255 range instead of wrapping.

## Running `lab3/filtering.py`

The script mounts Google Drive for local file access (when run in Colab),
but images can also
be pulled directly from this repo using the raw GitHub URL, e.g.:

```python
import urllib.request
import numpy as np
import cv2

url = 'https://raw.githubusercontent.com/hassam-ur-rehman/Computer_Vision/<commit>/images/cat%201.webp'
resp = urllib.request.urlopen(url)
img_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
```

Note: use `raw.githubusercontent.com` links (not `github.com/.../blob/...`
page links), and URL-encode spaces in filenames as `%20`.

If running locally rather than in Colab, `drive.mount()` isn't needed —
just point image paths at the `Images/` folder directly. Each `plt.show()`
call will open a Matplotlib window as the script runs.
