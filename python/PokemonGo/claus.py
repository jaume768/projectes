import mysql.connector
from colorama import Cursor
import string
import random

connection = {
    'host':'bctpwdzxwgkr5igzvgdp-mysql.services.clever-cloud.com',
    'user':'ulr6wsvhwvtiee7v',
    'password':'vZz0ZX8d8wCePDVrRhBe',
    'db':'bctpwdzxwgkr5igzvgdp'
}

conexion = mysql.connector.connect(**connection)
cursor = conexion.cursor()
print("Conexión con base de datos")


number_of_strings = 20
length_of_string = 12

for x in range(number_of_strings):
    paraula = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
    sql = "insert into claus(clau,premium,enviada) VALUES (%s,FALSE,TRUE);"
    cursor.execute(sql,(paraula,))
    conexion.commit()
    print(x)