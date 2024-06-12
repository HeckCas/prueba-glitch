from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# APIs son Interfaces (Intermediarios A -> B Cliente -> Servidor)

#APIs pueden hacer cualquier cosa que se pueda programar

#Endpoint -> URL de una API diversas operaciones

#URLBASE -> Raiz de la API, a través de esta construimos todos los endpoints

#swapi.tech/ -> URLBASE (tmbn es un endpoint)
#endpoints
#swapi.tech/people/1 -> Endpoints que hacían cosas
#swapi.tech/planets/5


# @nombre_del_decorador #Decorador -> Darle poderes extras a una funcion

# def hello_world():
#     return "Hello World!"  ✅ sintaxis correcta


# @nombre_del_decorador


# print()

# def hello_world():
#     return "Hello World!"  🚫 Mal para python



@app.route('/') # -> URLBASE Ej. swapi.tech   coingecko.com/api/v3/.....endpoint
def root():
  print('hola')
  return 'holiiii'



@app.route('/resta') #por default el metodo GET
def resta():
  x = 100
  y = 20
  print(x-y)
  return jsonify({
    "status_code": 200,
    "data": x-y,
    "message": "TODO OK"
  })


@app.route('/resta', methods=['POST']) # Puedo definirle a un mismo endpoint operaciones diferentes especificandsolas con el método ej: POST
def resta2():
  x = 78
  y = 20
  print(x-y)
  return jsonify({
    "status_code": 200,
    "data": x-y,
    "message": "TODO OK"
  })

@app.route('/suma')
def sum():
  x = 78
  y = 20
  print(x+y)
  return jsonify({
    "status_code": 200,
    "data": x+y,
    "message": "TODO OK"
  })



@app.route('/minus', methods=['POST'])
def minus():
  x = request.args.get('primer', type=float)
  y = request.args.get('segundo', type=float)
  print(x)
  print(y)
  if(x and y):
    return jsonify({
      "status_code": 200,
      "data": x-y,
      "message": "TODO OK"
    })
  else:
    response = jsonify({
      "status_code": 400,
      "data": "Tal vez falta un valor o no son numericos",
      "message": "ERROR"
    })
    response.status_code = 400
    return response


# Este endpoint es igualito/similar al que tendrían que entregar de proyecto
#Ej Swapi: http://swapi.tech/ruta/valor
#Ej Swapi: http://swapi.tech/planetas/9
  


#Ej Swapi: http://localhost:5000/mongo/0.263

#@app.route('/mongo', methods=['GET', 'POST'])
@app.route('/mongo/<value>', methods=['GET', 'POST'])
def mongo(value):
  print('value')
  print(value)
  val = float(value)
  client = MongoClient('mongodb+srv://holi:holi@cluster0.hnlgih4.mongodb.net/')
  # Apuntamos a la base de datos 'master-data'
  db = client['master-data']
  # Apuntamos a la colección 'spotify'
  coll = db['spotify']
  energy_gte = coll.find({"energy": {"$gte": val}}, {"energy": True, "name": True, '_id': False }).limit(6) # SELECT * FROM coll where energy >= 0.263 TOP 150 | LIMIT 150
  dataToReturn = list(energy_gte)
  return jsonify({
      "status_code": 200,
      "data": dataToReturn,
      "message": "Consulta BIEN"
    })

# Proyecto

# 1.- Recolectar Datos (Puede ser de: [Kaggle, JSONs, APIS, CSV, DB])
# 2.- Transformar [Estructura y limpieza (Tidy Data y DCleaning)] esos datos (Opcional) 95% de los casos si lo necesita 
# 3.- Subir los datos a mongo

# Pasos del API

# Construir endpoint que consulte a la BD de mongo
# Subir el API a PROD
# Hacer una micro documentacion de su endpoint

# LINK -> Entregable


# Levantar el servidor de nuestra web App
# localhost -> 127.0.0.1 | 0.0.0.0
# port = 3306, 80
app.run(debug=True, host='localhost', port=5000) # Solo va en local



# Esto va en prod

#if __name__ == "__main__":
#	app.run()









#ivancastelanapi.com
#Documentacion
#endpoint 1 se llama /resta reciobe 2 valores numericos y devuelve un valor numerico


