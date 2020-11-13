# Algorithm_specialization

## Divide and Conquer
  ### The paradim
    1. Divide into smaller subproblems
    2. Conquer via recursive calls.
    3. Combine solution of subproblems
  
  ### Algorithms
    1. The karatsuba algorithm -- large number multiplication
    2. The Merge Sort algorithm -- Sorting
    3. The number of inversion problem -- Utilizing Merge Sort
    4. Strassen's Algorithm -- Matrix Multiplication
    4. The Closest pair problem -- Find the closet pair of points among point set
    4. The Quick Sort algorithm -- Sorting
    
  ### The Master Method
    $T(n) \leq aT(\frac{n}{b}) + O(n^d)$
    n: Dimension of problem
    a: Number of recursive calls\\
    b: Factor by which the input size shrink\\
    d: Exponent in the amount of work done outside of the recursive call
    
    \begin{align}
    T(n) &= O(n^dlogn)\ if a = b^d\\
    T(n) &= O(n^d) \ if a < b^d\\
    T(n) &= O(n^{log_b^a})\ if a >b^d
    \end{align}    

## Graph

  ### Introduction
  #### Composition:
    1. Vertex (Node)
    2. Edges
  #### Types
    1. Directed 
    2. Undirected
  #### Representation
    1. Matrix (A_ij)
    2. Adjacency list
      array of vertices
      array of edges
      each edge points to its end points
      each vertex points to edges incident on it
  
  ### Min cut problem
    
    Input: an undirected graph G = (V, E), parallel edges allowed
    
    Goal: Compute a cut with fewest number of crossing edges
    
  #### Applications
    1. Computer vision: Image segamentation
    2. Identify network bottle neck
    3. Community detection in social networks
  
  #### Random Contraction Algorithm
  
    While there are more than 2 vertices:
      pick a remaining edge (u, v) uniformly at random
      merge u and v into a single vertex
      remove self-loops
    return cut represented by final 2 vertices
