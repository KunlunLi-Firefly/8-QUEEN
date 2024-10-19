# 8-QUEEN
This repository provides various algorithms for solving the classic N-Queens problem, where the goal is to place N queens on an N x N chessboard so that no two queens can attack each other
Backtracking
Hill Climbing
Simulated Annealing
Min-Conflicts
The performance of each algorithm is measured, and the solutions are displayed in a readable format.

Algorithms
1. Backtracking Algorithm (solve_n_queens)
This algorithm uses a brute-force recursive approach to explore possible queen placements. It checks if placing a queen in a position is safe (i.e., no two queens are attacking each other) before proceeding to place the next queen.
It returns the first valid solution for the N-Queens problem.
2. Hill Climbing Algorithm (hill_climbing)
Hill climbing is a heuristic search algorithm that starts with a random solution and iteratively makes local adjustments to improve it.
The algorithm attempts to minimize conflicts between queens and restarts if no solution is found.
3. Simulated Annealing (simulated_annealing)
Simulated Annealing is inspired by the annealing process in metallurgy. It gradually reduces the "temperature" to escape local optima and find a solution with minimal conflicts.
This algorithm searches for a solution by allowing occasional increases in the number of conflicts to escape local minima.
4. Min-Conflicts Algorithm (min_conflicts)
Min-Conflicts is a heuristic algorithm that tries to resolve the conflicts between queens by adjusting their positions iteratively.
The algorithm stops when no conflicts remain or when a maximum number of iterations is reached.
Execution Time Measurement
Each algorithm has its execution time measured using Python's time module. This helps compare the performance of different algorithms.


Example Usage
python

# Solving the N-Queens problem with different algorithms and measuring their performance.
n_queens = 8
print("Backtracking Solution:")
measure_performance(solve_n_queens, n_queens)

print("\nSimulated Annealing Solution:")
measure_performance(simulated_annealing, n_queens)

print("\nMin-Conflicts Solution:")
measure_performance(min_conflicts, 1000, n_queens)

print("\nHill Climbing Solution:")
measure_performance(hill_climbing, n_queens)


Output
The solution for each algorithm is printed in a human-readable chessboard format where Q represents a queen, and . represents an empty space. For example, an 8-Queens solution would look like:


. Q . . . . . .

. . . . Q . . .

. . Q . . . . .

Q . . . . . . .

. . . . . Q . .

. . . Q . . . .

. . . . . . Q .

. . . . . . . Q


Installation
Clone the repository to your local machine:
git clone https://github.com/yourusername/n-queens-solvers.git

Requirements

Python 3.x

No additional libraries are required except the built-in random and time modules.

License

This project is licensed under the MIT License.

