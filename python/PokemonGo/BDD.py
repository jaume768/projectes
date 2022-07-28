import uuid
import mysql.connector
from colorama import Cursor
import PokemonGoBDD

pokemonsAtrapats = 0
  
connection = {
    'host':'bctpwdzxwgkr5igzvgdp-mysql.services.clever-cloud.com',
    'user':'ulr6wsvhwvtiee7v',
    'password':'vZz0ZX8d8wCePDVrRhBe',
    'db':'bctpwdzxwgkr5igzvgdp'
}

conexion = mysql.connector.connect(**connection)
cursor = conexion.cursor()
print("Conexión con base de datos")

def ComprovarUsuaris():
    sql = 'SELECT * FROM claus;'
    cursor.execute(sql)
    claus = cursor.fetchall()
    mac =  (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
    for ele in range(0,8*6,8)][::-1]))
    conexio = False
    while(conexio == False):
        clauUsuari = input("Dime tu clave: ")
        for x in claus:
            if (x[1] == clauUsuari):
                sql2 = "SELECT * FROM claus WHERE clau = %s"
                cursor.execute(sql2,(clauUsuari,)) 
                resultatSQL2 = cursor.fetchone()
                ip = resultatSQL2[2]
                if(x[2] == mac):
                    print("iniciant")
                    conexio = True
                if(str(ip) == "None"):
                    sql2 = "UPDATE claus SET ipUsuari = %s WHERE clau = %s;"
                    cursor.execute(sql2,(mac,clauUsuari))
                    conexion.commit()
                    print("Bienvenido nuevo usuario!")
                    print("iniciando bot")
                    conexio = True
                if(x[2] != mac and str(ip) != "None"):
                    print("No es tu llave, compra otra")                    

        if (conexio == True):
            while True:
                PokemonGoBDD.sercarPokemons()
        else:
            print("Llave incorrecta...")

                      

ComprovarUsuaris()