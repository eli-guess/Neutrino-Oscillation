from oscillation import oscillation_probability
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


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

E = st.slider("Neutrino Energy (GeV)", 0.1, 10.0, 1.0)
L = st.slider("Distance Traveled (km)", 1, 10000, 500)
theta12 = st.slider("Mixing Angle $\\theta_{12}$ (degrees)", 0.0, 45.0, 33.0)

# Calculate Probabilities

L_values = np.linspace(1, 10000, 500)
P_values_L = np.zeros(len(L_values))

# Generate Probability

for i, L_val in enumerate(L_values):
    P_matrix = oscillation_probability(E, L_val, theta12)
    P_values_L[i] = P_matrix[flavor_index, (flavor_index + 1) % 2]  # Transition to next flavor

# Display Probabilitiy

P_matrix_at_E_and_L = oscillation_probability(E, L, theta12)
probability_at_E_and_L = P_matrix_at_E_and_L[flavor_index, (flavor_index + 1) % 2]  # Transition to next flavor

st.markdown(
    f"""
    <div style="text-align: center; font-size: 24px; font-weight: bold;">
        Oscillation Probability: {probability_at_E_and_L:.4f}
    </div>
    """,
    unsafe_allow_html=True,
)


# Plot Oscillation and Distance (Fixed Energy)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(L_values, P_values_L, label="Oscillation Probability")
ax.set_xlabel("Distance (L) [km]")
ax.set_ylabel("Oscillation Probability")
ax.set_title(f"Oscillation Probability of {initial_flavor} to {('Muon' if initial_flavor == 'Electron Neutrino' else 'Electron')} Neutrino")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Generate Probabilities

E_values = np.linspace(0.1, 10.0, 500)
P_values_E = np.zeros(len(E_values))

for i, E_val in enumerate(E_values):
    P_matrix = oscillation_probability(E_val, L, theta12)
    P_values_E[i] = P_matrix[flavor_index, (flavor_index + 1) % 2]  # Transition to next flavor

# Plot Probabilities and Energy

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(E_values, P_values_E, label="Oscillation Probability", color="orange")
ax.set_xlabel("Energy (E) [GeV]")
ax.set_ylabel("Oscillation Probability")
ax.set_title(f"Oscillation Probability of {initial_flavor} to {('Muon' if initial_flavor == 'Electron Neutrino' else 'Electron')} Neutrino")
ax.grid(True)
ax.legend()
st.pyplot(fig)