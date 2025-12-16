Fractal V1 — Mandelbrot & Burning Ship

A Python-based interactive fractal explorer built with Streamlit. Explore the intricate beauty of the Mandelbrot and Burning Ship fractals with customizable zoom and iteration settings.

Features

Interactive selection of fractal type:

Mandelbrot Set

Burning Ship Fractal

Adjustable zoom level to explore fractal details.

Customizable maximum iterations for fractal calculations.

Visual representation with a color map and dynamic axes.

Display of the current fractal bounds and zoom level.

Installation

Clone the repository:

git clone https://github.com/your-username/fractal-explorer.git
cd fractal-explorer


Install required packages:

pip install streamlit matplotlib numpy

Usage

Run the Streamlit app:

streamlit run app.py


Use the sidebar to select the fractal type.

Adjust max iterations and zoom level to explore different regions.

The plot updates in real-time.

How It Works

Fractal computation:

The Mandelbrot and Burning Ship fractals are generated using iterative algorithms.

Each pixel corresponds to a complex number and is colored based on the number of iterations before escape.

Zooming:

Zooming is implemented as a scaling factor, refining the selected region of the fractal.

Visualization:

Fractals are displayed using Matplotlib with a "hot" color map.

Example




Future Improvements

Add more fractal types (e.g., Julia set, Multibrot sets).

Enable dynamic color maps.

Add mouse-based zoom and pan interactions.

License

This project is licensed under the MIT License.
