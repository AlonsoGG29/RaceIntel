# agents/race_agent.py
# Nodo principal del agente: LLM con herramientas enlazadas (ReAct pattern).
# Recibe el historial completo y devuelve el siguiente mensaje.

import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage

from graph.state import RaceIntelState
from tools.racing_tools import (
    search_race_results,
    search_driver_stats,
    search_championship_standings,
    search_race_calendar,
)

SYSTEM_PROMPT = """Eres RaceIntel, un asistente especializado en automovilismo.
Cubres Formula 1, F2, F3 y Formula E, IndyCar e IndyNext, NASCAR, WEC (Le Mans), Dakar y otras series de velocidad.

Reglas:
- Usa las herramientas disponibles para obtener datos actualizados antes de responder.
- Si se piden ESTADÍSTICAS o DATOS específicos: usa formato de lista con viñetas (•) o numerado.
- Si se pide INFORMACIÓN general: responde en español con tono conciso y periodístico (máx. 3 párrafos).
- Cita las fuentes cuando sea relevante.
- Si la pregunta no es sobre automovilismo, indícalo amablemente y ofrece ayuda dentro de tu especialidad.
- Nunca inventes datos; si no encuentras información, dilo."""

_TOOLS = [
    search_race_results,
    search_driver_stats,
    search_championship_standings,
    search_race_calendar,
]


def get_tools() -> list:
    """Devuelve la lista de herramientas disponibles para el agente."""
    return _TOOLS


def _build_llm():
    """Construye el LLM con las herramientas enlazadas."""
    llm = ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("AZURE_OPENAI_BASE_URL"),
        model="gpt-4o-mini",  # Cambia esto por tu nombre de deployment en Azure si es diferente
        temperature=0.2,
    )
    return llm.bind_tools(_TOOLS)


# Se instancia una única vez al importar el módulo
_llm_with_tools = _build_llm()


def race_agent(state: RaceIntelState) -> RaceIntelState:
    """Invoca el LLM con el historial de mensajes y devuelve la respuesta."""
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]
    response = _llm_with_tools.invoke(messages)
    print(f"🏎️  [RaceAgent] {'Llamando herramientas: ' + str([tc['name'] for tc in response.tool_calls]) if response.tool_calls else 'Respuesta final lista'}")
    return {"messages": [response]}
