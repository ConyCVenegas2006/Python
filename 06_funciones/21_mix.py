#Constanza Concha
#28/04/2025

def funcion(a,b, *args, **kwargs):
    print("a=", a)
    print("b=", b)
    for arg in args:
        print("arg=", args)
    for key, value in kwargs.items():
        print(key,"=",value)

funcion(1,2,14,21,24,36,37,x="luis", y="sol", c="México")
