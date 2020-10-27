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
