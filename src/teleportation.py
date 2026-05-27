"""
Teleportación cuántica.

Alice transmite estado |psi> a Bob usando:
- 1 par Bell compartido
- 2 bits clasicos

Protocolo:
1) Crear par Bell entre qubit 1 (Alice) y 2 (Bob).
2) Alice aplica CNOT(0,1) y H(0).
3) Alice mide q0, q1 -> bits clásicos.
4) Bob aplica X^c1 Z^c0 condicionado a bits.
5) q2 acaba en |psi>.
"""
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, random_statevector
from utils import save_circuit, save_histogram, save_bloch


def teleportation_circuit(psi_init: QuantumCircuit | None = None) -> QuantumCircuit:
    qr = QuantumRegister(3, name="q")
    cr_a = ClassicalRegister(1, name="ca")
    cr_b = ClassicalRegister(1, name="cb")
    cr_out = ClassicalRegister(1, name="cout")
    qc = QuantumCircuit(qr, cr_a, cr_b, cr_out)

    # Estado a teleportar en q0
    if psi_init is not None:
        qc.compose(psi_init, qubits=[0], inplace=True)
    else:
        # estado por defecto: superposición arbitraria
        qc.ry(np.pi / 3, 0)
        qc.rz(np.pi / 5, 0)

    qc.barrier()

    # Par Bell entre q1 (Alice) y q2 (Bob)
    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()

    # Operaciones Alice
    qc.cx(0, 1)
    qc.h(0)
    qc.barrier()

    # Medidas de Alice
    qc.measure(0, cr_a[0])
    qc.measure(1, cr_b[0])
    qc.barrier()

    # Correcciones de Bob (clásicamente controladas)
    with qc.if_test((cr_b, 1)):
        qc.x(2)
    with qc.if_test((cr_a, 1)):
        qc.z(2)

    # Medida final para verificar
    qc.measure(2, cr_out[0])
    return qc


def run():
    print("\n=== TELEPORTACIÓN ===")
    qc = teleportation_circuit()
    save_circuit(qc, "teleportation")

    sim = AerSimulator()
    counts = sim.run(transpile(qc, sim), shots=4096).result().get_counts()
    save_histogram(counts, "teleportation", title="Teleportación (3 reg. clásicos)")
    print(f"  counts: {counts}")


if __name__ == "__main__":
    run()
