from qiskit import QuantumCircuit
from qft.qft import custom_qft, inverse_custom_qft
import numpy as np

def quantum_adder(a: int, b: int, n: int) -> QuantumCircuit:
  
    """
    Create a Quantum Circuit to add two integers a and b using the Draper adder.
    :param a: First integer
    :param b: Second integer
    :param n: Number of qubits (must fit max(a, b) in binary)
    :return: Quantum Circuit that performs addition
    """

    qc = QuantumCircuit(n)

    # Initialize the qubits with the first number (a)
    for i in range(n):
        if (a >> i) & 1:
            qc.x(i)

    # Apply Custom QFT
    qc.append(custom_qft(n), range(n))

    # Add the second number (b) in Fourier space using phase shifts
    for i in range(n):
        for j in range(i, n):
            if (b >> (j - i)) & 1:
                qc.cp(np.pi / (2 ** (j - i)), i, j)

    # Apply inverse QFT
    qc.append(inverse_custom_qft(n), range(n))
  
    return qc
