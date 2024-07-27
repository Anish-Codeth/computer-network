To ensure the links are embedded in the text without showing the URLs explicitly, you can use Markdown formatting. Here is the improved Markdown content:

---

# Assignments

## Assignment 1
[Assignment One Repository](https://github.com/Anish-Codeth/computer-network/tree/main/Assignment-one)

---

## Shortest Path Algorithms

### Dijkstra's Algorithm

#### Algorithm

1. **Initialization:**
   a. Create a priority queue and insert the starting node with a distance of 0.
   b. Initialize distances to all nodes as infinity, except the starting node, which is 0.
   c. Set the previous node for each node to None.

2. **Processing Nodes:**
   a. While the priority queue is not empty:
      i. Extract the node with the smallest distance from the priority queue.
      ii. For each neighbor of the extracted node:
          1. Calculate the new distance from the starting node to this neighbor through the extracted node.
          2. If this new distance is less than the currently known distance to this neighbor:
             a. Update the neighbor's distance.
             b. Set the previous node of the neighbor to the extracted node.
             c. Insert the neighbor into the priority queue with the updated distance.

3. **Completion:**
   a. Continue processing until all reachable nodes have been processed and their shortest distances from the starting node have been found.
   b. The distances array now contains the shortest path distances from the starting node to all other nodes.
   c. The previous nodes array can be used to reconstruct the shortest path from the starting node to any other node.

#### [Link to the Code](https://github.com/Anish-Codeth/computer-network/blob/main/shortest/deijkstra/dijkstra.py)

#### [Link to the Code using Heap](https://github.com/Anish-Codeth/computer-network/blob/main/shortest/deijkstra/dijkstraheap.py)

#### [Update of the Variables](https://github.com/Anish-Codeth/computer-network/blob/main/shortest/deijkstra/dijkstra.png)

---

