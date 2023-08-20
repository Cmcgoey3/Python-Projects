Finding Minimum Weight Cycle in Weighted Directed Graph
Overview
In this project, I aim to design an algorithm to find a cycle in a weighted directed graph with no negative cycles, such that the cycle has the minimum weight. The algorithm should run in O(|V|^3) time complexity.

Algorithm
The proposed algorithm builds upon the Floyd-Warshall algorithm (FM algorithm) to find the maximum spanning tree. The steps are as follows:

1. The algorithm utilizes the core concepts of the FM algorithm but extends the adjacency matrix to include additional space for storing the list of vertices visited along the path.
2. The matrix stores both the distance between edges and a list (or hashmap) of visited vertices along the path.
3. When a new minimum distance is discovered while visiting a vertex, the algorithm overrides the vertex list of the minimum path with that of the new minimum's vertex list. Initially, each vertex has an empty list.
4. As the algorithm progresses from node X to node Y, if Y already contains X in its vertex list, a cycle has been detected. This cycle is guaranteed to be a minimum cycle due to the nature of the FM algorithm.
5. The algorithm stores the cycle length (or the entire cycle) until all possible starting points have been explored.

Correctness
The algorithm's correctness is founded on expanding the established FM algorithm, which is a proven approach. By utilizing the logic behind finding all minimum paths and leveraging the storage of vertices in the matrix, the algorithm ensures the detection of minimal cycles. The algorithm's approach to detecting cycles at each step guarantees their minimal nature.

Time and Space Complexity
The algorithm's time complexity aligns with that of the FM algorithm, O(|V|^3), due to the addition of O(|V|^2) space required to store the vertex list in each matrix element. If a hashmap is employed for searching element existence, the search operation becomes constant time, maintaining a time complexity of O(|V|^3). The algorithm's extra space usage and time complexity are reasonable trade-offs for the ability to detect minimum weight cycles in the graph.