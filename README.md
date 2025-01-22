# Neutrino Oscillation Simulator

## Overview

Try it out: https://neutrino-osc.streamlit.app/

The **Neutrino Oscillation Simulator** is a web-based application built using Python and Streamlit to visualize the phenomenon of neutrino oscillations. Neutrino oscillation is a quantum mechanical process in which neutrinos change their flavor (e.g., from electron neutrino to muon neutrino) as they travel. This simulator uses a simplified two-flavor model to demonstrate the relationship between key parameters, such as energy, distance, and oscillation probability.

---

## Features
1. **Interactive Visualizations**:
   - Two 2D graphs to show oscillation probability:
     - **Probability vs. Distance**: For a fixed neutrino energy.
     - **Probability vs. Energy**: For a fixed travel distance.
   - Users can adjust parameters like energy and distance to see real-time changes in the graphs.

2. **Customization Options**:
   - Set neutrino energy (in GeV) using a slider.
   - Set the baseline distance traveled by the neutrino (in km).

3. **Clear Explanations**:
   - Provides a brief introduction to neutrino oscillations and their underlying physics.
   - Displays the oscillation probability equation and defines its components.

4. **Oscillation Probability Display**:
   - Calculates and displays the precise oscillation probability for user-selected parameters.

---

## Installation and Setup
### Prerequisites
- Python 3.9 or later
- Streamlit
- NumPy
- Matplotlib

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/eli-guess/neutrino-oscillation.git
   ```
2. Install the required packages:
   ```
   pip install requirements.txt
   ```
3. Run the application:
   ```
   streamlit run neutrino_app.py
   ```
## Usage
1. Launch the app and explore the parameter sliders to modify:
- Neutrino energy (𝐸)
- Distance traveled (𝐿).

2. Observe how the oscillation probability changes in the two provided graphs:
- Probability vs. Distance: Examines the impact of baseline length on oscillation for a fixed energy.
- Probability vs. Energy: Examines the effect of energy for a fixed baseline distance.
  
3. Review the calculated probability for the selected parameters displayed prominently in the app.

## License
This project is licensed under the MIT License.
