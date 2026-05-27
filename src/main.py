"""
Ejecutor maestro - corre todos los experimentos.
Uso:  python src/main.py
"""
import bell_states
import ghz_state
import teleportation
import grover
import deutsch_jozsa
import qft
import vqe_h2
import bloch_gallery


def main():
    print("=" * 60)
    print("QUANTUM PLAYGROUND - ejecutando todos los demos")
    print("=" * 60)

    bloch_gallery.run()
    bell_states.run()
    ghz_state.run()
    teleportation.run()
    grover.run()
    deutsch_jozsa.run()
    qft.run()
    vqe_h2.run()

    print("\n" + "=" * 60)
    print("LISTO. Revisa carpeta images/ con todos los PNGs.")
    print("=" * 60)


if __name__ == "__main__":
    main()
