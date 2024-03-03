import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    bmi = []
    if len(height) != len(weight):
        print("Error: Lists don't have same number of items")
        return [0]
    for h, w in zip(height, weight):
        if isinstance(h, (int, float)) and isinstance(w, (int, float)):
            bmi.append(np.divide(w, np.square(h)))
        else:
            print("Error: Element is not an Int or Float")
            return [0]
    return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    applied_limits = []
    for b in bmi:
        if isinstance(b, (int, float)):
            applied_limits.append(b > limit)
        else:
            print("Error: Element is not an Int or Float")
            return []
    return applied_limits
