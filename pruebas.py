#encoding:UTF-8
from database import *
import requests
from _mysql_exceptions import IntegrityError
from random import randint

if __name__ == '__main__':
    db = conectar_db()
    cursor = db.cursor()
    cursor.execute("show tables")
    print cursor.fetchall():
    db.close()

def pruebas():
    db = conectar_db()

    url_base = "http://127.0.0.1:5000"
    # url_base = "http://172.18.2.2:3306"

    

    print "========================================================="
    print "PRUEBA 3: Comprobar token (Unitaria)"
    print "========================================================="

    print "Comprobar token: PRUEBA 3.1 (Llamada correcta)"
    prueba_positiva = comprobar_token(db, "12345QWERTY")  # Prueba positiva
    print "Resultado Esperado: True"
    print "Resultado Obtenido: " + str(prueba_positiva)
    if str(prueba_positiva) == "True":
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"
    print "Comprobar token: PRUEBA 3.2 (Prueba negativa, no existe el token)"
    prueba_negativa1 = comprobar_token(db, "123")  # Prueba negativa, no existe el token
    print "Resultado Esperado: False"
    print "Resultado Obtenido: " + str(prueba_negativa1)
    if str(prueba_negativa1) == "False":
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"

    print "========================================================="
    print "PRUEBA 4: Get voto (Unitaria)"
    print "========================================================="

    print "Get voto: PRUEBA 4.1 (Llamada correcta)"
    prueba_positiva = get_voto(db, "1", "1") # Prueba positiva
    print "Resultado Esperado: Array con los datos de los votos realizados por el usuario a la votación dada"
    print "Resultado Obtenido: " + str(prueba_positiva)
    if str(prueba_positiva) == '<Response [404]>':
        print "---------------------------------------------------------"
        print "INCORRECTO"
    else:
        print "-------------------------------------------------------------"
        print "CORRECTO"

    print "---------------------------------------------------------"
    print "Get voto: PRUEBA 4.2 (No existe token)"
    prueba_negativa1 = get_voto(db, "123", "1") # Prueba negativa, no existe el token_usuario
    print "Resultado Esperado: Array vacío"
    print "Resultado Obtenido: " + str(prueba_negativa1)
    if str(prueba_negativa1) == '[]':
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"
    print "Get voto: PRUEBA 4.3 (No existe token_votacion)"
    prueba_negativa2 = get_voto(db, "1", "123")  # Prueba negativa, no existe el token_votacion
    print "Resultado Esperado: Array vacío"
    print "Resultado Obtenido: " + str(prueba_negativa2)
    if str(prueba_negativa2) == '[]':
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"

    # Pruebas para el metodo get_voto_pregunta

    print "========================================================="
    print "PRUEBA 5: Get voto pregunta (Unitaria)"
    print "========================================================="

    print "Get voto pregunta: PRUEBA 5.1 (Llamada correcta"
    prueba_positiva = get_voto_pregunta(db, "1", "1", "1")  # Prueba positiva
    print "Resultado esperado: Array con el voto realizado por el usuario para una pregunta de una votación dada"
    print "Resultado Obtenido: " + str(prueba_positiva)
    if str(prueba_positiva) == '[]':
        print "---------------------------------------------------------"
        print "INCORRECTO"
    else:
        print "---------------------------------------------------------"
        print "CORRECTO"

    print "---------------------------------------------------------"
    print "Get voto pregunta: PRUEBA 5.2 (No existe token_usuario)"
    prueba_negativa1 = get_voto_pregunta(db, "123", "1", "1")  # Prueba negativa, no existe el token_usuario
    print "Resultado esperado: Array vacío"
    print "Resultado Obtenido: " + str(prueba_negativa1)
    if str(prueba_negativa1) == '[]':
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"
    print "Get voto pregunta: PRUEBA 5.3 (No existe token_votacion)"
    prueba_negativa2 = get_voto_pregunta(db, "1", "123", "1")  # Prueba negativa, no existe el token_votacion
    print "Resultado esperado: Array vacío"
    print "Resultado Obtenido: " + str(prueba_negativa2)
    if str(prueba_negativa2) == '[]':
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"
    print "Get voto pregunta: PRUEBA 5.4 (Prueba negativa, no existe el token_pregunta)"
    prueba_negativa3 = get_voto_pregunta(db, "1", "1", "123")  # Prueba negativa, no existe el token_pregunta
    print "Resultado esperado: Array vacío"
    print "Resultado Obtenido: " + str(prueba_negativa3)
    if str(prueba_negativa3) == '[]':
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"

    

    print "========================================================="
    print "PRUEBA 8: Consultar voto pregunta (Unitaria)"
    print "========================================================="

    print "Consultar voto pregunta: PRUEBA 8.1 (Llamada correcta)"
    prueba_positiva = consultar_votos_pregunta(db, "1", "1")  # Prueba positiva
    print "Resultado Esperado: Array con los datos de los votos realizados por el usuario con votación de token=1 y pregunta de token=1"
    print "Resultado Obtenido: " + str(prueba_positiva)
    if str(prueba_positiva) == '<Response [404]>':
        print "---------------------------------------------------------"
        print "INCORRECTO"
    else:
        print "-------------------------------------------------------------"
        print "CORRECTO" 

    print "-------------------------------------------------------------"
    print "Consultar voto pregunta: PRUEBA 8.2 (Respuesta vacía)"
    prueba_negativa = consultar_votos_pregunta(db, "123", "1")  # Error, no existe el token
    print "Resultado Esperado: Array Vacío"
    print "Resultado Obtenido" + str(prueba_negativa)
    if str(prueba_negativa) == '[]':
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"
    
    print "---------------------------------------------------------"

    print "========================================================="
    print "PRUEBA 9: Guardar voto (Unitaria)"
    print "========================================================="
    
    print "Guardar voto: PRUEBA 9.1 (Llamada correcta)"
    print "Resultado Esperado: None"
    try:
        prueba_positiva = guardar_voto(db,"8", "1", "6", "3")  # Prueba positiva
    except IntegrityError:
        print "Resultado Obtenido: " + str(prueba_positiva)
        print "---------------------------------------------------------"
        print "La llamada está bien pero ese voto ya existe y no se puede duplicar"
    else:
        print "Resultado Obtenido: " + str(prueba_positiva)
        if str(prueba_positiva) == "None":
            print "---------------------------------------------------------"
            print "CORRECTO"
        else:
            print "---------------------------------------------------------"
            print "INCORRECTO"

    print "---------------------------------------------------------"
    print "Guardar voto: PRUEBA 9.2 (Respuesta vacía)"
    print "Resultado Esperado: Array vacío (no se puede guardar porque ya existe el token)"
    try:
        prueba_negativa = guardar_voto(db, "1", "1", "1", "1")  # Error, ya existe el token
    except IntegrityError:
        print "Resultado Obtenido: " + str(prueba_negativa)
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"

    desconectar_db(db)
    

