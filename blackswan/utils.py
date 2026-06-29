def tier_from_score(score: int) -> str:
    if score >= 9000:
        return "A"
    elif score >= 8000:
        return "B"
    elif score >= 7000:
        return "C"
    elif score >= 6000:
        return "D"
    else:
        return "E"