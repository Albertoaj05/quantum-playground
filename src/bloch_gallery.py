"""
Galería esfera de Bloch.

Muestra cómo distintas puertas mueven |0> por la esfera.
"""
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from utils import save_bloch


def run():
    print("\n=== BLOCH GALLERY ===")
    cases = {
        "bloch_0":      lambda qc: None,
        "bloch_H":      lambda qc: qc.h(0),
        "bloch_X":      lambda qc: qc.x(0),
        "bloch_Y":      lambda qc: qc.y(0),
        "bloch_Z_on_H": lambda qc: (qc.h(0), qc.z(0)),
        "bloch_S_on_H": lambda qc: (qc.h(0), qc.s(0)),
        "bloch_T_on_H": lambda qc: (qc.h(0), qc.t(0)),
        "bloch_RX_pi3": lambda qc: qc.rx(np.pi / 3, 0),
        "bloch_RY_pi4": lambda qc: qc.ry(np.pi / 4, 0),
    }
    for name, op in cases.items():
        qc = QuantumCircuit(1)
        op(qc)
        sv = Statevector.from_instruction(qc)
        save_bloch(sv, name)


if __name__ == "__main__":
    run()
