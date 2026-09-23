<div align="center">

# RaceIntel: Asistente inteligente sobre automovilismo

<img src="https://live.staticflickr.com/65535/55546573056_0a35d63761_b.jpg" />

### Un agente conversacional diseñado para responder preguntas reales sobre Fórmula 1, IndyCar, NASCAR, WEC, Dakar y otras competiciones de motor, usando búsqueda actualizada y razonamiento automatizado.
</div>

## Visión general

RaceIntel nace como una solución práctica para transformar consultas naturales en respuestas accionables sobre el mundo del motor. En lugar de depender de un flujo rígido o de un sistema estático, el agente decide de forma autónoma qué información necesita, qué fuentes consultar y cómo combinar los resultados antes de responder.

Esto lo convierte en una herramienta útil tanto para:

- estudiantes y aficionados que quieren entender resultados, estadísticas o calendario,
- profesionales que necesitan consultas rápidas sin navegar varias fuentes,
- presentaciones, demos o prototipos de IA con valor real para un cliente o evaluador técnico.

---

## ¿Qué hace?

RaceIntel permite hacer preguntas como:

- ¿Quién ganó el GP de Mónaco 2024?
- ¿Cómo va el campeonato de NASCAR 2025?
- ¿Cuáles son las estadísticas de Fernando Alonso en F1?
- ¿Cuándo es la próxima carrera de IndyCar?
- ¿Qué equipos ganaron Le Mans 2024 en LMP2?

Y responde con información basada en fuentes web recientes, usando herramientas especializadas para cada tipo de consulta.

---

## ¿Por qué es interesante?

### 1. Búsqueda inteligente, no respuesta aleatoria
El sistema no intenta “adivinar” respuestas. Primero identifica la intención del usuario y luego usa herramientas específicas para recuperar datos recientes y relevantes.

### 2. Diseño basado en agentes
La arquitectura sigue un patrón ReAct: el modelo razona, elige una herramienta, analiza la respuesta y continúa hasta tener suficiente información para dar una respuesta útil.

### 3. Preparado para demostración técnica
Es ideal para mostrar en clase, en una entrevista técnica o ante un cliente cómo funciona una aplicación de IA con:

- Orquestación de agentes,
- Integración de herramientas externas,
- Trazabilidad y observabilidad,
- Experiencia conversacional con memoria de sesión.

### 4. Escalable y extensible
La estructura actual cubre varias competiciones y puede ampliarse con nuevas series, filtros o fuentes de datos.

---

## Flujo de uso

