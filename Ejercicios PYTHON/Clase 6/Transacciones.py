import psycopg2 as bd

conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    conexion.autocommit= False
    cursor= conexion.cursor()
    sentencia= 'INSERT INTO persona(nombre, apellido, email)VALUES(%s, %s, %s)'
    valores= ('Maria', 'Esperanza', 'mesparza@gmail.com')
    cursor.execute(sentencia, valores)
    conexion.commit() # Hacemos el commit manualmente.
    print('Termina la transaccion.')

except Exception as e:
    conexion.rollback()
    print(f'ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()

