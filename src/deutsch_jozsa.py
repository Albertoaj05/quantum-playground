"""
Deutsch-Jozsa.

Decide si f: {0,1}^n -> {0,1} es:
- constante: misma salida para todo input
- balanceada: 0 en mitad, 1 en otra mitad

Clásico: hasta 2^(n-1)+1 evaluaciones para garantizar.
Cuántico: 1 sola evaluación.

Si tras correr y medir los n qubits de entrada salen todos 0 -> constante.
Cualquier otra cosa -> balanceada.
"""
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from utils import save_circuit, save_histogram


def constant_oracle(n: int, value: int = 0) -> QuantumCircuit:
    qc = QuantumCircuit(n + 1, name="f_const")
    if value == 1:
        qc.x(n)
    return qc


def balanced_oracle(n: int, pattern: str | None = None) -> QuantumCircuit:
    """Oráculo balanceado: f(x) = XOR de bits seleccionados por el pattern."""
    qc = QuantumCircuit(n + 1, name="f_bal")
    if pattern is None:
        pattern = "1" * n
    for i, b in enumerate(reversed(pattern)):
        if b == "1":
            qc.cx(i, n)
    return qc


def dj_circuit(n: int, oracle: QuantumCircuit) -> QuantumCircuit:
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)
    qc.h(range(n + 1))
    qc.barrier()
    qc.compose(oracle, inplace=True)
    qc.barrier()
    qc.h(range(n))
    qc.measure(range(n), range(n))
    return qc


def run():
    print("\n=== DEUTSCH-JOZSA ===")
    n = 4
    sim = AerSimulator()

    qc_c = dj_circuit(n, constant_oracle(n, value=1))
    save_circuit(qc_c, "dj_constant")
    counts_c = sim.run(transpile(qc_c, sim), shots=2048).result().get_counts()
    save_histogram(counts_c, "dj_constant", title="DJ - oráculo constante")
    print(f"  constante -> {counts_c} (esperado: '0'*n)")

    qc_b = dj_circuit(n, balanced_oracle(n, "1010"))
    save_circuit(qc_b, "dj_balanced")
    counts_b = sim.run(transpile(qc_b, sim), shots=2048).result().get_counts()
    save_histogram(counts_b, "dj_balanced", title="DJ - oráculo balanceado")
    print(f"  balanceado -> {counts_b} (esperado: distinto de '0'*n)")


if __name__ == "__main__":
    run()
