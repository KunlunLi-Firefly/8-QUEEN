#!/usr/bin/env python
# coding: utf-8

# In[4]:


def print_board(board):
    for row in board:
        print(" ".join(["Q" if col else "." for col in row]))

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nq_util(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_nq_util(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_nq_util(board, 0, n):
        print("Solution does not exist")
        return False
    print_board(board)
    return True

solve_n_queens(8)


# In[11]:


def print_solution(solution):
    n = len(solution)
    for row in range(n):
        line = ""
        for col in range(n):
            if col == solution[row]:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")


# In[10]:


def hill_climbing(n=8):
    def get_conflicts(queens):
        conflicts = 0
        for i in range(n):
            for j in range(i+1, n):
                if queens[i] == queens[j] or abs(queens[i] - queens[j]) == j - i:
                    conflicts += 1
        return conflicts

    def get_best_move(queens):
        moves = {}
        current_conflicts = get_conflicts(queens)
        for col in range(n):
            best_move = queens[col]
            for row in range(n):
                if queens[col] == row:
                    continue
                queens_copy = list(queens)
                queens_copy[col] = row
                moves[(col, row)] = get_conflicts(queens_copy)
            min_conflicts = min(moves.values())
            if min_conflicts < current_conflicts:
                best_moves = [move for move, conflicts in moves.items() if conflicts == min_conflicts]
                return random.choice(best_moves)
        return None

    queens = list(range(n))
    random.shuffle(queens)
    while True:
        best_move = get_best_move(queens)
        if best_move is None:
            break
        queens[best_move[0]] = best_move[1]
    
    if get_conflicts(queens) == 0:
        return queens
    else:
        return hill_climbing(n)  # Restart if not solved


def print_solution(solution):
    n = len(solution)
    for row in solution:
        print(' '.join('Q' if col == row else '.' for col in range(n)))


solution = hill_climbing(8)
print_solution(solution)


# In[9]:


import random

def min_conflicts(max_steps, n=8):
    def conflicts(state, row, col):
        return sum(state[col] == row or
                   state[col] - col == row - i or
                   state[col] + col == row + i
                   for i in range(n))

    board = [random.randrange(n) for _ in range(n)]
    for _ in range(max_steps):
        conflicts_list = [conflicts(board, board[col], col) for col in range(n)]
        if sum(conflicts_list) == 0:
            return board
        col = conflicts_list.index(max(conflicts_list))
        vals = [conflicts(board, row, col) for row in range(n)]
        board[col] = vals.index(min(vals))
    return board


print(min_conflicts(1000, 8))
final_solution = simulated_annealing(8)
print_solution(final_solution)


# In[8]:


import random, math

def initial_solution(n=8):
    return list(random.sample(range(n), n))

def get_cost(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def simulated_annealing(n=8):
    current_solution = initial_solution(n)
    current_cost = get_cost(current_solution)
    T = 1.0
    T_min = 0.00001
    alpha = 0.99
    while T > T_min:
        i, j = random.sample(range(n), 2)
        new_solution = current_solution[:]
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        new_cost = get_cost(new_solution)
        delta = new_cost - current_cost
        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / T):
            current_solution, current_cost = new_solution, new_cost
        T = T*alpha
    return current_solution


print(simulated_annealing(8))
final_solution = simulated_annealing(8)
print_solution(final_solution)


# In[41]:


import time

def measure_performance(algorithm, *args, **kwargs):
    start_time = time.time()
    result = algorithm(*args, **kwargs)
    end_time = time.time()
    print(f"{algorithm.__name__}: Execution time = {end_time - start_time} seconds")
    if isinstance(result, list):  # Assuming a solution is a list
        print_solution(result)
    return result

# Example usage
n_queens = 8
print("Backtracking Solution:")
measure_performance(solve_n_queens, n_queens)
print("\nSimulated Annealing Solution:")
measure_performance(simulated_annealing, n_queens)
print("\nMin-Conflicts Solution:")
measure_performance(min_conflicts, 1000, n_queens)
print("\nHill Climbing Solution:")
measure_performance(hill_climbing, n_queens)


# In[18]:


import time

def print_board(board):
    for row in board:
        print(" ".join(["Q" if col else "." for col in row]))

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nq_util(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_nq_util(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_nq_util(board, 0, n):
        print("Solution does not exist")
        return False
    print_board(board)
    return True

# Measure execution time only for backtracking
start_time = time.perf_counter()
solve_n_queens(8)
end_time = time.perf_counter()
print(f"Execution time: {end_time - start_time:.6f} seconds")


# In[ ]:




