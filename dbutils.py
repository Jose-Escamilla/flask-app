from pymongo import MongoClient

MONGO_URI = ""

##client = MongoClient(MONGO_URI)

def db_connect(MONGO_URI, db_name,col_name):
	client = MongoClient(MONGO_URI) 
	database = client[db_name]
	collection = database[col_name]
	return collection

def db_insert_user(collection, user):
	return collection.insert_one(user)

def db_find_all(collection,query={}):
	return collection.find(query)


if __name__ == '__main__':
    print("MongoClient imported successfully!")

    # creams uan base de datos llamada mi_app:
    #database = client['mi_app']

    #creamos una colecciom llamada users:
    #users = database['users']

    # creamos usuario demo
    #usuario_demo = {
    #"user": "jose escamilla",
    #"email": "jose00escamilla@gmail.com"
    #}
    #users.insert_one(usuario_demo)