def categorize_by_age(age):
    if age >= 120:
        return f"csal: {age}"
    elif age >= 90:
        return "DédSzülő"
    elif age >= 65:
        return "Nyugdíjas"
    elif age >= 18:
        return "Felnőtt"
    else:
        return "Gyerek"
