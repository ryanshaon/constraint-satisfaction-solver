# AI Assignment: Constraint Satisfaction Problems (CSP)

## Overview

This project contains Python implementations of multiple problems modeled as **Constraint Satisfaction Problems (CSPs)**.
Each problem is solved using **backtracking search** with constraint checks.

---

## Bit 1: Map Coloring (Australia)

### Problem

Assign colors to Australian states so that no two adjacent states share the same color.

### Approach

- Variables: States
- Domain: `{Red, Green, Blue}`
- Constraints: Neighboring states must have different colors
- Method: Backtracking

---

## Bit 2: Telangana Map Coloring

### Problem

Assign colors to Telangana districts so that adjacent districts do not share the same color.

### Approach

- Variables: Districts
- Domain: `{Red, Green, Blue}`
- Constraints: Adjacent districts must have different colors
- Method: Backtracking

### Visualization

- Built using **NetworkX** and **Matplotlib**
- Districts are graph nodes
- Adjacency is represented with edges
- Final color assignment is displayed visually

---

## Bit 3: Sudoku Solver

### Problem

Solve a `9x9` Sudoku puzzle.

### CSP Formulation

- Variables: Every cell in the grid
- Domain: `{1-9}`
- Constraints:
- No repeated value in a row
- No repeated value in a column
- No repeated value in a `3x3` subgrid

### Approach

- Backtracking search over empty cells
- Constraint checks at each placement

---

## Bit 4: Cryptarithmetic (SEND + MORE = MONEY)

### Problem

Assign digits to letters such that:

`SEND + MORE = MONEY`

### CSP Formulation

- Variables: `S, E, N, D, M, O, R, Y`
- Domain: `{0-9}`
- Constraints:
- All letters map to unique digits
- No leading zero (`S != 0`, `M != 0`)
- The equation must hold exactly

### Approach

- Backtracking assignment of digits to letters
- Constraint checks on partial and complete assignments

---

## Concepts Used

- Constraint Satisfaction Problems (CSP)
- Backtracking Algorithm
- Constraint Checking
- Recursion
- Graph Representation (for visualization)

---

## Project Files

- `australia_map_coloring.py`
- `telangana_map_coloring.py`
- `sudokupuzzle.py`
- `cryptarithmetic_backtracking.py`

---

## How to Run

Run each script with Python:

```bash
python australia_map_coloring.py
python sudokupuzzle.py
python cryptarithmetic_backtracking.py
python telangana_map_coloring.py
```

### Optional dependencies (required only for Telangana visualization)

```bash
pip install networkx matplotlib
```

---

## Conclusion

These examples show how map coloring, Sudoku, and cryptarithmetic can be modeled and solved as CSPs using backtracking.