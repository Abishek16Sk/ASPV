from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb+srv://ASPV:ASPV@aspv.lxffi.mongodb.net/?retryWrites=true&w=majority&appName=ASPV")
db = client['ASPV']
collection = db['products'] 

try:
    
    print("Connected to MongoDB.")
    print(f"Database: {db.name}")
    print(f"Collection: {collection.name}")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

@app.route('/api/products', methods=['GET'])
def get_products():
    try:
       
        products = list(collection.find({}, {'_id': 0}))  
        
        
        print(f"Fetched {len(products)} products.")
        
       
        if not products:
            print("No products found in the database.")
        return jsonify(products)
    except Exception as e:
        print(f"Error fetching products: {e}")
        return jsonify({"error": "Failed to fetch products"}), 500

if __name__ == '__main__':
    app.run(port=5000)
