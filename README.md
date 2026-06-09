# Constraint Satisfaction Solver

A Python project that models and solves classic Artificial Intelligence problems using Constraint Satisfaction Problem techniques and backtracking search.

## Overview

This repository demonstrates how structured problems can be represented using variables, domains, and constraints. Each solver uses backtracking with constraint checks to search for valid solutions.

Projects included:

- Australia map coloring
- Telangana map coloring
- Sudoku solver
- Cryptarithmetic solver

## Project 1: Australia Map Coloring

Assigns colors to Australian states so that no two adjacent states share the same color.

Approach:

- Variables: states
- Domain: Red, Green, Blue
- Constraint: neighboring states must have different colors
- Method: backtracking search

## Project 2: Telangana Map Coloring

Assigns colors to Telangana districts while respecting adjacency constraints.

Features:

- Districts represented as graph nodes
- Adjacency represented using graph edges
- Visualization built with NetworkX and Matplotlib
- Final color assignment displayed visually

## Project 3: Sudoku Solver

Solves a 9x9 Sudoku puzzle using CSP modeling.

Constraints:

- No repeated value in a row
- No repeated value in a column
- No repeated value in a 3x3 subgrid

## Project 4: Cryptarithmetic Solver

Solves the classic SEND + MORE = MONEY puzzle by assigning digits to letters.

Constraints:

- Each letter maps to a unique digit
- Leading letters cannot be zero
- The equation must hold exactly

## Concepts Used

- Constraint Satisfaction Problems
- Backtracking search
- Constraint checking
- Recursion
- Graph representation
- Visualization with NetworkX and Matplotlib

## Project Files

- australia_map_coloring.py
- telangana_map_coloring.py
- sudokupuzzle.py
- cryptarithmetic_backtracking.py

## How to Run

Run each script with Python:

```bash
python australia_map_coloring.py
python sudokupuzzle.py
python cryptarithmetic_backtracking.py
python telangana_map_coloring.py
```

Optional dependencies for visualization:

```bash
pip install networkx matplotlib
```

## What I Learned

Through this project, I practiced:

- Modeling problems as CSPs
- Designing variables, domains, and constraints
- Implementing recursive backtracking
- Solving puzzle and graph-based AI problems
- Visualizing graph coloring solutions

## Future Improvements

- Add MRV heuristic
- Add Degree heuristic
- Add Forward Checking
- Add AC-3 constraint propagation
- Add performance comparisons between solving methods
