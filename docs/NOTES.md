# Notes

How each demo is built, what to look for in its figures, and the numbers I got. Qubit order follows Qiskit: qubit 0 is the rightmost bit in every bitstring.

## Bloch gallery (`bloch_gallery.py`)

One qubit starting in |0⟩, one gate at a time. X and Y take it to the south pole; H puts it on the equator, and then Z, S and T only rotate it around the vertical axis by π, π/2 and π/4. That last group is the useful one to look at: those gates change the phase, which the measurement histogram never shows but the sphere does.

## Bell states (`bell_states.py`)

H on qubit 0 followed by CNOT gives |Φ+⟩. The other three come from adding X before the H (sign flip) or X on qubit 1 (swaps 00/11 for 01/10). The histograms of Φ+ and Φ− are identical, both ~50/50 between 00 and 11. Only the density-matrix plot (`*_city.png`) shows the difference, in the sign of the off-diagonal terms.

## GHZ (`ghz_state.py`)

Same idea as Φ+ extended to 5 qubits: H on qubit 0 and a chain of CNOTs. Out of 4096 shots I got 2078 × `00000` and 2018 × `11111`, nothing else.

## Teleportation (`teleportation.py`)

Qubit 0 holds the state to send, Ry(π/3) then Rz(π/5). Qubits 1 and 2 share a Bell pair. After Alice's CNOT + H and her two measurements, Bob applies X and Z conditioned on those bits (`if_test`, so the corrections happen inside the circuit, not in post-processing).

Check: for Ry(π/3), P(1) = sin²(π/6) = 0.25. Bob's qubit came out 1 in 975 of 4096 shots (23.8%), whatever Alice measured. The Rz does not change that probability, only the phase.

## Deutsch–Jozsa (`deutsch_jozsa.py`)

4 input qubits plus one ancilla prepared in |−⟩. The constant oracle does nothing (or flips the ancilla); the balanced one is f(x) = x·s with CNOTs from the selected input qubits to the ancilla. One oracle call is enough: the constant case gives `0000` in all 2048 shots, the balanced case gives `1010`, which is exactly the pattern s used by the oracle.

## Grover (`grover.py`)

N = 16 states, one marked (`1010`). The oracle wraps a multi-controlled Z with X gates on the positions where the target has a 0; the diffuser is the same construction around |0000⟩, between two layers of H. The number of iterations is ⌊(π/4)√16⌋ = 3. With 4096 shots the marked state appears about 96% of the time (3937 in my last run); the theoretical value for 3 iterations is 96.1%.

## QFT (`qft.py`)

Textbook construction: H plus controlled phase rotations π/2^(k−j), then swaps to reverse the qubit order. I apply it to |5⟩ = |0101⟩. Every basis state ends up with the same amplitude and a phase that grows linearly, 2π·5·y/16, which is what the Q-sphere colours show.

## VQE for H2 (`vqe_h2.py`)

Hamiltonian of H2 at 0.735 Å (STO-3G, parity mapping with two-qubit reduction), five Pauli terms with precomputed coefficients. Ansatz: Ry on each qubit, CNOT, Ry again, 4 parameters. COBYLA minimises the exact statevector expectation value, so there is no shot noise.

Result: −1.857275 Ha after 64 evaluations. Diagonalising the 4×4 Hamiltonian gives −1.857275 Ha, so the ansatz reaches the true ground state. This is the electronic energy only; adding nuclear repulsion would give the total energy.

## Things I would do next

- Run Grover and Deutsch–Jozsa on real IBM hardware and compare with the simulator.
- VQE with shot-based estimation, to see how many shots are needed for chemical accuracy (1.6 mHa).
- Scan the H–H distance and plot the dissociation curve.
