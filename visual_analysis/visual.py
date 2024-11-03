# visual.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit import execute
from qiskit_aer import Aer
import matplotlib.pyplot as plt
from IPython.display import display
from qiskit.visualization import plot_state_qsphere

# Function to plot the circuit
def plot_circuit(qc, title="Quantum Circuit"):
    """
    Plot the quantum circuit.
    """
    qc.draw('mpl')
    plt.title(title)
    plt.show()

# Function to plot results

def plot_results(results, a, b):
    """
    Plot the results of the quantum addition analysis as a heatmap.
    """
    # Unique noise levels
    p1_values = sorted(set(p1 for (p1, p2) in results.keys()))
    p2_values = sorted(set(p2 for (p1, p2) in results.keys()))

    # Initialize a 2D array to hold the error rates
    error_rates = np.zeros((len(p1_values), len(p2_values)))

    for i, p1 in enumerate(p1_values):
        for j, p2 in enumerate(p2_values):
            if (p1, p2) in results:
                counts = results[(p1, p2)]
                expected_outcome = f"{a + b:04b}"  # Assuming a+b fits in 4 bits
                error = counts.get(expected_outcome, 0)  # Get count for expected outcome
                error_rates[i, j] = 1 - (error / 1000)  # Calculate error rate
            else:
                error_rates[i, j] = np.nan  # If no data, set NaN for plotting

    # Create the heatmap
    plt.figure(figsize=(8, 6))
    plt.imshow(error_rates, interpolation='nearest', cmap='Blues', 
               extent=[min(p2_values), max(p2_values), min(p1_values), max(p1_values)],
               aspect='auto', origin='lower')

    plt.colorbar(label='Error Rate')
    plt.xlabel("Noise Probability (p2)")
    plt.ylabel("Noise Probability (p1)")
    plt.title("Quantum Addition Error Rate vs Noise Levels")
    plt.xticks(p2_values)  # Set x-ticks to p2 values
    plt.yticks(p1_values)  # Set y-ticks to p1 values
    plt.savefig('quantum_addition_error_heatmap.png')
    plt.show()

# Function to plot the state vector
def plot_statevector(state_vector, title="State Vector"):
    """
    Plot the state vector using a bar chart.
    """
    # Convert the state vector to a numpy array
    state_vector_np = np.array(state_vector)  # Convert to a NumPy array if needed
    plt.bar(range(len(state_vector_np)), abs(state_vector_np) ** 2)  # Plot the probabilities
    plt.title(title)
    plt.xlabel('Basis States')
    plt.ylabel('Probability Amplitude Squared')
    plt.xticks(range(len(state_vector_np)), [f"|{i}> " for i in range(len(state_vector_np))])
    plt.show()
