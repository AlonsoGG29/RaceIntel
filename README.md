# 🏁 RaceIntel

Asistente conversacional de automovilismo construido con **LangGraph** y trazabilidad en **LangSmith**.
Cubre F1, IndyCar, NASCAR, WEC (Le Mans) y Dakar.

---

## ¿Qué hace?

RaceIntel es un agente **ReAct** (Reasoning + Acting) que recibe preguntas en lenguaje natural sobre carreras de motor y decide, de forma autónoma, qué herramienta de búsqueda usar para obtener datos actualizados antes de responder.

### Workflow

```
START → race_agent ──(tool_calls?)──► tools ──► race_agent → END
                  └──────(no tools)──────────────────────────►
```

El bucle `race_agent ⇄ tools` se repite hasta que el LLM considera que tiene suficiente información para responder. A diferencia de pipelines con nodos fijos, aquí **el propio modelo decide** el número de llamadas y qué herramienta invocar en cada paso.

### Herramientas disponibles

| Herramienta | Cuándo se usa |
|---|---|
| `search_race_results` | Ganadores, podios y tiempos de carrera |
| `search_driver_stats` | Estadísticas y palmarés de pilotos |
| `search_championship_standings` | Clasificaciones de campeonato |
| `search_race_calendar` | Calendario y próximas carreras |

### Tracing en LangSmith

Cada sesión genera un `session_id` único que se usa como `thread_id` y `run_name`. Todas las trazas van al proyecto `raceintel` en LangSmith, donde se puede inspeccionar cada llamada al LLM y cada invocación de herramienta.

---

## Estructura del proyecto

```
raceintel/
├── main.py                  # Punto de entrada y bucle de conversación
├── requirements.txt
├── .env.example
├── graph/
│   ├── state.py             # RaceIntelState (TypedDict con messages + session_id)
│   └── builder.py           # Construcción y compilación del grafo
├── agents/
│   └── race_agent.py        # Nodo ReAct: LLM con herramientas enlazadas
└── tools/
    └── racing_tools.py      # Cuatro herramientas Tavily especializadas
```

---

## Instalación y ejecución

### 1. Clonar y crear entorno

```bash
cd raceintel
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configurar credenciales

```bash
cp .env.example .env
# Edita .env con tus claves
```

Variables necesarias:

| Variable | Descripción |
|---|---|
| `OPENAI_API_KEY` | Clave de Azure OpenAI |
| `AZURE_OPENAI_BASE_URL` | Endpoint de tu despliegue en Azure |
| `TAVILY_API_KEY` | Clave de [Tavily](https://tavily.com) (búsqueda web) |
| `LANGSMITH_API_KEY` | Clave de [LangSmith](https://smith.langchain.com) |
| `LANGSMITH_TRACING` | `true` para activar el tracing |
| `LANGSMITH_PROJECT` | Nombre del proyecto en LangSmith (`raceintel`) |

### 3. Ejecutar

```bash
python main.py
```

---

## Ejemplos de uso

```
Tú: ¿Quién ganó el GP de Mónaco 2024?
Tú: ¿Cómo va el campeonato de F1 2025?
Tú: Estadísticas de Fernando Alonso en F1
Tú: ¿Cuándo es la próxima carrera de IndyCar?
Tú: ¿Qué equipos ganaron Le Mans 2024 en LMP2?
```

Escribe `salir` para terminar la sesión.
