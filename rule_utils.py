

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""

    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100

    # Fallback to default game range
    return 1, 100