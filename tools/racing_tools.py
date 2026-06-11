# tools/racing_tools.py
# Herramientas especializadas de búsqueda para el agente RaceIntel.
# Cada tool restringe la búsqueda a un dominio concreto del automovilismo.

import os
from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults


def _tavily(max_results: int = 4) -> TavilySearchResults:
    """Instancia un cliente Tavily con el número de resultados indicado."""
    return TavilySearchResults(
        max_results=max_results,
        tavily_api_key=os.getenv("TAVILY_API_KEY"),
    )


@tool
def search_race_results(query: str) -> str:
    """Busca resultados de carreras: ganadores, podios y tiempos de vuelta.

    Úsala para preguntas como: '¿quién ganó el GP de Mónaco 2024?',
    '¿cuál fue el podio en Le Mans 2023?', 'resultado Dakar etapa 5 2025'.
    """
    refined = f"race result winner podium {query}"
    results = _tavily(4).invoke(refined)
    if not results:
        return "No se encontraron resultados para esa carrera."
    return "\n\n".join(
        f"[{r.get('url', '')}]\n{r.get('content', '')[:300]}"
        for r in results
        if isinstance(r, dict)
    )


@tool
def search_driver_stats(query: str) -> str:
    """Busca estadísticas, palmarés y biografía de pilotos.

    Úsala para preguntas como: '¿cuántos mundiales tiene Verstappen?',
    'estadísticas de Fernando Alonso en F1', 'historial de Scott Dixon en IndyCar'.
    """
    refined = f"driver statistics career stats {query}"
    results = _tavily(4).invoke(refined)
    if not results:
        return "No se encontraron estadísticas para ese piloto."
    return "\n\n".join(
        f"[{r.get('url', '')}]\n{r.get('content', '')[:300]}"
        for r in results
        if isinstance(r, dict)
    )


@tool
def search_championship_standings(query: str) -> str:
    """Busca clasificaciones de campeonatos: F1, IndyCar, NASCAR, WEC, Dakar, etc.

    Úsala para preguntas como: '¿cómo va el campeonato de F1 2025?',
    'clasificación WEC 2024 LMP1', 'standings NASCAR Cup Series'.
    """
    refined = f"championship standings classification 2025 {query}"
    results = _tavily(4).invoke(refined)
    if not results:
        return "No se encontraron datos de clasificación."
    return "\n\n".join(
        f"[{r.get('url', '')}]\n{r.get('content', '')[:300]}"
        for r in results
        if isinstance(r, dict)
    )


@tool
def search_race_calendar(query: str) -> str:
    """Busca calendarios de temporada y próximas citas de carreras.

    Úsala para preguntas como: '¿cuándo es la próxima carrera de F1?',
    'calendario IndyCar 2025', '¿qué circuitos tiene el WEC esta temporada?'.
    """
    refined = f"race calendar schedule next race 2025 {query}"
    results = _tavily(3).invoke(refined)
    if not results:
        return "No se encontró información de calendario."
    return "\n\n".join(
        f"[{r.get('url', '')}]\n{r.get('content', '')[:300]}"
        for r in results
        if isinstance(r, dict)
    )
