caracteres = ["a","b","c","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z",1,2,3,4,5,6,7,8,9,0]

import random

def generate_password():
    
    password = ""
    
    cantidad_vueltas = input(f"Ingrese la cantidad de caracteres que quiere que tenga su contraseña (Debe ser un numero menor o igual a {len(caracteres)}): \n")
    
    while cantidad_vueltas.isdigit():
    
        cantidad_vueltas = int(cantidad_vueltas)
    
        if cantidad_vueltas <= 35:
            
            for x in range(cantidad_vueltas) :
                        
                    caracter = random.choice(caracteres)
                    
                    caracter = str(caracter)
                    
                    password = password + caracter
                        
            return password
        
        else: print("Algo salió Mal")
            