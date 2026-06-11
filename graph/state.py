# graph/state.py
# Define el estado compartido del grafo principal.

from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class RaceIntelState(TypedDict):
    """Estado del agente RaceIntel.

    - messages: historial completo de la conversación (HumanMessage, AIMessage, ToolMessage).
      Usa add_messages como reducer para acumular sin sobrescribir.
    - session_id: identificador de sesión para LangSmith tracing.
    """
    messages: Annotated[list, add_messages]
    session_id: str
