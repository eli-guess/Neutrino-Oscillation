import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Two-Flavor Oscillation Function

def oscillation_probability(E, L, theta12):

    # Fixed Value for Mass-Squared Difference (eV²)

    delta_m21 = 7.53e-5  # eV²
    
    # Degrees to Radians

    t12 = np.radians(theta12)

    # Simplified PMNS Matrix

    U = np.array([
        [np.cos(t12), np.sin(t12)],
        [-np.sin(t12), np.cos(t12)],
    ])

    # Oscillation Probabilities
    
    delta21 = 1.267 * delta_m21 * L / E

    P = np.zeros((2, 2)) 
    for alpha in range(2):
        for beta in range(2):
            if alpha != beta:
                P[alpha, beta] = (
                    -4 * np.real(U[alpha, 0] * U[beta, 1] * np.conj(U[alpha, 1]) * np.conj(U[beta, 0]))
                    * np.sin(delta21) ** 2
                )
    return P