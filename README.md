
---

# 8-Puzzle Solver with Heuristic Functions

This Python project provides a solution to the **8-puzzle problem** using heuristic search techniques. The 8-puzzle involves a 3x3 grid where the objective is to move tiles (represented by numbers 1 to 8) into their correct positions, with one empty space (represented by 0) that allows the tiles to be slid around. The goal state is:

```
1 2 3
4 5 6
7 8 0
```

### Heuristic Functions Used:
1. **Misplaced Tiles**: The heuristic counts the number of tiles that are not in their correct goal positions. This heuristic is easy to compute but may not always lead to the most efficient solution.
2. **Manhattan Distance**: (Not implemented in the current version but can be added) Measures the sum of the absolute differences between the current position and the goal position of each tile.
3. **Euclidean Distance**: (Also can be added) Calculates the straight-line distance between the current and goal positions of each tile using the Pythagorean theorem.

### Features:
- **Misplaced Tiles Heuristic**: Computes the number of misplaced tiles by comparing the current state with the goal state.
- **Search Algorithm**: Uses a search-based algorithm to explore possible moves (up, down, left, right) from the initial state to the goal state.
- **Step-by-Step Output**: Displays each intermediate state in the puzzle as the search progresses toward the goal state.

### Implementation:
- **Goal State**: `[[1, 2, 3], [4, 5, 6], [7, 8, 0]]`
- **Possible Moves**: The possible movements are up, down, left, and right (denoted as coordinate shifts).
- **Search Process**: The algorithm generates new states by sliding the tiles into the empty space and evaluates them using the heuristic function.

### Example:
```python
# Initial state
initial_state = [[1, 2, 3], [4, 5, 0], [7, 8, 6]]

# Heuristic of initial state
print("Heuristic of initial_state:", heuristic(initial_state))

# Solving the puzzle
solution = solve_puzzle(initial_state)

# Displaying solution
if solution is not None:
    print("Solution:")
    for row in solution:
        print(row)
else:
    print("No solution exists.")
```

### How to Run the Code:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Bushra-Butt-17/8-Puzzle-Solver-with-Heuristic-Functions.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd 8-Puzzle-Solver-with-Heuristic-Functions
   ```

3. **Install required dependencies** (if any):
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the solver**:
   ```bash
   python heuristic_with_misplaced_tiles.py
   ```

### Expected Output:
```bash
Heuristic of initial_state: 3
STEPS:
--> [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
--> [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
--> [[1, 2, 3], [0, 4, 5], [7, 8, 6]]
--> [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
Solution:
[[1, 2, 3], [4, 5, 6], [7, 8, 0]]
```

### Future Improvements:
- Add the **Manhattan Distance** and **Euclidean Distance** heuristics for a more optimized approach to solving the puzzle.
- Implement a more sophisticated search algorithm (like A* or IDA*) to improve efficiency and scalability.

---

### requirements.txt

```
numpy==1.23.5
```


