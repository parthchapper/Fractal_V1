import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Mandelbrot Set – Zoom Explorer")

# ======================
# CONTROLS
# ======================
max_iter = st.sidebar.slider("Max iterations", 20, 500, 100)

zoom = st.sidebar.slider(
    "Zoom level",
    min_value=0,
    max_value=12,
    value=0,
    step=1,
    help="Each step zooms in by a factor of 2"
)

# ======================
# INTERESTING CENTER
# (Classic Seahorse Valley)
# ======================
cx = -0.743643887037151
cy =  0.13182590420533

# Base window (classic Mandelbrot view)
base_width = 1.5
base_height = 1.5

# Exponential zoom
scale = 2 ** (-zoom)

xmin = cx - base_width * scale
xmax = cx + base_width * scale
ymin = cy - base_height * scale
ymax = cy + base_height * scale

# ======================
# MANDELBROT FUNCTIONS
# ======================
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            img[i, j] = mandelbrot(c, max_iter)

    return img

# ======================
# RENDER
# ======================
width = height = 500
data = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(
    data,
    extent=(xmin, xmax, ymin, ymax),
    cmap="hot",
    origin="lower"
)

ax.set_title("Mandelbrot Set")
ax.set_xlabel("Re")
ax.set_ylabel("Im")
plt.colorbar(im, ax=ax)

st.pyplot(fig)

# ======================
# DEBUG / INFO
# ======================
st.caption(
    f"x ∈ [{xmin:.8f}, {xmax:.8f}] | "
    f"y ∈ [{ymin:.8f}, {ymax:.8f}] | "
    f"zoom = {zoom}"
)
