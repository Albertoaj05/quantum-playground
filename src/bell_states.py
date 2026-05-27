"""
Estados de Bell - 4 estados maximamente entrelazados de 2 qubits.

|Φ+> = (|00> + |11>) / sqrt(2)
|Φ-> = (|00> - |11>) / sqrt(2)
|Ψ+> = (|01> + |10>) / sqrt(2)
|Ψ-> = (|01> - |10>) / sqrt(2)
"""
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from utils import save_circuit, save_histogram, save_state_city, save_qsphere


def bell_phi_plus():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    return qc


def bell_phi_minus():
    qc = QuantumCircuit(2, 2)
    qc.x(0)
    qc.h(0)
    qc.cx(0, 1)
    return qc


def bell_psi_plus():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.x(1)
    qc.cx(0, 1)
    return qc


def bell_psi_minus():
    qc = QuantumCircuit(2, 2)
    qc.x(0)
    qc.x(1)
    qc.h(0)
    qc.cx(0, 1)
    return qc


def run():
    print("\n=== BELL STATES ===")
    sim = AerSimulator()
    states = {
        "bell_phi_plus":  bell_phi_plus(),
        "bell_phi_minus": bell_phi_minus(),
        "bell_psi_plus":  bell_psi_plus(),
        "bell_psi_minus": bell_psi_minus(),
    }
    for name, qc in states.items():
        print(f"\n-> {name}")
        # estado puro (sin medir)
        sv = Statevector.from_instruction(qc)
        save_state_city(sv, name)
        save_qsphere(sv, name)
        # circuito + medidas
        qc_m = qc.copy()
        qc_m.measure([0, 1], [0, 1])
        save_circuit(qc_m, name)
        # simulación
        tqc = transpile(qc_m, sim)
        result = sim.run(tqc, shots=4096).result()
        counts = result.get_counts()
        save_histogram(counts, name, title=name)
        print(f"  counts: {counts}")


if __name__ == "__main__":
    run()
