# Graph

## Introduction
### Composition:
    1. Vertex (Node)
    2. Edges
  ### Types
    1. Directed 
    2. Undirected
  ### Representation
    1. Matrix (A_ij)
        Suitable for dense graph
        Highly inefficient if the matrix is sparse
    2. Adjacency list
      array of vertices
      array of edges
      each edge points to its end points
      each vertex points to edges incident on it
  
  ## Min cut problem
    
    Input: an undirected graph G = (V, E), parallel edges allowed
    
    Goal: Compute a cut with fewest number of crossing edges
    
  ### Applications
    1. Computer vision: Image segamentation
    2. Identify network bottle neck
    3. Community detection in social networks
  
  ### Random Contraction Algorithm
  
    While there are more than 2 vertices:
      pick a remaining edge (u, v) uniformly at random
      merge u and v into a single vertex
      remove self-loops
    return cut represented by final 2 vertices