from examen1 import ValidaCaracter
from examen2 import ValidaNum

letra = raw_input('Ingrese palabra: ') 
num = raw_input('Ingrese numeros: ')
if ValidaCaracter(letra) == True and ValidaNum(num) == True:
    print 'Ingreso exitoso de palabra y numeros exitoso'
else:
    print 'Ingreso NO exitoso'
