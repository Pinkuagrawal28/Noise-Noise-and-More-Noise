# main.py

from qiskit import QuantumCircuit, Aer, execute, transpile
from visual_analysis.visual import plot_circuit, plot_results, plot_statevector  # Import the visualization functions
from draper_adder.drapper_adder import quantum_adder  # Import the Draper adder function
from noise_model.noise import add_pauli_noise  # Import the noise function
from qft.qft import custom_qft, inverse_custom_qft  # Import QFT functions
from gate_basis.transform_to_basis import transform_to_basis  # Import the gate conversion function

# Step 4: Define the analysis function
def analyze_quantum_addition_with_noise(a, b, noise_levels):
    """
    Analyze the quantum addition circuit under different noise levels.
    """
    results = {}
    n = max(a.bit_length(), b.bit_length()) + 1  # Number of qubits needed
    print("Quantum Adder Circuit:")
    qc = quantum_adder(a, b, n)
    print(qc.draw())

    print("Quantum Adder Circuit After Basis Transformation:")
    transformed_qc = transform_to_basis(qc)
    print(transformed_qc.draw())

    for p1, p2 in noise_levels:
        # Create and transform the quantum adder circuit
        noisy_qc = add_pauli_noise(transformed_qc, p_single=p1, p_double=p2)
        
        print(f"Quantum Adder Circuit with Noise (p1={p1}, p2={p2}):")
        print(noisy_qc.draw())
        
        # Simulate and get the state vector
        simulator = Aer.get_backend('statevector_simulator')
        compiled_circuit = transpile(noisy_qc, simulator)
        state_job = execute(compiled_circuit, backend=simulator)
        state_vector = state_job.result().get_statevector()

        # Plot the state vector
        plot_statevector(state_vector, title=f"State Vector with Noise (p1={p1}, p2={p2})")
        
        # Measure the noisy circuit
        noisy_qc.measure_all()
        compiled_measurement_circuit = transpile(noisy_qc, simulator)
        job = execute(compiled_measurement_circuit, backend=simulator, shots=1000)
        result = job.result()
        counts = result.get_counts()
        
        # Store results for analysis
        results[(p1, p2)] = counts

        # Print and visualize the counts
        print(f"\nResults for noise levels (p1={p1}, p2={p2}):")
        for outcome, count in counts.items():
            print(f"Outcome {outcome}: {count} times")
            
    return results

# Step 5: Run the analysis with specified noise levels
if __name__ == "__main__":
    noise_levels = [(0.01, 0.01), (0.05, 0.01), (0.1, 0.01), (0.01, 0.05), (0.05, 0.05), (0.1, 0.1)]  # Define noise levels
    results = analyze_quantum_addition_with_noise(3, 5, noise_levels)  # Example: Adding 3 and 5

    # Visualize the results
    plot_results(results, 3, 5)
