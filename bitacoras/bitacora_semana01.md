# Bitácora — Semana 1 (Python científico + Álgebra lineal)
**Rango:** Lunes 8 → Sábado 13 de septiembre de 2025  
**Meta semanal:** dominar `numpy`/`scipy`/`matplotlib` para álgebra lineal aplicada y sentar las bases para discretizaciones matriciales en QM.  
**Mini‑proyecto:** diagonalización y análisis de matrices 3×3 (casos con y sin degeneración) con validaciones numéricas.  

---

## Definición de Hecho (DoD) — Semana 1
- `00-numerics.ipynb` ejecuta sin errores y muestra:
  - Comparación `np.linalg.eig` vs `np.linalg.eigh` en sistemas simétricos.
  - Estudio de convergencia/condición: norma de residuo `||Ax - λx||` < 1e-8.
  - Gráfico (matplotlib) legible con ejes/leyenda/unidades donde aplique.
- Reporte corto `docs/sem1_numerics.md` (≤ 1 pág.) con: objetivo, método, resultados, limitaciones y próximos pasos.
- Carpeta `tests/` con un test mínimo (`test_eigs.py`) que verifica el residuo y casos con degeneración.

**Entregables:** 1 notebook + 1 reporte + 1 test mínimo.

---

## Estructura sugerida de carpetas
```
qm/
statmech/
md/
docs/
figs/
tests/
data/
```

---

## Plantilla de entrada diaria (copia/pega)
**Fecha:** <YYYY‑MM‑DD> — **Día:** <L/Miércoles/...>  
**Objetivo del día (1 frase):**  
**Bloques:**
- Plan (5 min): <qué haré + criterio de éxito>
- Construir (50–60 min): <micro‑tareas en secuencia>
- Verificar (20 min): <prueba mínima y umbral>
- Cerrar (5 min): [RECAP] 3–5 viñetas

**Artefactos producidos:** <archivos/figuras/commits>  
**Tiempo real invertido:** <min>  
**Bloqueos:** <sí/no + cómo los resolví>  
**Estado:** ☐ Hecho ☐ En progreso ☐ Bloqueado

---

## Lunes 8/sep — Arranque técnico
**Objetivo:** crear `00-numerics.ipynb` y validar operaciones básicas de álgebra lineal.  
**Plan (5 min):** definir DoD y datos de prueba; activar entorno.  
**Construir (50–60 min):**
1) Inicializar entorno (venv/conda) y abrir notebook.
2) Crear matrices A (simétrica) y B (no simétrica) 3×3 bien condicionadas y mal condicionadas.
3) Calcular autovalores/autovectores con `eig`/`eigh`.  
4) Implementar función `residuo(A, λ, x)` y verificar `||Ax − λx||`.
5) Graficar error vs. número de dígitos/escala (simple).
**Verificar (20 min):** residuo < 1e-8 en casos bien condicionados; documentar cuando no se cumple.  
**Cerrar (5 min) — [RECAP]:** notas de hallazgos y TODO.  
**Artefactos:** `00-numerics.ipynb`, figura `figs/eig_error_lunes.png`, commit `feat(numerics): eig/eigh baseline`.  
**Riesgos:** mal condicionamiento → **Mitigación:** escalar y usar `eigh` para simétricas.

---

## Martes 9/sep — Estabilidad y condicionamiento
**Objetivo:** cuantificar el número de condición y su efecto en `eig`.  
**Plan (5 min):** fijar umbrales de residuo y reproducibilidad (semilla).  
**Construir (50–60 min):**
1) Función `cond2(A)` y generación de familias A(α) con cond(A) controlado.
2) Tabla/plot: cond(A) vs residuo medio/max.
3) Caso degenerado: A con autovalores repetidos; observar rotación de subespacio propio.
**Verificar (20 min):** gráfico `figs/cond_residuo.png` y conclusiones breves.
**Artefactos:** actualización del notebook; `docs/sem1_numerics.md` (borrador).  
**Riesgos:** falsa confianza por ε‑máquina → **Mitigación:** reportar tolerancias y tipo de dato (float64).

---

