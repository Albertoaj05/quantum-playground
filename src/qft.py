"""
Quantum Fourier Transform (QFT).

Base de Shor, estimación de fase. Análogo cuántico de la DFT.
QFT |x> = (1/sqrt(N)) * sum_y exp(2*pi*i*x*y/N) |y>
"""
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from utils import save_circuit, save_qsphere, save_state_city


def qft(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n, name="QFT")
    for j in range(n):
        qc.h(j)
        for k in range(j + 1, n):
            qc.cp(np.pi / 2 ** (k - j), k, j)
    # swap final para invertir orden
    for i in range(n // 2):
        qc.swap(i, n - 1 - i)
    return qc


def run():
    print("\n=== QFT ===")
    n = 4
    # preparar |x=5> = |0101>
    prep = QuantumCircuit(n)
    prep.x(0)
    prep.x(2)

    full = prep.compose(qft(n))
    save_circuit(full, "qft")

    sv = Statevector.from_instruction(full)
    save_qsphere(sv, "qft_out")
    save_state_city(sv, "qft_out")
    print(f"  QFT|5> calculado y guardado.")


if __name__ == "__main__":
    run()
