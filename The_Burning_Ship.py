import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Burning Ship Fractal – Zoom Explorer")

width = 500
height = 500
max_iter = st.sidebar.slider("Max iterations", 20, 500, 100)


zoom = st.sidebar.slider(
    "Zoom level",
    min_value=-5,
    max_value=5,
    value=0,
    step=1,
    help="Each step zooms in by a factor of 2"
)


cx = -1.755
cy = -0.03


base_width = 1.5
base_height = 1.5


scale = 2 ** (-zoom)

xmin = cx - base_width * scale
xmax = cx + base_width * scale
ymin = cy - base_height * scale
ymax = cy + base_height * scale

def burning_ship(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = complex(abs(z.real), abs(z.imag))**2 + c
    return max_iter

def burning_ship_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            img[i, j] = burning_ship(c, max_iter)

    return img


data = burning_ship_set(xmin, xmax, ymin, ymax, width, height, max_iter)

fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(
    data,
    extent=(xmin, xmax, ymin, ymax),
    cmap="hot",
    origin="lower"
)

ax.set_title("Burning Ship Fractal")
ax.set_xlabel("Re")
ax.set_ylabel("Im")
plt.colorbar(im, ax=ax)

st.pyplot(fig)


st.caption(
    f"x ∈ [{xmin:.6f}, {xmax:.6f}] | "
    f"y ∈ [{ymin:.6f}, {ymax:.6f}] | "
    f"zoom = {zoom}"
)
