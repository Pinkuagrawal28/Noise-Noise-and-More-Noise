# Noise-Noise-and-More-Noise

Q.) One of the main challenges in quantum computing is the noise in current devices. In this task, you will create a simple noise generator and assess its effect. You can use any framework you like (Qiskit, Cirq, etc..)

> Note : To View the report and graphs, Use the Result Directory

This project simulates and analyzes a quantum addition circuit using the Draper adder, transformed to basis gates and subjected to varying noise levels. The circuit utilizes Quantum Fourier Transform (QFT) for addition, and we investigate its performance under different noise conditions, visualizing the error rates and state vectors.

Project Structure : 

```
.
├── basic_gates/
│   └── transform_to_basis.py
├── draper_adder/
│   └── draper_adder.py
├── noise_model/
│   └── noise.py
├── qft/
│   └── qft.py
├── results
├── visual_analysis/
│   └── visual.py
├── README.md
├── main.py
└── quantum_noise_analysis.ipynb
```
### Requirements : 

To run this project, you’ll need:
  - Python 3.8 or above
  - Qiskit for quantum circuit creation and simulation, qiskit-aer
  - Matplotlib for data visualization
  - numpy

Install dependencies with:
```
pip install qiskit matplotlib
```

### Usage : 

To run the quantum addition analysis with noise, execute main.py:
```bash
python main.py
```
This script will:
  - Print and plot the original and transformed circuits.
  - Simulate the circuit under different noise levels and visualize the state vector.
  - Plot error rates vs. noise levels in a heatmap.


### Modules : 
1. Draper Adder (draper_adder/drapper_adder.py)
Implements the Draper quantum adder circuit, which uses the Quantum Fourier Transform (QFT) for addition. Given two integers a and b, the circuit computes their sum in binary.

2. Gate Basis Transformation (gate_basis/transform_to_basis.py)
Transforms the quantum circuit into a set of basis gates (e.g., CX, U3), making it compatible with real quantum hardware.

3. Noise Model (noise_model/noise.py)
Adds configurable Pauli noise (bit-flip and phase-flip errors) to simulate realistic quantum hardware conditions. This helps analyze the circuit's robustness to noise.

4. Quantum Fourier Transform (qft/qft.py)
Contains implementations of both the Quantum Fourier Transform (QFT) and its inverse. QFT is essential for the quantum adder.

5. Visualization (visual_analysis/visual.py)
Contains functions for visualizing quantum circuits, plotting state vectors, and displaying error rates in a heatmap.

#### Main Script : 
The main script integrates all modules to create a quantum addition circuit, apply noise, and visualize results.
Key steps include:
1. Create the Quantum Adder Circuit: Generate the circuit using `quantum_adder` for the given inputs `a` and `b`.
2. Transform to Basis Gates: Use `transform_to_basis` to convert the circuit to basic gates compatible with noisy quantum hardware.
3. Add Noise: Apply varying levels of Pauli noise with `add_pauli_noise`.
4. Simulate and Visualize: Run the circuit on the statevector simulator, measure outcomes, and plot the results.

### Visualization : 
  - *State Vector*: Shows the probability amplitude squared for each basis state in the presence of noise.
  - *Error Rate Heatmap*: Displays the error rate as a function of noise levels, providing insights into the circuit's robustness to noise.

### Example Output : 
The script analyzes quantum addition of two integers (e.g., 3 + 5), displaying the circuit and results for various noise levels (p1 and p2). It generates a heatmap of error rates based on different noise probabilities.

### Customizing the Analysis : 
To change the analyzed integers or noise levels, update these parameters in main.py
```python
a = 3  # First integer
b = 5  # Second integer
noise_levels = [(0.01, 0.01), (0.05, 0.01), (0.1, 0.01), ...]  # Noise probabilities
```
#### Future Scope : 
1. Testing on Various Models of Noise
2. Testing on Different Types of Circuits and Comparative analysis
3. Making a Web Application via Django for simplify Usage

## Results and Conclusion
The quantum addition circuit, implemented using the Draper adder, was transformed into a specific gate basis suitable for execution on quantum hardware. Once transformed, noise was systematically introduced to simulate realistic operational conditions.

```
Results for noise levels p1=0.01, p2=0.01:
Outcome 0011: 810 times
Outcome 1101: 8 times
Outcome 0010: 27 times
Outcome 1011: 19 times
Outcome 0001: 11 times
Outcome 1111: 7 times
Outcome 0111: 15 times
Outcome 0000: 29 times
Outcome 0100: 8 times
Outcome 0110: 21 times
Outcome 0101: 17 times
Outcome 1001: 14 times
Outcome 1100: 2 times
Outcome 1110: 1 times
Outcome 1000: 11 times
```
![quantum_addition_error_heatmap](https://github.com/user-attachments/assets/508fe87e-e82b-4685-8c83-a6500023599a)
