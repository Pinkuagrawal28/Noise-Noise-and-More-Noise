from qiskit import QuantumCircuit
import numpy as np

def custom_qft(n: int) -> QuantumCircuit:
    """
    Create a Quantum Fourier Transform (QFT) circuit for n qubits.
    :param n: Number of qubits
    :return: Quantum Circuit for QFT
    """
    qft_circuit = QuantumCircuit(n)
    
    for j in range(n):
        qft_circuit.h(j)  # Apply Hadamard gate
        for k in range(j + 1, n):
            qft_circuit.cp(np.pi / (2 ** (k - j)), j, k)  # Apply controlled-phase gate
    
    # Reverse the qubits to match the standard QFT output layout
    for j in range(n // 2):
        qft_circuit.swap(j, n - j - 1)
    
    return qft_circuit

def inverse_custom_qft(n: int) -> QuantumCircuit:
    """
    Create the inverse Quantum Fourier Transform (QFT) circuit for n qubits.
    :param n: Number of qubits
    :return: Quantum Circuit for inverse QFT
    """
    inv_qft_circuit = QuantumCircuit(n)
    
    # Reverse the qubits to match the original qubit layout
    for j in range(n // 2):
        inv_qft_circuit.swap(j, n - j - 1)
    
    # Apply the inverse QFT by reversing the QFT steps
    for j in reversed(range(n)):
        for k in range(j + 1, n):
            inv_qft_circuit.cp(-np.pi / (2 ** (k - j)), j, k)  # Apply inverse controlled-phase gate
        inv_qft_circuit.h(j)  # Apply Hadamard gate
    
    return inv_qft_circuit
