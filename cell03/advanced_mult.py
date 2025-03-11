
i = 0
while i <= 10:
    j = 0
    row = ""
    while j <= 10:
        row += str(i * j) + " "
        j += 1
    print(f"Table de {i}: {row}")
    i += 1