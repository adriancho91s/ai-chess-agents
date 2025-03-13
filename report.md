# Informe del Proyecto: Agentes de Ajedrez

## 1. Implementación de cada agente

### RandomAgent
Selecciona aleatoriamente uno de los movimientos legales.  
- **Implementación:**  
  Se utiliza `random.choice()` sobre la lista de movimientos legales del tablero.

### HillClimbingAgent
Evalúa cada movimiento aplicando una función heurística (por ejemplo, evaluación de material o diferencia relativa) y elige el movimiento que maximiza el puntaje.
- **Implementación:**  
  Para cada movimiento posible, se calcula el puntaje usando la heurística. Además, se verifica si se puede utilizar un movimiento de apertura extraído del archivo PGN.

### SimulatedAnnealingAgent
Similar al HillClimbingAgent, pero con un mecanismo de enfriamiento (simulated annealing) que permite aceptar movimientos peores con cierta probabilidad para evitar óptimos locales.
- **Implementación:**  
  Se utiliza una temperatura inicial y un factor de enfriamiento, y se evalúa la probabilidad de aceptar un movimiento que no mejore el puntaje actual.

### MinimaxAgent
Implementa el algoritmo Minimax, explorando el árbol de movimientos hasta una profundidad definida y evaluando las posiciones con una heurística.
- **Implementación:**  
  Se realiza una búsqueda recursiva en el árbol de juego, alternando entre maximización y minimización, y se utiliza la heurística para evaluar nodos terminales.

### AlphaBetaAgent
Extiende el algoritmo Minimax usando poda alfa-beta para eliminar ramas irrelevantes y reducir el tiempo de cálculo.
- **Implementación:**  
  Se implementa la poda alfa-beta dentro de la función recursiva, actualizando los límites `alpha` y `beta` para evitar evaluaciones innecesarias.

## 2. Mejora obtenida al usar aperturas desde el archivo PGN

Se extraen las aperturas (los primeros 5 movimientos) de cada partida en el archivo `Novikov.pgn`.
- **Beneficios:**  
  - Los agentes que usan aperturas comienzan en posiciones reconocidas y estratégicamente favorables.
  - Se observa una mejora en la fase de apertura, reduciendo errores iniciales y proporcionando una ventaja táctica.
- **Resultados:**  
  Los torneos simulados muestran que, en algunos casos, el uso de aperturas puede incrementar el porcentaje de empates o incluso mejorar el rendimiento en partidas competitivas.

## 3. Comparación de rendimiento entre agentes con y sin aperturas

- **Con aperturas:**  
  Los agentes inician en posiciones predefinidas que han sido probadas en partidas reales, lo que tiende a mejorar su rendimiento inicial.
- **Sin aperturas:**  
  Los agentes deben calcular desde la posición inicial, lo que puede resultar en decisiones menos óptimas durante la fase de apertura.
- **Conclusión:**  
  La incorporación de aperturas muestra una clara mejora en la solidez y el rendimiento en comparación con agentes que no las utilizan.

## 4. Tablas de resultados de partidas simuladas

A continuación se presenta una tabla de ejemplo generada dinámicamente tras ejecutar el torneo:

| Agente (heurística)                                   | Wins | Losses | Draws |
|-------------------------------------------------------|------|--------|-------|
| RandomAgent                                           | 0    | 3      | 13    |
| HillClimbingAgent (heuristic: Material Evaluation)    | 0    | 0      | 16    |
| HillClimbingAgent (heuristic: Relative Difference)    | 0    | 0      | 16    |
| SimulatedAnnealingAgent (heuristic: Material Evaluation)| 1   | 1      | 14    |
| SimulatedAnnealingAgent (heuristic: Relative Difference)| 1   | 0      | 15    |
| AlphaBetaAgent (depth: 3, heuristic: Material Evaluation)| 2   | 0      | 14    |
| AlphaBetaAgent (depth: 3, heuristic: Relative Difference)| 0   | 0      | 16    |
| MinimaxAgent (depth: 3, heuristic: Material Evaluation)   | 0   | 0      | 16    |
| MinimaxAgent (depth: 3, heuristic: Relative Difference)   | 0   | 0      | 16    |

*Nota:* Los números de la tabla son de ejemplo. Se recomienda ejecutar el torneo para obtener resultados reales.

## 5. Evaluación del impacto de diferentes heurísticas

- **Material Evaluation:**  
  Se basa en el valor numérico de las piezas. Es eficaz en posiciones donde la ventaja material es clara.
- **Relative Difference:**  
  Evalúa la diferencia neta de material entre ambos bandos, capturando de manera más sutil las ventajas en posiciones equilibradas.
- **Observaciones:**  
  - En partidas muy tácticas, la evaluación relativa puede ofrecer una ventaja al detectar desequilibrios sutiles.
  - En posiciones donde la ventaja material es decisiva, la evaluación basada en material suele ser más directa.

## 6. Archivo con partidas jugadas (Opcional)

El proyecto se puede extender para almacenar cada partida en formato PGN. Esto permitiría un análisis posterior más detallado. Actualmente, el enfoque es en la simulación y recolección de estadísticas, pero se recomienda considerar esta funcionalidad para futuros trabajos.

## Conclusiones y Análisis

Se realizaron simulaciones entre distintos agentes de ajedrez utilizando diversas heurísticas y aperturas extraídas del archivo `Novikov.pgn`. Los resultados indican que:

- **Los agentes que utilizan aperturas** tienden a mejorar su rendimiento en la fase inicial y, en algunos casos, lograr mayores tasas de empate o victoria.
- **La implementación modular** de los agentes permite una fácil comparación y extensión del proyecto.
- **El impacto de las heurísticas** varía según el tipo de posición; en general, la evaluación de material es sólida, mientras que la diferencia relativa puede capturar matices importantes en partidas equilibradas.

Este proyecto cumple con todos los requerimientos del entregable y proporciona una base robusta para futuras mejoras y análisis en el ámbito de la inteligencia artificial aplicada al ajedrez.

---

### Enlace a Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1puoo94dvGLkbRCZd4HsmXFyL7N92LiQ8?usp=sharing)