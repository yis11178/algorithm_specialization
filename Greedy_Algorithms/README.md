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
  
        sort edges in order of increasing cost
        T = null set
        for i = 1 to M: (1 being cheapest and M being most expensive)
          if T and i form no cycles (linear running time with naive graph search)
          add i to T
        return T
        
  * Union-find Data structure 
  
    - Partition of a set of objects
    - Used to accelerate Kruskal's algorithm
    
    - Operations 
      
      find(x) : return name of group that x belongs to
      union(ci, cj) : fuse group ci and cj into a single one 
    
    - Invariants
      
      each vertex points to the 'leader' of its component
      
    
    
