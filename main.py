from collections import deque
import heapq
from heapq import heappush, heappop


def shortest_shortest_path(graph, source):
  """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
  distances = {v: float('inf') for v in graph}
  distances[source] = 0
  edges = {v: float('inf') for v in graph}
  edges[source] = 0
  priority_queue = [(0, 0, source)]

  while priority_queue:
    current_distance, edge, current_vertex = heapq.heappop(priority_queue)
    if current_distance > distances[current_vertex]:
      continue
    for neighbor, weight in graph[current_vertex]:
      distance = current_distance + weight
      if distance < distances[neighbor] or (distance == distances[neighbor]
                                            and edge + 1 < edges[neighbor]):
        distances[neighbor] = distance
        edges[neighbor] = edge + 1
        heapq.heappush(priority_queue, (distance, edge + 1, neighbor))
  return {vertex: (distances[vertex], edges[vertex]) for vertex in graph}
  pass


def bfs_path(graph, source):
  """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
  queue = deque([source])
  parents = {source: None}

  while queue:
    current_vertex = queue.popleft()

    for neighbor in graph[current_vertex]:
      if neighbor not in parents:
        parents[neighbor] = current_vertex
        queue.append(neighbor)

  return parents
  pass


def get_sample_graph():
  return {'s': {'a', 'b'}, 'a': {'b'}, 'b': {'c'}, 'c': {'a', 'd'}, 'd': {}}


def get_path(parents, destination):
  """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
  path = []
  current_node = destination

  while current_node is not None:
    path.append(current_node)
    current_node = parents[current_node]

  path = path[::-1][:-1]
  return ''.join(path)
  pass
