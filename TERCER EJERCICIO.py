#ESTUDIANTE: JHANET PARRAGA BLANCO
print("TERCER  EJERCICIO")
print("=======================================================")
a,b,c=map(int,input().split())
if (c<60 and b<60 and a<24):
    if (c < 59):
        c = c + 1
    elif (b < 59):
        b = b + 1
        c = 0
    elif (a < 23):
        a = a + 1
        b = 0
        c = 0
    else:
        a = 0
        b = 0
        c = 0
    print('%02d:' % (a), '%02d:' % b, '%02d' % c)
else:
    print("rango no permitido")