"""
Utilidades comunes: guardar circuitos, histogramas, estados.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from qiskit.visualization import (
    plot_histogram,
    plot_bloch_multivector,
    plot_state_city,
    plot_state_qsphere,
)

IMG_DIR = Path(__file__).resolve().parent.parent / "images"
IMG_DIR.mkdir(exist_ok=True)


def save_circuit(qc, name: str):
    """Dibuja circuito y lo guarda como PNG."""
    fig = qc.draw(output="mpl", style="iqp", fold=-1)
    path = IMG_DIR / f"{name}_circuit.png"
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [img] {path.name}")
    return path


def save_histogram(counts, name: str, title: str = ""):
    fig = plot_histogram(counts, title=title or name, figsize=(8, 5))
    path = IMG_DIR / f"{name}_hist.png"
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [img] {path.name}")
    return path


def save_bloch(state, name: str):
    fig = plot_bloch_multivector(state)
    path = IMG_DIR / f"{name}_bloch.png"
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [img] {path.name}")
    return path


def save_state_city(state, name: str):
    fig = plot_state_city(state, title=name)
    path = IMG_DIR / f"{name}_city.png"
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [img] {path.name}")
    return path


def save_qsphere(state, name: str):
    fig = plot_state_qsphere(state)
    path = IMG_DIR / f"{name}_qsphere.png"
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [img] {path.name}")
    return path
