def ValidaCaracter(letra):
    if len(letra) < 5:
        return 'La palabra debe contener minimo 5 letras'

    elif len(letra) > 8:
        return 'La palabra no debe contener mas de 8 letras'

    else: 
        return True
 
letra = raw_input('Ingrese una palabra: ')
print ValidaCaracter(letra)
    
    
