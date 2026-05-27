# 🧪 Quantum Playground

Proyecto educativo de **computación cuántica** con Qiskit. Implementa los algoritmos clásicos del campo, todos con **visualizaciones generadas automáticamente**: circuitos, histogramas, esfera de Bloch, q-sphere y mapas de estado.

> Todo el código está comentado en español y diseñado para que entiendas qué pasa en cada línea.

---

## 📋 Índice

- [¿Qué incluye?](#-qué-incluye)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Instalación](#-instalación)
- [Cómo ejecutarlo](#-cómo-ejecutarlo)
- [Resultados esperados](#-resultados-esperados)
- [Subir a GitHub](#-subir-a-github)
- [Recursos](#-recursos)

---

## ✨ ¿Qué incluye?

| # | Demo | Qué demuestra |
|---|------|---------------|
| 1 | **Bloch gallery** | Cómo H, X, Y, Z, S, T, Rx, Ry mueven un qubit en la esfera. |
| 2 | **Estados de Bell** | Los 4 estados de máximo entrelazamiento de 2 qubits (Φ±, Ψ±). |
| 3 | **GHZ** | Entrelazamiento multipartito de N qubits. |
| 4 | **Teleportación** | Transmisión de un qubit usando entrelazamiento + 2 bits clásicos. |
| 5 | **Grover** | Búsqueda cuántica con ventaja √N respecto al clásico. |
| 6 | **Deutsch–Jozsa** | Distinguir función constante vs balanceada en 1 sola query. |
| 7 | **QFT** | Transformada cuántica de Fourier (base de Shor y QPE). |
| 8 | **VQE H₂** | Calcular la energía del estado fundamental de la molécula de hidrógeno. |

Cada demo genera múltiples PNGs en `images/`:

- `*_circuit.png` — el circuito dibujado.
- `*_hist.png` — histograma de medidas (4096 shots por defecto).
- `*_qsphere.png` — visualización Qsphere del estado.
- `*_city.png` — matriz de densidad como mapa de barras 3D.
- `*_bloch.png` — esfera de Bloch (solo 1 qubit).

---

## 📁 Estructura del proyecto

```
quantum-playground/
├── src/                          ← código fuente
│   ├── utils.py                  ← helpers de visualización
│   ├── bloch_gallery.py          ← galería de puertas en esfera de Bloch
│   ├── bell_states.py            ← 4 estados de Bell
│   ├── ghz_state.py              ← estado GHZ
│   ├── teleportation.py          ← teleportación cuántica
│   ├── grover.py                 ← algoritmo de Grover
│   ├── deutsch_jozsa.py          ← Deutsch–Jozsa
│   ├── qft.py                    ← Quantum Fourier Transform
│   ├── vqe_h2.py                 ← VQE para H₂
│   └── main.py                   ← ejecuta TODO de una vez
├── notebooks/
│   └── quantum_playground.ipynb  ← versión Jupyter interactiva
├── images/                       ← PNGs generados (se llena al ejecutar)
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🛠 Instalación

### Requisitos previos

- **Python 3.10+** (probado en 3.11).
- `pip` actualizado.
- (Opcional) `git` para clonar y subir a GitHub.

### Paso a paso

```bash
# 1. Clona o descarga el proyecto
git clone https://github.com/TU_USUARIO/quantum-playground.git
cd quantum-playground

# 2. Crea un entorno virtual (recomendado)
python3 -m venv .venv
source .venv/bin/activate           # Linux / Mac
# .venv\Scripts\activate            # Windows PowerShell

# 3. Instala dependencias
pip install -r requirements.txt
```

> En Linux puede que necesites `sudo apt install python3-tk` si matplotlib se queja del backend.

---

## ▶️ Cómo ejecutarlo

### Opción A — ejecutar TODO de golpe

Genera los 40+ PNGs en `images/`:

```bash
cd src
python main.py
```

Verás por consola los resultados de cada algoritmo (counts, energía, iteraciones…).

### Opción B — ejecutar un demo concreto

```bash
cd src
python grover.py
python vqe_h2.py
# etc.
```

### Opción C — modo interactivo (Jupyter)

```bash
jupyter notebook notebooks/quantum_playground.ipynb
```

Cambia parámetros (`n`, `marked`, etc.) y reejecuta celdas.

---

## 📊 Resultados esperados

Cuando ejecutes `python main.py` deberías ver algo como:

```
=== GROVER ===
  n=4, N=16, marcado=1010, iters=3
  top: 1010 (3942/4096 = 96.2%)

=== DEUTSCH-JOZSA ===
  constante  -> {'0000': 2048}
  balanceado -> {'1010': 2048}

=== VQE H2 ===
  E_min  (VQE) = -1.857275 Ha
  iters         = 64
```

| Demo | Resultado clave |
|------|-----------------|
| Bell Φ⁺ | Solo `00` y `11` (~50/50). |
| GHZ (5q) | Solo `00000` y `11111`. |
| Grover | Estado marcado con >95% probabilidad. |
| Deutsch–Jozsa constante | Todos `0`. |
| Deutsch–Jozsa balanceada | Cualquier cosa menos todos `0`. |
| VQE H₂ | Energía ≈ **-1.85728 Ha** (referencia química exacta). |

---

## 🚀 Subir a GitHub

### Si aún no tienes repo

```bash
# desde la carpeta quantum-playground/
git init
git add .
git commit -m "feat: quantum playground inicial con Qiskit"
git branch -M main

# crea el repo VACÍO en github.com (sin README, sin .gitignore, sin license)
# luego:
git remote add origin https://github.com/TU_USUARIO/quantum-playground.git
git push -u origin main
```

### Si quieres usar GitHub CLI (más rápido)

```bash
gh auth login                                        # solo la primera vez
gh repo create quantum-playground --public --source=. --remote=origin --push
```

### Si ya tienes repo y solo añades cambios

```bash
git add .
git commit -m "feat: añade VQE para H2 y notebook"
git push
```

### Comprobaciones recomendadas antes de subir

```bash
# que no se te cuelen __pycache__ ni venv
git status

# ver tamaño total
du -sh .

# las imágenes pueden engordar bastante: si no las quieres en el repo,
# añade `images/` al .gitignore y bórralas del tracking:
# git rm -r --cached images/
```

---

## 🧠 Recursos para profundizar

- 📘 [Qiskit Textbook](https://learning.quantum.ibm.com/) — tutorial oficial.
- 📗 *Quantum Computation and Quantum Information* — Nielsen & Chuang (la biblia).
- 🎥 [Qiskit YouTube](https://www.youtube.com/qiskit).
- 🌐 [IBM Quantum Platform](https://quantum.ibm.com/) — ejecuta en hardware real (gratis con cuenta).

---

## 📜 Licencia

MIT — haz lo que quieras con esto.
