# main.py

from qiskit import QuantumCircuit, Aer, execute
from visual_analysis.visual import plot_circuit, plot_results, plot_statevector  # Import the visualization functions
from draper_adder.drapper_adder import quantum_adder  # Import the Draper adder function
from noise_model.noise import add_pauli_noise  # Import the noise function
from qft.qft import custom_qft, inverse_custom_qft  # Import QFT functions
from gate_basis.transform_to_basis.py import transform_to_basis  # Import the gate conversion function

def analyze_quantum_addition_with_noise(a, b, noise_levels):
    """Analyze the quantum addition circuit under different noise levels.

    Args:
        a (int): First number to add.
        b (int): Second number to add.
        noise_levels (list of tuples): List of noise level tuples (p1, p2).

    Returns:
        dict: Results of counts for each noise level.
    """
    results = {}

    for p1, p2 in noise_levels:
        # Create the quantum adder circuit
        n = max(a.bit_length(), b.bit_length()) + 1  # Number of qubits needed
        qc = quantum_adder(a, b, n)

        # Convert the circuit to the basis gates
        transformed_qc = transform_to_basis(qc)  # Transform the circuit to the basis gates
        
        # Add noise to the circuit
        noisy_qc = add_pauli_noise(transformed_qc, p_single=p1, p_double=p2)

        # Simulate and get state vector
        simulator = Aer.get_backend('statevector_simulator')  # Use statevector simulator
        state_job = execute(noisy_qc, backend=simulator)
        state_vector = state_job.result().get_statevector()  # Retrieve state vector
        
        # Plot the state vector using your custom visualization
        plot_statevector(state_vector, title=f"State Vector with Noise p1={p1}, p2={p2}")

        # Measure the noisy circuit
        noisy_qc.measure_all()
        job = execute(noisy_qc, backend=Aer.get_backend('qasm_simulator'), shots=1000)
        result = job.result()
        counts = result.get_counts()
        
        # Store results for analysis
        results[(p1, p2)] = counts
        plot_circuit(noisy_qc, title=f"Quantum Adder Circuit with Noise p1={p1}, p2={p2}")
    
    return results

if __name__ == "__main__":
    noise_levels = [(0.01, 0.01), (0.05, 0.05), (0.1, 0.1), (0.2, 0.2)]  # Define noise levels
    results = analyze_quantum_addition_with_noise(3, 5, noise_levels)  # Example: Adding 3 and 5

    # Visualize the results
    plot_results(results)
