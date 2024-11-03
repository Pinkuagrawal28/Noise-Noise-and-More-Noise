import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import RZGate, SXGate, XGate, CXGate

def transform_to_basis(qc: QuantumCircuit) -> QuantumCircuit:
    """
    Transform gates in a Quantum Circuit to {CX, ID, RZ, SX, X}.
    :param qc: Original Quantum Circuit
    :return: Quantum Circuit with only the allowed gate basis
    """
    transformed_qc = QuantumCircuit(*qc.qregs)
    
    for instr in qc.data:
        operation = instr.operation  # Get the operation
        qargs = instr.qubits          # Get the qubits
        
        if operation.name == 'h':
            # Replace Hadamard with RZ and SX (approximate decomposition)
            transformed_qc.rz(np.pi / 2, qargs[0])
            transformed_qc.sx(qargs[0])
            transformed_qc.rz(np.pi / 2, qargs[0])
        elif operation.name == 't':
            # Replace T with an RZ gate
            transformed_qc.rz(np.pi / 4, qargs[0])
        elif operation.name == 'cx':
            transformed_qc.cx(qargs[0], qargs[1])
        else:
            transformed_qc.append(operation, qargs)
    
    return transformed_qc
