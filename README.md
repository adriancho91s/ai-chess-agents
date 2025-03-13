# ChessAgentsProject

Este repositorio implementa varios agentes de ajedrez que utilizan diferentes algoritmos de búsqueda y heurísticas para evaluar el tablero. Además, se emplean aperturas extraídas de un archivo PGN (*Novikov.pgn*) para mejorar la fase inicial de las partidas.

## Estructura del Proyecto

El repositorio se organiza de la siguiente manera:

```plaintext
ChessAgentsProject/
├── README.md            # Instrucciones de uso y resumen del proyecto.
├── report.md            # Informe detallado del proyecto.
├── main.py              # Código principal que simula el torneo.
├── Novikov.pgn          # Archivo PGN con aperturas (base de datos de partidas).
└── agents/              # Módulos individuales de los agentes de ajedrez.
├── __init__.py      # Inicialización del paquete de agentes.
├── base_agent.py    # Clase base compartida entre todos los agentes.
├── random_agent.py  # Implementación del agente que elige movimientos al azar.
├── hill_climbing_agent.py  # Agente basado en Hill Climbing.
├── simulated_annealing_agent.py  # Agente que utiliza Simulated Annealing.
├── minimax_agent.py  # Agente que implementa el algoritmo Minimax.
└── alphabeta_agent.py  # Agente que implementa Minimax con poda alfa-beta.
```

Esta estructura modular facilita la extensión y el mantenimiento del proyecto, permitiendo que cada agente se encuentre en su propio módulo y que el código principal se concentre en la simulación y comparación de resultados.

## Requisitos

- Python 3.x
- [chess](https://pypi.org/project/chess/)

Instala las dependencias ejecutando:

```bash
pip install chess
```

## Cómo Ejecutar el Proyecto

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/adriancho91s/ai-chess-agents.git
   cd ai-chess-agents
   ```

2. **Verificar el archivo PGN:**

   Asegúrate de que el archivo `Novikov.pgn` se encuentre en la raíz del repositorio. Si la ruta es diferente, actualiza la variable `pgn_file` en `main.py`.

3. **Ejecutar el torneo:**

   Ejecuta el archivo principal:

   ```bash
   python main.py
   ```

   Durante la ejecución se te solicitará elegir el modo de visualización:
   - **1:** Modo gráfico (usa `chess.svg` para mostrar el tablero).
   - **2:** Modo texto (imprime el tablero en consola).
     
   Durante la ejecución se te solicitará elegir un delay (en segundos) entre movimientos (0 para desactivar).
   Al final se mostrará la tabla de resultados generada dinámicamente.

4. **Ejecutar en Google Colab:**

   También puedes ejecutar este proyecto en Google Colab. Abre el siguiente enlace para ejecutar el Notebook:

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1puoo94dvGLkbRCZd4HsmXFyL7N92LiQ8?usp=sharing)

## Funcionalidades Destacadas

- **Implementación Modular:**  
  Cada agente se encuentra en su propio módulo, lo que facilita la comprensión y extensión del código.

- **Uso de Aperturas en PGN:**  
  Se extraen las aperturas (los primeros 5 movimientos) del archivo PGN para mejorar la fase inicial del juego, lo que proporciona una ventaja estratégica.

- **Comparación de Agentes:**  
  Se simulan torneos entre agentes (incluyendo RandomAgent, HillClimbingAgent, SimulatedAnnealingAgent, MinimaxAgent y AlphaBetaAgent) y se generan tablas dinámicas con los resultados.

- **Visualización Flexible:**  
  El usuario puede elegir entre visualización gráfica (usando `chess.svg`) o modo texto para observar la partida.

## Conclusión

Este proyecto cumple con todos los requerimientos de la asignatura:

1. **Código fuente bien documentado de cada agente.**
2. **Informe detallado** en `report.md` que explica la implementación, mejoras al usar aperturas, comparación de rendimiento, tablas de resultados y evaluación de heurísticas.
3. **Simulación de partidas y registro de resultados** (con posibilidad de exportar partidas en formato PGN para análisis adicional).

¡Disfruta explorando y ampliando este proyecto de agentes de ajedrez!

---

Si tienes alguna duda o deseas contribuir, no dudes en abrir un _issue_ o enviar un _pull request_.