
---

### README.md

# 8-Puzzle Solver with Heuristic Functions

This project implements a solution to the 8-puzzle problem using different heuristic functions in Python. The puzzle involves a 3x3 grid where one tile is empty (represented by 0), and the goal is to arrange the tiles in a specific order by sliding them into the empty space.

### Features:
- Implements the **Misplaced Tiles** heuristic for solving the 8-puzzle.
- Uses a **search-based approach** to explore possible moves and solve the puzzle.
- Provides step-by-step output to show the progression towards the goal state.

### Heuristic Functions Used:
- **Misplaced Tiles**: Counts the number of tiles that are not in their goal positions.
- **Manhattan Distance**: (Currently not implemented but can be added easily) Measures the sum of the absolute differences between the current position and the goal position for each tile.
- **Euclidean Distance**: (Currently not implemented but can be added easily) Uses Pythagoras' theorem to calculate the straight-line distance between current and goal positions of each tile.

### How to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/8-puzzle-solver.git
   ```

2. Navigate to the project directory:
   ```bash
   cd 8-puzzle-solver
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the puzzle solver script:
   ```bash
   python solve_puzzle.py
   ```

### Sample Output:
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

### Additional Notes:
- The project can be extended with additional heuristics such as **Manhattan Distance** and **Euclidean Distance**.
- The script currently searches up to 1000 steps; you can modify this limit based on your needs.

---

### requirements.txt

```
numpy==1.23.5
```

*Note: You can add other dependencies as needed based on your implementation (like libraries for advanced heuristics).*

---

