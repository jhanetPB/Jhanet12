#ESTUDIANTE: JHANET PARRAGA BLANCO
print("SEGUNDO  EJERCICIO")
print("=======================================================")
import math
A,B,C= map(int, input().split())
if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con numeros complejos")
else:
  x1 = (-B+math.sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-math.sqrt(B**2-(4*A*C)))/(2*A)
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)