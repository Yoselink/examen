def ValidaNum(num):
    if len(num) < 5:
        return 'Debe contener al menos 5 numeros'
    elif not num.isalnum():
        return 'Debe contener numeros solamente'
    else:
        return True
    
num = raw_input('Ingrese numeros: ')
print ValidaNum(num)
