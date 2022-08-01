import uuid
import mysql.connector
from colorama import Cursor
import PokemonGoBDD
import urllib.request

#GL4mhMnebpPz

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
    externalip = urllib.request.urlopen("https://ident.me").read().decode("utf8")
    conexio = False
    while(conexio == False):
        clauUsuari = input("Dime tu clave: ")
        for x in claus: 
            if (x[2] == clauUsuari):
                sql2 = "SELECT * FROM claus WHERE clau = %s"
                cursor.execute(sql2,(clauUsuari,)) 
                resultatSQL2 = cursor.fetchone()
                id_usuari = resultatSQL2[1]
                if(str(id_usuari) == "None"):
                    sql3 = "insert into usuaris(Mac,ipUsuari) VALUES (%s,%s);"
                    cursor.execute(sql3,(mac,externalip))
                    conexion.commit()
                    sql4 = "SELECT * FROM usuaris WHERE Mac = %s;"
                    cursor.execute(sql4,(mac,))
                    select = cursor.fetchone()
                    id_usuari_select = select[0]
                    sql5 = "UPDATE claus SET id_usuaris = %s WHERE clau = %s;"
                    cursor.execute(sql5,(id_usuari_select,clauUsuari))
                    conexion.commit()
                    print("Bienvenido nuevo usuario!!")
                    print("iniciando Bot")
                    conexio = True
                if(str(id_usuari) != "None"):   
                    sql6 = "SELECT * from usuaris where Mac = %s" 
                    cursor.execute(sql6,(mac,))
                    select = cursor.fetchone()
                    id_usuari_select = select[0]
                    sql7 = "SELECT * from claus where clau = %s" 
                    cursor.execute(sql7,(clauUsuari,))
                    select2 = cursor.fetchone()
                    id_usuari_select2 = select2[1]
                    if (id_usuari_select == id_usuari_select2):
                        print("Bienvenido, iniciando el bot...")
                        conexio = True
                    else:
                        print("Esta llave se ha utilizado en otro dispositivo!!")  
                        print("Puedes enviar un mensaje a los moderadores y se te proporcionara otra.")                    

        if (conexio == True):
            contador = 0
            while True:
                contador = contador + 1
                PokemonGoBDD.sercarPokemons()
                if (contador > 59 and PokemonGoBDD.mirarSiEstasACamp() == False):
                    PokemonGoBDD.SalirDeTodo()
                    contador = 0
                if (contador > 59 and PokemonGoBDD.mirarSiEstasACamp() == True):
                    contador = 0    
        else:
            print("Llave incorrecta...")

                      

ComprovarUsuaris()