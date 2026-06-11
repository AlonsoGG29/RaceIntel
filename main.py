# main.py
# Punto de entrada de RaceIntel.
# Configura LangSmith tracing y lanza el bucle de conversación.

import os
import uuid
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

load_dotenv()

# ── LangSmith: basta con las variables de entorno (cargadas desde .env) ──────
# LANGSMITH_TRACING=true
# LANGSMITH_API_KEY=<key>
# LANGSMITH_PROJECT=raceintel          ← todas las trazas irán a este proyecto

from graph.builder import build_graph

BANNER = """
╔══════════════════════════════════════════╗
║  🏁  RaceIntel — Asistente de Carreras  ║
║  F1 · IndyCar · NASCAR · WEC · Dakar    ║
╚══════════════════════════════════════════╝
Escribe tu pregunta o 'salir' para terminar.
"""


def run():
    """Ejecuta el bucle de conversación multi-turno."""
    graph = build_graph()
    session_id = str(uuid.uuid4())[:8]
    conversation_history = []

    print(BANNER)
    print(f"🔗 Sesión: {session_id}  |  Tracing → proyecto '{os.getenv('LANGSMITH_PROJECT', 'default')}'\n")

    while True:
        try:
            user_input = input("Tú: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n👋 ¡Hasta la próxima!")
            break

        if user_input.lower() in ("salir", "exit", "quit", "q"):
            print("👋 ¡Hasta la próxima!")
            break

        if not user_input:
            continue

        # Acumula el nuevo mensaje al historial
        conversation_history.append(HumanMessage(content=user_input))

        # Invoca el grafo con el historial completo y el session_id
        result = graph.invoke(
            {
                "messages": conversation_history,
                "session_id": session_id,
            },
            config={
                "configurable": {"thread_id": session_id},
                "run_name": f"raceintel-{session_id}",   # nombre visible en LangSmith
            },
        )

        # Extrae la respuesta del asistente y la añade al historial
        assistant_message = result["messages"][-1]
        conversation_history = result["messages"]   # actualiza con todo (tool msgs incluidos)

        print(f"\n🏎️  RaceIntel: {assistant_message.content}\n")


if __name__ == "__main__":
    run()
