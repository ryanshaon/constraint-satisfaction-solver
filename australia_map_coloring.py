"""Australia map coloring solved with CSP backtracking."""

STATES = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
COLORS = ["Red", "Green", "Blue"]
NEIGHBORS = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": [],
}


def is_valid(state, color, assignment):
    """Return True if coloring `state` with `color` violates no constraints."""
    for neighbor in NEIGHBORS[state]:
        if assignment.get(neighbor) == color:
            return False
    return True


def choose_unassigned_state(assignment):
    """Pick the next state that does not yet have a color."""
    for state in STATES:
        if state not in assignment:
            return state
    return None


def backtrack(assignment):
    if len(assignment) == len(STATES):
        return dict(assignment)

    state = choose_unassigned_state(assignment)
    if state is None:
        return None

    for color in COLORS:
        if not is_valid(state, color, assignment):
            continue

        assignment[state] = color
        result = backtrack(assignment)
        if result:
            return result
        del assignment[state]

    return None


def main():
    solution = backtrack({})

    if solution:
        print("Solution:")
        for state in solution:
            print(state, "=", solution[state])
    else:
        print("No solution found")


if __name__ == "__main__":
    main()
