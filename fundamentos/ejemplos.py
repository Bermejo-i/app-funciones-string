
def mayusculaMinuscula(valor):
    print(valor.upper())
    print(valor.lower())
    print(valor.capitalize())
    print(len(valor))

def longMensaje(valor):
    print("la longitud del string es: ", len(valor))

def convertNum2str(valor):
    print(str(valor))

def arregloPalabras(valor):
    print(valor.split())

def array2str():
    nombres = ["Luis","Angel","Maria","Angelica"]
    print("".join(nombres))

def OtrasFx(valor):
    print(valor.replace("Python","Isra"))
    print(valor.find("mundo"))
    print(valor.count("Python"))
    print(valor.endswith("Python"))
