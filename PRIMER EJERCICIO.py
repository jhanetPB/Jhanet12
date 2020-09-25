#ESTUDIANTE: JHANET PARRAGA BLANCO
print("PRIMER EJERCICIO")
print("=======================================")
x=int(input("ingrese un tiempo en segundos"))
h =x//3600
h1=x/3600 - h
m =int(h1*60)
m1 =h1*60 - m
s =round(m1*60)

print("la hora es",h)
print("los minutos son ",m)
print("los segundos son ",s)

z =int(input("tiempo que tomará en realizarse una tarea en segundos, minutos y horas"))

hz =z//3600
h1z=z/3600 - hz
mz =int(h1z*60)
m1z =h1z*60 - mz
sz =round(m1z*60)

print("los segundos son ",sz)
print("los minutos son ",mz)
print("la hora es",hz)


if x > z:
    print("alcanza el tiempo")
else:
    print("no alcanza el tiempo")
print("finalizo el programa")