colonia1 = 4
colonia2 = 10
dias = 0

while colonia1 < colonia2:
    colonia1 = colonia1 * 1.03
    colonia2 = colonia2 * 1.015
    dias += 1

print(f"A colônia A terá {colonia1:.2f}")
print(f"A colônia B terá {colonia2:.2f}")
print(f"Levará {dias} dias para A ultrapassar ou igualar B")