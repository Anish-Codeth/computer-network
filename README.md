# Assignments

## Assignment 1

[Assignment One Repository](https://github.com/Anish-Codeth/computer-network/tree/main/Assignment-one)

---

## Shortest Path Algorithms

### Dijkstra's Algorithm

#### Algorithm

1. **Initialization:**
   - Create a priority queue and insert the starting node with a distance of 0.
   - Initialize distances to all nodes as infinity, except the starting node, which is 0.
   - Set the previous node for each node to None.

2. **Processing Nodes:**
   - While the priority queue is not empty:
     1. Extract the node with the smallest distance from the priority queue.
     2. For each neighbor of the extracted node:
        - Calculate the new distance from the starting node to this neighbor through the extracted node.
        - If this new distance is less than the currently known distance to this neighbor:
          - Update the neighbor's distance.
          - Set the previous node of the neighbor to the extracted node.
          - Insert the neighbor into the priority queue with the updated distance.

3. **Completion:**
   - Continue processing until all reachable nodes have been processed and their shortest distances from the starting node have been found.
   - The distances array now contains the shortest path distances from the starting node to all other nodes.
   - The previous nodes array can be used to reconstruct the shortest path from the starting node to any other node.

#### [Link to the Code](https://github.com/Anish-Codeth/computer-network/blob/main/shortest/deijkstra/dijkstra.py)

#### [Link to the Code using Heap](https://github.com/Anish-Codeth/computer-network/blob/main/shortest/deijkstra/dijkstraheap.py)

#### [Update of the Variables](https://github.com/Anish-Codeth/computer-network/blob/main/shortest/deijkstra/dijkstra.png)

### Alternative Approach: Bellman-Ford Algorithm

1. **Algorithm Steps:**
   - Initialize an array `dist` with size `n` to store the minimum cost to reach each city from `src`. Set `dist[src]` to 0 and all other entries to ∞.
   - Relax all edges `n−1` times:
     - For each flight `[u, v, w]` in `flights`, if `dist[u] + w < dist[v]`, update `dist[v]` to `dist[u] + w`.
   - After `n−1` iterations, `dist[dst]` contains the minimum cost to reach `dst` from `src` with at most `k` stops or `-1` if no such path exists.