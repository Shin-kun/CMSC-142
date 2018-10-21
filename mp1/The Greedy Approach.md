# The Greedy Approach

Solve these problems using the greedy method

- **Knight's Tour** 
  - Given an $m \times n$ chessboard and a starting point $(i,j)$ , Find the knights path that traverses all of the squares in the board
- **Set Cover Problem**
  - Given a universal set $U$ and a set of sets $S$ such that $\cup_{t \in S} t=U$. Find the subset of $S$ with the least elements, $C$ such that $\cup_{t \in C} t=U$.
  - Example:
    - $U=\{1,2,3,4,5,6,7,8\}$
    - $S=\{\{1,2\},\{7,8\},\{2,3,4,5,6,7,\},\{1,2,3,4\},\{5,6,7,8\},\{5,6,7\}\}$
    - $C=\{\{2,3,4,5,6,7,\},\{1,2\},\{7,8\}\}$(greedy solution) 
- **Coin Change Problem**
  - Given a set of coins $S$, and an amount of money $m$. Find the smallest amount of coins that could represent $m$.
- **Sorting an Array**
  - Given a sequence of numbers $S$, Find the sorted sequence $S'$

Indicate the time complexities of your solutions. Write it as comments to your code.