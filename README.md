# Chem121 — Computación en química (starter)

Este repositorio contiene la estructura base para tu plan de 10 semanas. Semana 1 se centra en `numpy`/`scipy`/`matplotlib` y álgebra lineal aplicada.

## Estructura
```
src/qm/            # utilidades numéricas y módulos de QM
tests/             # tests con pytest
docs/              # reportes cortos (ACS-style)
figs/              # figuras generadas
notebooks/         # cuadernos de trabajo
bitacoras/         # bitácoras semanales
.github/workflows/ # CI con pytest
```

## Requisitos
- Python 3.10+
- `pip install -r requirements.txt`

## Uso rápido
1. Clona o extrae este repositorio.
2. Crea y activa entorno:
   - `python -m venv .venv && source .venv/bin/activate` (Linux/Mac)
   - `python -m venv .venv && .venv\Scripts\activate` (Windows)
3. Instala dependencias: `pip install -r requirements.txt`
4. Ejecuta tests: `pytest -q`
5. Abre `notebooks/00-numerics.ipynb` y sigue la bitácora de `bitacoras/bitacora_semana01.md`.

## Convenciones
- Commits: `feat|fix|refactor|docs|test(scope): mensaje`
- Una figura por gráfico, ejes/unidades siempre.
- Tests con tolerancias explícitas y semilla fija cuando aplique.

## Licencia
MIT
