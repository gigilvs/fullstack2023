from Password import *

while True:
        
        try:
    
            entrada = int(input("1.Admin\n2.Usuario\nSu eleccion ==> "))
            
            contador = 0
            
            intentos = 3
            
            if entrada > 0 and entrada < 3 :
                
                while contador < 3:
                    
                        print("======================================")
                        user = input("Ingrese su Usuario: \n")
                        password = input("Ingrese su Contraseña: \n")
                        print("======================================")
                    
                        if entrada == 1 and user in admin_ok and password == admin_ok[user]:
                                from Admin import admin_ok
                                print("======================================")
                                print("Ingreso Existoso")
                                print("======================================")
                                break
                
                        elif entrada == 2 and user in user_ok and password == user_ok[user]:
                                from User import user_ok
                                print("======================================")
                                print("Ingreso Existoso")
                                print("======================================")
                                break


                        else:
                            contador += 1
                            print("======================================")
                            print("Datos Incorrectos.. Intente nuevamente")
                            print("======================================")
                            print(f'Le quedan {intentos-contador} Intentos')
                            print("======================================")
                                 

            if contador == 3:
                        print("======================================")
                        print("CUENTA BLOQUEADA")
                        print("======================================")
                        exit()              
       
        except ValueError as e:
            #MANEJO DE ERROR PARA DEPURAR HABILITAR DE SER NECESARIO
            #print("Error: ",e)
            entrada = 0
            print("===============================================================")
            print("Ingrese una opcion correcta\nIngrese 1 o 2 Y solo numeros por favor!!!")
            print("===============================================================")
        #except NameError as ea:
            #MANEJO DE ERROR PARA DEPURAR HABILITAR DE SER NECESARIO
            #print("Error: ",ea)
            #entrada = 0
            #print("===============================================================")
            #print("Ingrese una opcion correcta\nIngrese 1 o 2 por favor!!!")
            #print("===============================================================")
          