## Miércoles 10/sep — Operadores y simetrías (puente a QM)
**Objetivo:** preparar terreno para discretizar operadores hermíticos.  
**Plan (5 min):** definir por qué `eigh` es el camino para operadores hermíticos.  
**Construir (50–60 min):**
1) Revisar propiedades de matrices simétricas/hermíticas.
2) Ensayo numérico: A=Aᵀ+εN con N aleatoria; ver impacto en autovalores.
3) Escribir sección “Método” en `docs/sem1_numerics.md` (½ pág.).
**Verificar (20 min):** residuo y ortonormalidad de autovectores (`XᵀX≈I`).  
**Artefactos:** gráfico `figs/ortho_check.png`, commit `docs: método y validez`.  
**Riesgos:** ortogonales mal normalizados → **Mitigación:** re‑normalizar y reportar error.

---

## Jueves 11/sep — Casos de prueba y `tests/`
**Objetivo:** establecer un test mínimo repetible.  
**Plan (5 min):** definir PASS/FAIL claro.  
**Construir (50–60 min):**
1) Crear `tests/test_eigs.py` con dos casos (bien/degenerado).
2) Añadir función generadora de matrices de prueba con semilla fija.
3) Integrar verificación de residuo y ortonormalidad.
**Verificar (20 min):** ejecutar tests; guardar salida.  
**Artefactos:** `tests/test_eigs.py`, captura `figs/tests_output.txt`.  
**Riesgos:** flaky tests por aleatoriedad → **Mitigación:** fijar `np.random.seed(…)` y tolerancias.

---

## Viernes 12/sep — Visualización clara
**Objetivo:** producir una figura “ACS‑ready”.  
**Plan (5 min):** decidir 1 figura final clara (sin estilos ni colores forzados).  
**Construir (50–60 min):**
1) Limpieza de gráficos: títulos, ejes, unidades, fuente legible.
2) Figura final: `cond(A)` vs `||Ax−λx||` con barras de error.
3) Pie de figura auto‑contenido (qué, cómo, parámetros).  
**Verificar (20 min):** checklist ACS; guardar `figs/cond_vs_residuo.png`.  
**Artefactos:** figura final, commit `figs: cond vs residuo (ACS‑ready)`.  
**Riesgos:** saturación visual → **Mitigación:** una métrica por gráfico.

---

## Sábado 13/sep — Empaque y reporte
**Objetivo:** cierre semanal con reporte y checklist.  
**Plan (5 min):** revisar DoD de la semana.  
**Construir (50–60 min):**
1) Redactar `docs/sem1_numerics.md` (≤1 pág; objetivo→método→resultados→limitaciones→próximos pasos).
2) Pasar tests; etiquetar commits finales.
3) Actualizar README con cómo reproducir (entorno, comandos).  
**Verificar (20 min):** DoD completo (notebook, reporte, test, figura).  
**Cierre (5 min) — [RECAP]:** 5 viñetas + plan de arranque para Semana 2.

---

## Tabla de progreso (llenar al cierre de cada día)
| Día | Artefactos clave | Estado | Residuo max | cond(A) máx. probado | Comentarios |
|-----|-------------------|--------|-------------|-----------------------|-------------|
| Lunes | 00-numerics.ipynb, eig/eigh | ☐/☑ |  |  |  |
| Martes | cond2 y estudio | ☐/☑ |  |  |  |
| Miérc. | ortonormalidad, método | ☐/☑ |  |  |  |
| Jueves | tests mínimos | ☐/☑ |  |  |  |
| Viernes | figura ACS | ☐/☑ |  |  |  |
| Sábado | reporte y README | ☐/☑ |  |  |  |

---

## Matriz rápida de riesgos
- **R1:** Inestabilidad numérica en matrices mal condicionadas → reportar cond(A) y usar `eigh` en simétricas.
- **R2:** Tiempo se va en gráficos → 1 figura final + pie ACS, el resto como anexos si hace falta.
- **R3:** Tests frágiles → fijar semilla y tolerancias explícitas.

---

## Checklist de entrega (Sábado)
- [ ] `00-numerics.ipynb` ejecuta de principio a fin.
- [ ] `docs/sem1_numerics.md` (≤1 pág) con secciones y conclusiones.
- [ ] `tests/test_eigs.py` pasa en limpio.
- [ ] `figs/cond_vs_residuo.png` con pie ACS.
- [ ] README actualizado (reproducibilidad).
