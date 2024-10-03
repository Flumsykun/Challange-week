# utils.py
def clamp(value, min_value, max_value):
    """Clamps a value between a minimum and maximum."""
    return max(min_value, min(value, max_value))
