#!/usr/bin/python

import os
import sys
import platform

class main:
    
    sistemaOperativo = ""
    
    #Limpiamos pantalla
    if sys.platform.startswith("win"):
        os.system("cls")
        sistemaOperativo = "win"
    else:
        os.system("clear")
        sistemaOperativo = "other"
        
    print('''                                         
 _____                                   
|  _  |___ ___ ___ ___ ___ _____ ___ ___ 
|   __|  _| . | . |  _| .'|     | .'|  _|
|__|  |_| |___|_  |_| |__,|_|_|_|__,|_|  
              |___|                      
                                         
 _____                   _               
|  _  |___ ___ ___ ___ _| |___           
|     | . | .'| . | .'| . | . |          
|__|__|  _|__,|_  |__,|___|___|          
      |_|     |___|                      
      By: NeXxeZ \n\n''')
    
    print("Plataforma: " + platform.system() + "\n")
    
    if sistemaOperativo == "win":
        while True:
            print("1. Apagar sistema en X horas.")
            print("2. Cancelar apagado programado.")
            print("3. Salir")
            so = int(input())
            if so == 1:
                hora = input("Apagar sistema en X horas... \n")
                hora = hora * 3600
                os.system("shutdown -s -t " + str(hora))
            elif so == 2:
                os.system("shutdown -a")
            elif so == 3:
                sys.exit("Saliendo...")
            else:
                pass
            
    elif sistemaOperativo == "other":
        while True:
            print("1. Apagar sistema en X horas.")
            print("2. Cancelar apagado programado.")
            print("3. Salir")
            so = int(input())
            if so == 1:
                hora = input("Apagar sistema en X horas... \n")
                hora = hora * 60
                os.system("sudo shutdown -h " + str(hora))
            elif so == 2:
                os.system("sudo shutdown -c")
            elif so == 3:
                sys.exit("Saliendo...")
            else:
                pass
                
    else:
        print("No hemos encontrado tu sistema operativo.")
        