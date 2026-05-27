"""
Algoritmo de Grover.

Búsqueda en base de datos no estructurada:
- Clásico: O(N) consultas.
- Grover: O(sqrt(N)) consultas.

Implementación: 4 qubits, N=16, marcamos estado |1010>.
Iteraciones óptimas ≈ (pi/4) * sqrt(N/M).
"""
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from utils import save_circuit, save_histogram


def oracle(n: int, marked: str) -> QuantumCircuit:
    """Oráculo que invierte fase del estado marcado."""
    qc = QuantumCircuit(n, name="oracle")
    # poner 0 donde el marcado tiene 0 (para que MCZ vea |11...1>)
    for i, b in enumerate(reversed(marked)):
        if b == "0":
            qc.x(i)
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)
    for i, b in enumerate(reversed(marked)):
        if b == "0":
            qc.x(i)
    return qc


def diffuser(n: int) -> QuantumCircuit:
    """Operador difusión (inversión sobre la media)."""
    qc = QuantumCircuit(n, name="diffuser")
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)
    qc.x(range(n))
    qc.h(range(n))
    return qc


def grover(n: int, marked: str) -> QuantumCircuit:
    N = 2 ** n
    iters = int(np.floor((np.pi / 4) * np.sqrt(N)))
    qc = QuantumCircuit(n, n)
    qc.h(range(n))  # superposición uniforme
    for _ in range(iters):
        qc.compose(oracle(n, marked), inplace=True)
        qc.compose(diffuser(n), inplace=True)
    qc.measure(range(n), range(n))
    return qc, iters


def run():
    print("\n=== GROVER ===")
    n = 4
    marked = "1010"
    qc, iters = grover(n, marked)
    print(f"  n={n}, N={2**n}, marcado={marked}, iters={iters}")
    save_circuit(qc, "grover")

    sim = AerSimulator()
    counts = sim.run(transpile(qc, sim), shots=4096).result().get_counts()
    save_histogram(counts, "grover", title=f"Grover busca |{marked}>")
    top = max(counts, key=counts.get)
    print(f"  top: {top} ({counts[top]}/4096 = {100*counts[top]/4096:.1f}%)")


if __name__ == "__main__":
    run()
