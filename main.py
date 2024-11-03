# main.py

from qiskit import QuantumCircuit, execute, transpile
from qiskit_aer import Aer
from visual_analysis.visual import plot_circuit, plot_results, plot_statevector  # Import the visualization functions
from draper_adder.drapper_adder import quantum_adder  # Import the Draper adder function
from noise_model.noise import add_pauli_noise  # Import the noise function
from qft.qft import custom_qft, inverse_custom_qft  # Import QFT functions
from gate_basis.transform_to_basis.py import transform_to_basis  # Import the gate conversion function

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
        # Create the quantum adder circuit
        qc = quantum_adder(a, b, n)
        
        # Convert the circuit to the basis gates
        transformed_qc = transform_to_basis(qc)  # Transform the circuit to the basis gates
        
        # Add noise to the circuit
        noisy_qc = add_pauli_noise(transformed_qc, p_single=p1, p_double=p2)
        
        print(f"Quantum Adder Circuit with Noise p1={p1}, p2={p2}")
        print(noisy_qc.draw())
        
        # Simulate and get state vector
        simulator = Aer.get_backend('statevector_simulator')  # Use statevector simulator
        compiled_circuit = transpile(noisy_qc, simulator)  # Compile the circuit for the simulator
        state_job = simulator.run(compiled_circuit)  # Execute the compiled circuit
        state_vector = state_job.result().get_statevector()  # Retrieve state vector
        
        
        # Plot the state vector using your custom visualization
        plot_statevector(state_vector, title=f"State Vector with Noise p1={p1}, p2={p2}")
        
        # Measure the noisy circuit
        noisy_qc.measure_all()
        compiled_measurement_circuit = transpile(noisy_qc, simulator)  # Compile measurement circuit
        job = simulator.run(compiled_measurement_circuit, shots=1000)  # Execute measurement
        result = job.result()
        counts = result.get_counts()
        
        # Store results for analysis
        results[(p1, p2)] = counts
        
         # Print and visualize the counts
        print(f"\nResults for noise levels p1={p1}, p2={p2}:")
        for outcome, count in counts.items():
            print(f"Outcome {outcome}: {count} times")
            
    return results

# Step 5: Run the analysis with specified noise levels
if __name__ == "__main__":
    noise_levels = [(0.01, 0.01), (0.05, 0.01), (0.1, 0.01), (0.01, 0.05), (0.05, 0.05), (0.1, 0.1)]  # Define noise levels
    results = analyze_quantum_addition_with_noise(3, 5, noise_levels)  # Example: Adding 3 and 5

    # Visualize the results
    plot_results(results,3,5)
