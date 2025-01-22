from oscillation import oscillation_probability
import streamlit as st
import numpy as np
import plotly.graph_objects as go


# Streamlit UI

st.title("Two-Flavor Neutrino Oscillation Simulation")

st.subheader("What are Neutrino Oscillations?")
st.write("""
Neutrinos oscillate between three flavor states: electron neutrino ($\\nu_e$), muon neutrino ($\\nu_\\mu$), and tau neutrino ($\\nu_\\tau$).

This phenomenon occurs because the flavor states are quantum mechanical superpositions of the mass states.

**This simulation uses a simplified two-flavor model** of neutrino oscillations, where we only consider the oscillations between two neutrino flavors: 
- Electron neutrino ($\\nu_e$)
- Muon neutrino ($\\nu_\\mu$)

In the **simplified two-flavor model** used here:
- We assume only the oscillation between two flavors (typically $\\nu_e$ and $\\nu_\\mu$).
- We use a single mixing angle ($\\theta_{12}$) to describe the transition between these two flavors, and only one mass-squared difference ($\\Delta m^2$) is involved.
""")

# Probability Equation using LaTeX

st.latex(r"""
P(\nu_\alpha \to \nu_\beta) = \sin^2(2\theta) \sin^2\left(\frac{\Delta m^2 L}{4E}\right)
""")

st.write("""
Where:
- $\\nu_\\alpha, \\nu_\\beta$: Neutrino flavors (e.g., $\\nu_e$, $\\nu_\\mu$).
- $\\theta$: The mixing angle.
- $\\Delta m^2$: Difference in the squared masses of the eigenstates.
- $L$: Distance traveled by the neutrino (km).
- $E$: Neutrino energy (GeV).
""")

# Neutrino Flavor List

st.write("The neutrino flavors are:")
st.latex(r"\nu_e, \nu_\mu")

# User Inputs

flavors = ["Electron Neutrino", "Muon Neutrino"]
initial_flavor = st.selectbox("Select Initial Neutrino Flavor", flavors, index=0)
flavor_index = flavors.index(initial_flavor)

if initial_flavor == "Electron Neutrino":
    final_flavor = "Muon Neutrino"
else:
    final_flavor = "Electron Neutrino"

E = st.slider("Neutrino Energy (GeV)", 0.1, 10.0, 1.0)
L = st.slider("Distance Traveled (km)", 1, 10000, 500)
theta12 = st.slider("Mixing Angle $\\theta_{12}$ (degrees)", 0.0, 45.0, 33.0)

# Calculate Probabilities 

L_values = np.linspace(1, 10000, 500)
E_values = np.linspace(0.1, 10.0, 500)
P_flavor = np.zeros((len(L_values), len(E_values)))

# Generate Probabilities

for i, L_val in enumerate(L_values):
    for j, E_val in enumerate(E_values):
        P_matrix = oscillation_probability(E_val, L_val, theta12)
        P_flavor[i, j] = P_matrix[flavor_index, (flavor_index + 1) % 2]

# Display Probability

P_matrix_at_E_and_L = oscillation_probability(E, L, theta12)
probability_at_E_and_L = P_matrix_at_E_and_L[flavor_index, (flavor_index + 1) % 2]  # Transition to next flavor

st.markdown(
    f"""
    <div style="text-align: center; font-size: 24px; font-weight: bold;">
        Oscillation Probability from {initial_flavor} to {final_flavor}: {probability_at_E_and_L:.4f}
    </div>
    """,
    unsafe_allow_html = True,
)
# Generate Probabilities

L_values = np.linspace(1, 10000, 500)
P_distance = np.zeros(len(L_values))

for i, L_val in enumerate(L_values):
    P_matrix = oscillation_probability(E, L_val, theta12)
    P_distance[i] = P_matrix[flavor_index, (flavor_index + 1) % 2]  # To next flavor

# Plot Oscillation and Distance (Fixed Energy)

fig_distance = go.Figure()
fig_distance.add_trace(go.Scatter(x=L_values, y=P_distance, mode='lines', name=f"Oscillation Probability"))
fig_distance.update_layout(
    title = "Oscillation Probability vs Distance (Fixed Energy)",
    title_x = 0.25,
    xaxis_title = "Distance (L) [km]",
    yaxis_title = "Oscillation Probability",
    template = "plotly_dark"
)
# Generate Probabilities

E_values = np.linspace(0.1, 10.0, 500)
P_energy = np.zeros(len(E_values))

for i, E_val in enumerate(E_values):
    P_matrix = oscillation_probability(E_val, L, theta12)
    P_energy[i] = P_matrix[flavor_index, (flavor_index + 1) % 2]  # To next flavor

# Plot Oscillation and Energy (Fixed Distance)

fig_energy = go.Figure()
fig_energy.add_trace(go.Scatter(x=E_values, y=P_energy, mode='lines', name=f"Oscillation Probability"))
fig_energy.update_layout(
    title = "Oscillation Probability vs Energy (Fixed Distance)",
    title_x = 0.275,
    xaxis_title = "Energy (E) [GeV]",
    yaxis_title = "Oscillation Probability",
    template = "plotly_dark"
)

# Remove Plot Titles on Mobile
custom_css = """
<style>
/* Hide the Plotly titles on mobile (screens smaller than 600px) */
@media only screen and (max-width: 600px) {
    .plotly-graph-div .gtitle {
        display: none !important;
    }
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Display Plots

st.plotly_chart(fig_distance, use_container_width=True)
st.plotly_chart(fig_energy, use_container_width=True)
