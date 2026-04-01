"""Cryptarithmetic solver for SEND + MORE = MONEY using backtracking."""

LETTERS = ["S", "E", "N", "D", "M", "O", "R", "Y"]


def to_number(word, assignment):
    value = 0
    for char in word:
        value = value * 10 + assignment[char]
    return value


def is_valid_partial(assignment):
    """Check constraints that can be validated for the current assignment."""
    if assignment.get("S") == 0:
        return False
    if assignment.get("M") == 0:
        return False

    if len(assignment) == len(LETTERS):
        send = to_number("SEND", assignment)
        more = to_number("MORE", assignment)
        money = to_number("MONEY", assignment)
        return send + more == money

    return True


def backtrack(index, assignment, used_digits):
    if index == len(LETTERS):
        return dict(assignment)

    letter = LETTERS[index]

    for digit in range(10):
        if digit in used_digits:
            continue

        assignment[letter] = digit
        if is_valid_partial(assignment):
            result = backtrack(index + 1, assignment, used_digits | {digit})
            if result:
                return result

        del assignment[letter]

    return None


def main():
    result = backtrack(0, {}, set())

    print("\nSolution:\n")

    send = to_number("SEND", result)
    more = to_number("MORE", result)
    money = to_number("MONEY", result)

    print("SEND  =", send)
    print("MORE  =", more)
    print("MONEY =", money)

    print("\nLetter Mapping:")
    for letter in sorted(result):
        print(f"{letter} = {result[letter]}")


if __name__ == "__main__":
    main()