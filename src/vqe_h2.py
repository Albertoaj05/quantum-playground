"""
VQE (Variational Quantum Eigensolver) - molécula H2.

Hamiltoniano H2 a distancia interatómica 0.735 Å, base STO-3G,
mapeo Jordan-Wigner, paridad/tapering reducido a 2 qubits.

Coeficientes precalculados (referencia Qiskit Nature):

H = c0 * I⊗I + c1 * I⊗Z + c2 * Z⊗I + c3 * Z⊗Z + c4 * X⊗X

c0 = -1.0523732
c1 =  0.39793742
c2 = -0.39793742
c3 = -0.01128010
c4 =  0.18093119

Energía exacta ≈ -1.85728 Ha (electronic part).
"""
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp, Statevector
from utils import save_circuit, IMG_DIR


COEFFS = {
    "II": -1.0523732,
    "IZ":  0.39793742,
    "ZI": -0.39793742,
    "ZZ": -0.01128010,
    "XX":  0.18093119,
}


def h2_hamiltonian() -> SparsePauliOp:
    return SparsePauliOp.from_list([(p, c) for p, c in COEFFS.items()])


def ansatz(params) -> QuantumCircuit:
    """Ansatz hardware-efficient con 2 qubits y 4 parámetros."""
    theta = params
    qc = QuantumCircuit(2)
    qc.ry(theta[0], 0)
    qc.ry(theta[1], 1)
    qc.cx(0, 1)
    qc.ry(theta[2], 0)
    qc.ry(theta[3], 1)
    return qc


def expectation(params, H):
    qc = ansatz(params)
    sv = Statevector.from_instruction(qc)
    return float(np.real(sv.expectation_value(H)))


def run():
    print("\n=== VQE H2 ===")
    H = h2_hamiltonian()
    history = []

    def cost(p):
        e = expectation(p, H)
        history.append(e)
        return e

    np.random.seed(7)
    x0 = np.random.uniform(0, 2 * np.pi, size=4)
    res = minimize(cost, x0, method="COBYLA", options={"maxiter": 200, "rhobeg": 0.3})

    print(f"  E_min  (VQE)  = {res.fun:.6f} Ha")
    print(f"  iters         = {len(history)}")

    # circuito final del ansatz óptimo
    save_circuit(ansatz(res.x), "vqe_h2_ansatz")

    # curva de convergencia
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(history, lw=2)
    ax.axhline(-1.85728, color="red", ls="--", label="referencia exacta")
    ax.set_xlabel("iteración")
    ax.set_ylabel("E (Hartree)")
    ax.set_title("VQE H2 - convergencia")
    ax.grid(alpha=0.3)
    ax.legend()
    path = IMG_DIR / "vqe_h2_convergence.png"
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [img] {path.name}")


if __name__ == "__main__":
    run()
