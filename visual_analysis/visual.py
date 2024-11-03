# visual.py

from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit import Aer, execute
import matplotlib.pyplot as plt
from IPython.display import display

def plot_circuit(circuit: QuantumCircuit, title="Quantum Circuit"):
    """
    Plot the quantum circuit layout.
    """
    print(f"\n{title}")
    display(circuit.draw(output='mpl'))  # Draws the circuit with matplotlib
    plt.show()

def plot_results(results: dict):
    """
    Plot the results of the quantum circuit execution.
    
    Args:
        results (dict): Dictionary with counts for different noise levels.
    """
    for (p1, p2), counts in results.items():
        plot_histogram(counts, title=f"Results for noise levels (p1={p1}, p2={p2})")
        plt.show()

def plot_statevector(circuit: QuantumCircuit):
    """
    Visualize the Bloch sphere representation of the qubits' state vector.
    
    Args:
        circuit (QuantumCircuit): The circuit whose state vector to visualize.
    """
    state_simulator = Aer.get_backend('statevector_simulator')
    result = execute(circuit, backend=state_simulator).result()
    statevector = result.get_statevector()
    plot_bloch_multivector(statevector)
    plt.show()
