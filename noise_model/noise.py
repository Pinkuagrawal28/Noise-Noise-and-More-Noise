import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit import Gate

def add_pauli_noise(qc: QuantumCircuit, p_single: float, p_double: float) -> QuantumCircuit:
    """
    Add Pauli noise to a quantum circuit.
    
    :param qc: Quantum Circuit where noise will be added
    :param p_single: Probability of adding noise after a single-qubit gate
    :param p_double: Probability of adding noise after a two-qubit gate
    :return: Quantum Circuit with added noise
    """
    
    noisy_qc = QuantumCircuit(qc.num_qubits)
    for instr, qargs, cargs in qc.data:
        # Add the original gate to the new circuit
        noisy_qc.append(instr, qargs, cargs)

        # Check if the gate is single or two-qubit and add noise accordingly
        if len(qargs) == 1 and np.random.rand() < p_single:
            noisy_qc = add_random_pauli(noisy_qc, qargs[0].index)
        elif len(qargs) == 2 and np.random.rand() < p_double:
            noisy_qc = add_random_pauli(noisy_qc, qargs[0].index)
            noisy_qc = add_random_pauli(noisy_qc, qargs[1].index)
    
    return noisy_qc

def add_random_pauli(qc: QuantumCircuit, qubit: int) -> QuantumCircuit:
    """
    Apply a random Pauli (X, Y, Z) gate to a specific qubit in the circuit.
    
    :param qc: Quantum Circuit to which the Pauli gate will be added
    :param qubit: The qubit index to which the noise will be applied
    :return: Quantum Circuit with the added Pauli noise on the specified qubit
    """
    
    pauli_gate = np.random.choice(['x', 'y', 'z'])
    if pauli_gate == 'x':
        qc.x(qubit)
    elif pauli_gate == 'y':
        qc.y(qubit)
    elif pauli_gate == 'z':
        qc.z(qubit)
    
    return qc
