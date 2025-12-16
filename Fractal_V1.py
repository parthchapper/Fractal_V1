import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Fractal Explorer — Mandelbrot & Burning Ship")


fractal_type = st.sidebar.selectbox(
    "Choose fractal",
    ["Mandelbrot", "Burning Ship"]
)
# more fractals can be added here

max_iter = st.sidebar.slider("Max iterations", 20, 600, 120)

zoom = st.sidebar.slider(
    "Zoom level",
    min_value=-5,
    max_value=14,
    value=0,
    step=1,
    help="Each step zooms in by a factor of 2"
)


if fractal_type == "Mandelbrot":
    # Seahorse Valley
    cx, cy = -0.743643887037151, 0.13182590420533
    base_width = base_height = 1.5
else:
    cx, cy = -1.755, -0.03
    base_width = base_height = 1.5
# the elif can be used to add more fractals in future


scale = 2 ** (-zoom)

xmin = cx - base_width * scale
xmax = cx + base_width * scale
ymin = cy - base_height * scale
ymax = cy + base_height * scale


def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def burning_ship(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = complex(abs(z.real), abs(z.imag))**2 + c
    return max_iter

def fractal_set(xmin, xmax, ymin, ymax, width, height, max_iter, mode):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            if mode == "Mandelbrot":
                img[i, j] = mandelbrot(c, max_iter)
            else:
                img[i, j] = burning_ship(c, max_iter)

    return img


width = height = 600
data = fractal_set(
    xmin, xmax, ymin, ymax,
    width, height,
    max_iter,
    fractal_type
)

fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(
    data,
    extent=(xmin, xmax, ymin, ymax),
    cmap="hot",
    origin="lower"
)

ax.set_title(f"{fractal_type} Set")
ax.set_xlabel("Re")
ax.set_ylabel("Im")
plt.colorbar(im, ax=ax)

st.pyplot(fig)

st.caption(
    f"x ∈ [{xmin:.10f}, {xmax:.10f}] | "
    f"y ∈ [{ymin:.10f}, {ymax:.10f}] | "
    f"zoom = {zoom}"
)
