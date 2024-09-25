from datetime import datetime 
from typing import Callable

def normalize_value(value: float, min_value: float, max_value: float) -> float:
  """normaliza o valor entre 0 e 1"""
  return ((value - min_value) / (max_value - min_value))

def normalize_report(data: dict[str, list[float]]): 
  """normaliza as durações de cada alternativa (entre 0 e 1)"""
  result: dict[str, float] = {}
  _max = 0
  _min = 0
  for key, value in data.items():
    if _max > 0:
      value.append(_max)
    _max = max(value)
    if _min > 0:
      value.append(_min)
    _min = min(value)
  
  for key, value in data.items():
    new_values = [normalize_value(x, _min, _max) for x in value]
    result.update({
      key: sum(new_values) / len(new_values)
    })

  return result

def test_alternatives(alternatives: Callable[[list[int]], None], ranges: list[int]) -> tuple[dict[str, float], str]: 
  """
  testa alternativas injetando as listas criadas a partir dos raios fornecidos
  retorn: reporte e melhor alternativa 
  """
  report: dict[str, list[float]] = {}
  for range_size in ranges:
    for alt in alternatives: 
      start_at = datetime.now()
      alt(range(range_size))
      end_at = datetime.now()
      duration = (end_at - start_at).total_seconds()
      report.setdefault(alt.__name__, []).append(duration)
  return normalize_report(report), min(report, key=report.get)
