# graph/builder.py
# Construye y compila el grafo ReAct de RaceIntel.
# Patrón: race_agent ⇆ tools  (loop hasta que el LLM no llame herramientas)

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from graph.state import RaceIntelState
from agents.race_agent import race_agent, get_tools


def build_graph():
    """Construye el grafo principal y lo devuelve compilado."""
    tools = get_tools()
    tool_node = ToolNode(tools)

    builder = StateGraph(RaceIntelState)

    # Nodos
    builder.add_node("race_agent", race_agent)
    builder.add_node("tools", tool_node)

    # Aristas
    builder.add_edge(START, "race_agent")
    builder.add_conditional_edges(
        "race_agent",
        tools_condition,          # sigue a "tools" si hay tool_calls, si no → END
    )
    builder.add_edge("tools", "race_agent")   # resultado vuelve al agente

    return builder.compile()
