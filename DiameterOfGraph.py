import random

def find_diameter(n, p):
  # n is the number of nodes and p is the probability of edge creation
  graph = {}

  # Create a dictionary with node as key and list of connected nodes as value
  for node in range(n):
    graph[node] = []
    for i in range(n):
      if node != i and random.random() < p:
        graph[node].append(i)

  def bfs(node, parent):
    # perform breadth-first search and return the distance from node to farthest node
    queue = [(node, 0)]
    visited = set()
    farthest_node = node
    farthest_distance = 0

    while queue:
      current, distance = queue.pop(0)
      visited.add(current)
      if distance > farthest_distance:
        farthest_distance = distance
        farthest_node = current
      for neighbor in graph[current]:
        if neighbor not in visited:
          queue.append((neighbor, distance + 1))

    return farthest_node, farthest_distance

  # Perform bfs starting from each node and find the farthest node
  farthest_node, farthest_distance = bfs(0, None)
  _, diameter = bfs(farthest_node, None)

  return diameter

# generate a random graph with 10 nodes and edge creation probability of 0.5
diameter = find_diameter(10, 0.5)
print("Diameter of the random graph: ", diameter)