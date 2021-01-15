# Greedy Algorithm

## Application

### Internet Routing

* Find shortest path from one site to another

* Impossible to maintain a record for websites globally

* Not practical to use the Dijkstra's algorithm

* Bellmam-Ford Algorithm (can be thought as dynamic programming)

### Sequence Alignment

* Find similarity between two strings (e.g. `AGGGCT` and `AGGCA`)

* Similarity is computed by the minimum penalty to align the sequences

* +ve penalty for each gap (inserted between characters)

* +ve penalty for each mismatch characters 


## Minimum Spanning Tree Problem (MST)

### Informal Goal 

  Connect a bunch of points together as cheaply as possible. 
  
### Input 

  undirected graph G = (V, E) and a cost c_e for each edge
  
  * Assume adjacency list representation
  
  * Negative edges are allowed
  
### Output

  Minimum cost tree T in E that span all vertices
  
  * cost = sum of edge costs
  
  * The subgraph is connected
  
### Application

  * Clustering
  
  * Networking
  
### Algorithms

  Running time: O(mlogn) with m = number of edges, n = numbers of vertices

  * Prim's Algorithm (Similar to Dijkstra's algorithm)
  
        initialize X = [s] (s chosen from V arbitrarily)
        T = null set 
        while X != V:
          let e = (u, v) be the cheapest edge of G with u in X, v not in X
          add e to T
          add v to X
  
  * Kruskal's Algorithm
