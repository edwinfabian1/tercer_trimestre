a = 5
b = 0
c = a/b
print(b/a)

try:
    a = 5
    b = 0
    c = a/b
    print(c)
except ZeroDivisionError:
    print("No se puede dividir por cero")