![Flujo de uso](https://live.staticflickr.com/65535/55546634408_8ffa1f1785_m.jpg)

El sistema se repite en varios pasos hasta que el modelo considera que ya tiene suficiente contexto para responder.

---

## Experiencia de usuario


### Cobertura deportiva

RaceIntel cubre varias disciplinas del automovilismo, incluyendo:

<div align="center">

<table>
  <tr>
    <td align="center" width="300">
      <img src="https://thumb.wikimedia.org/wikipedia/commons/thumb/3/33/F1.svg/3840px-F1.svg.png?utm_source=es.wikipedia.org&utm_campaign=index&utm_content=thumbnail" height="50" alt="Fórmula 1" /><br />
      <sub><b>Fórmula 1</b></sub>
    </td>
    <td align="center" width="300">
      <img src="https://thumb.wikimedia.org/wikipedia/commons/thumb/f/ff/IndyCar_Series_textlogo.svg/500px-IndyCar_Series_textlogo.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail&_=20210511055910" height="50" alt="IndyCar" /><br />
      <sub><b>IndyCar</b></sub>
    </td>
    <td align="center" width="300">
      <img src="https://thumb.wikimedia.org/wikipedia/commons/thumb/6/67/NASCAR_logo_2017.svg/330px-NASCAR_logo_2017.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail&_=20171113040636" height="50" alt="NASCAR" /><br />
      <sub><b>NASCAR</b></sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="300">
      <img src="https://upload.wikimedia.org/wikipedia/commons/4/4c/FIA_WEC_Logo_2024.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail_unscaled&_=20250803222127" height="80" alt="WEC / Le Mans" /><br />
      <sub><b>WEC</b></sub>
    </td>
    <td align="center" width="300">
      <img src="https://www.blunik.com/clients/blunik/racing/rally/images/1567_details.webp" height="80" alt="Dakar" /><br />
      <sub><b>Dakar</b></sub>
    </td>
    <td align="center" width="300">
      <img src="https://upload.wikimedia.org/wikipedia/commons/a/a2/EPrix_logo.svg?utm_source=es.wikipedia.org&utm_campaign=index&utm_content=original" height="45" alt="Dakar" /><br />
      <img src="https://content.presspage.com/uploads/2368/11bf6d9c-b3e5-4b83-9443-36f44f83063e/800_logofia.png?x=1734527936410" height="35" alt="WEC / Le Mans" /><br />
      <sub><b>Otras competiciones</b></sub>
    </td>
  </tr>
</table>

</div>

---

### Ejemplos de interacción

#### Puedes buscar de forma individual a una herramienta:
![Búsqueda individual de estadísticas](https://live.staticflickr.com/65535/55546693839_97510f33f2_b.jpg)
---

#### Si la herramienta no está segura del todo de la respuesta, se autoejecuta varias veces para comprobar que la información es correcta:
![Comprobando búsqueda](https://live.staticflickr.com/65535/55546634423_2d903409c2_b.jpg)
---

#### También puede acceder a varias herramientas si el resultado lo pide:
![Múltiples herramientas](https://live.staticflickr.com/65535/55546634413_76a4e1ef9e_b.jpg)




---

## Stack tecnológico

RaceIntel combina varias herramientas modernas para construir una experiencia de IA útil y observable:

- Python
- LangGraph para la orquestación del agente
- LangChain para integración de modelos y herramientas
- Azure OpenAI / OpenAI para el modelo de lenguaje
- Tavily para búsqueda web especializada
- LangSmith para trazabilidad y seguimiento de ejecuciones
- Variables de entorno para configuración segura

---

## Arquitectura técnica

La solución está organizada en módulos claros y mantenibles:

```text
RaceIntel/
├── main.py                     # Entrada principal y bucle conversacional
├── README.md                  # Documentación base del proyecto
├── README_Nuevo.md            # Presentación visual y orientada a cliente
├── requirements.txt           # Dependencias del proyecto
├── .env.example               # Plantilla de variables de entorno
├── graph/
│   ├── __init__.py
│   ├── builder.py             # Construcción del grafo del agente
│   └── state.py               # Estado de la sesión y mensajes
├── agents/
│   ├── __init__.py
│   └── race_agent.py          # Nodo principal con el modelo y herramientas
├── tools/
│   ├── __init__.py
│   └── racing_tools.py        # Herramientas para resultados, stats y calendario
└── raceintel.ipynb            # Exploración y prototipado
```

### Componentes clave

- `main.py`: lanza la conversación y mantiene la sesión.
- `agents/race_agent.py`: define el agente ReAct con herramientas enlazadas.
- `tools/racing_tools.py`: encapsula búsquedas especializadas por categoría.
- `graph/builder.py`: conecta el flujo del grafo.
- `graph/state.py`: modela el estado de la conversación.

---

## Cómo funciona internamente

El agente usa un patrón de razonamiento y acción:

1. Recibe la pregunta del usuario.
2. Evalúa si necesita información externa.
3. Selecciona la herramienta más adecuada.
4. Busca datos relevantes en internet.
5. Procesa el contexto obtenido.
6. Genera una respuesta final clara y útil.
7. Mantiene trazabilidad de la ejecución en LangSmith.

Este enfoque es especialmente útil para aplicaciones donde el modelo debe decidir dinámicamente qué buscar y cómo responder a preguntas complejas.

---

## Herramientas disponibles

RaceIntel incluye cuatro herramientas especializadas:

- `search_race_results`: Resultados de carreras, ganadores, podios y tiempos de vuelta.
- `search_driver_stats`: Estadísticas y palmarés de pilotos.
- `search_championship_standings`: Clasificaciones de campeonatos.
- `search_race_calendar`: Calendarios y próximas fechas.

Cada una está diseñada para una categoría concreta del conocimiento automovilístico.

---

### Tracing en LangSmith

Cada sesión genera un `session_id` único que se usa como `thread_id` y `run_name`. Todas las trazas van al proyecto `raceintel` en LangSmith, donde se puede inspeccionar cada llamada al LLM y cada invocación de herramienta.

---

## Trazabilidad y observabilidad

Cada sesión genera un identificador único y se registra con seguimiento en LangSmith. Esto permite inspeccionar:

- llamadas al modelo,
- invocaciones a herramientas,
- pasos intermedios del agente,
- rendimiento y flujo de ejecución.

Esto es especialmente valioso en demos, validación técnica y análisis de comportamiento del asistente.

---

## Instalación y ejecución

### 1. Clonar el proyecto

```bash
cd RaceIntel
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Copia el ejemplo:

```bash
copy .env.example .env
```

o en Linux/macOS:

```bash
cp .env.example .env
```

Luego completa las claves necesarias:

```env
OPENAI_API_KEY=tu_clave
AZURE_OPENAI_BASE_URL=https://tu-endpoint
TAVILY_API_KEY=tu_clave_tavily
LANGSMITH_API_KEY=tu_clave_langsmith
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=raceintel
```

---

## Variables necesarias

| Variable | Descripción |
|---|---|
| `OPENAI_API_KEY` | Clave del modelo de OpenAI / Azure OpenAI |
| `AZURE_OPENAI_BASE_URL` | Endpoint del despliegue de Azure OpenAI |
| `TAVILY_API_KEY` | Acceso a búsqueda web para las herramientas |
| `LANGSMITH_API_KEY` | Credencial de trazabilidad en LangSmith |
| `LANGSMITH_TRACING` | Activa el tracing del proyecto |
| `LANGSMITH_PROJECT` | Nombre del proyecto de LangSmith |

---

## Ejecución del proyecto

```bash
python main.py
```

A partir de ahí, puedes interactuar con el asistente desde la terminal.

---

## Casos de uso reales

RaceIntel puede ser útil en escenarios como:

- asistentes de contenido deportivo,
- prototipos de IA para clientes,
- herramientas internas para consulta rápida de resultados,
- demos académicas y demostraciones de arquitectura multi-agente,
- sistemas de apoyo con búsqueda web y generación de respuestas contextualizadas.

---

## Conclusión

RaceIntel combina tres elementos clave para una demostración sólida de IA aplicada:

- conocimiento de un dominio concreto,
- capacidad de razonamiento y ejecución de herramientas,
- trazabilidad y observabilidad para validar cada decisión.

Es una solución clara, moderna y altamente visual para mostrar cómo una IA puede convertirse en un asistente útil y profesional dentro del mundo del automovilismo.

---

## Licencia

Este proyecto está pensado como ejemplo de aplicación de agentes conversacionales con IA aplicada a un dominio real y especializado.

Si quieres, puedo preparar también una versión aún más premium con:

- portada tipo landing page,
- badges visuales más modernos,
- sección de screenshots y flujo de UX,
- estilo más orientado a presentación para entregar a un cliente o profesor.



<div align="center">


<img src="https://img.shields.io/badge/AI%20Agent-Ready-1f6feb?style=for-the-badge" alt="AI Agent Ready" />
<img src="https://img.shields.io/badge/LangGraph-Workflow-4b1d3f?style=for-the-badge" alt="LangGraph" />
<img src="https://img.shields.io/badge/LangSmith-Tracing-ff6b6b?style=for-the-badge" alt="LangSmith" />
<img src="https://img.shields.io/badge/Tavily-Search-00c2a8?style=for-the-badge" alt="Tavily" />

</div>