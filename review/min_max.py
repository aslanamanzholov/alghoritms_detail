def min_max(a, b):
    if a < b:
        a, b = b, a
    if a > b:
        b, a = a, b
    return {"min": a, "max": b}


print(min_max(12, 12))

a = list(range(100))

print(min(a))
print(max(a))
