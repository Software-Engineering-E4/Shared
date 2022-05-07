def hamming_distance(left: str, right: str) -> int:
    return sum(i != j for i, j in zip(left, right)) + abs(len(left) - len(right))
