
ListaNombres = []

for i in range(0,3,1):
    ListaNombres.append(input("Escriba un nombre: "))

print(f"El nombre más largo es ", max(ListaNombres, key = len))
print(f"El nombre más pequeño es ", min(ListaNombres, key = len))




