"""
Estado GHZ (Greenberger-Horne-Zeilinger).

|GHZ> = (|000...0> + |111...1>) / sqrt(2)

Generalización Bell a N qubits. Entrelazamiento multipartito.
"""
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from utils import save_circuit, save_histogram, save_qsphere


def ghz(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n, n)
    qc.h(0)
    for i in range(n - 1):
        qc.cx(i, i + 1)
    return qc


def run():
    print("\n=== GHZ ===")
    n = 5
    qc = ghz(n)
    sv = Statevector.from_instruction(qc)
    save_qsphere(sv, f"ghz_{n}q")

    qc_m = qc.copy()
    qc_m.measure(range(n), range(n))
    save_circuit(qc_m, f"ghz_{n}q")

    sim = AerSimulator()
    counts = sim.run(transpile(qc_m, sim), shots=4096).result().get_counts()
    save_histogram(counts, f"ghz_{n}q", title=f"GHZ {n} qubits")
    print(f"  counts: {counts}")


if __name__ == "__main__":
    run()
