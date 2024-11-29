import pymongo
from pymongo import MongoClient


MONGO_URI = "mongodb+srv://ASPV:ASPV@aspv.lxffi.mongodb.net/?retryWrites=true&w=majority&appName=ASPV"

try:
    client = MongoClient(MONGO_URI)
    print("Connected to MongoDB successfully!")
except pymongo.errors.ConnectionError as e:
    print("Error connecting to MongoDB:", e)
    exit()


db = client["ASPV"]

products = [
   
    {
        "name": "Basmati Rice",
        "category": "FMCG",
        "sub_category": "Rice",
        "description": "Premium Basmati rice, long-grain, aromatic.",
        "image_url": "https://drive.google.com/uc?export=view&id=1aRci7joOcx7BQM9ugfdtHvB3yT0BK-6d",
        "price": 60.00,
        "quantity": "1 kg"
    },
    {
        "name": "White Rice",
        "category": "FMCG",
        "sub_category": "Rice",
        "description": "High-quality white rice for daily use.",
        "image_url": "https://drive.google.com/uc?export=view&id=1fj9PVlsGrrmXwKMu_1xvNmN3jy1VLJmx",
        "price": 40.00,
        "quantity": "1 kg"
    },
    {
        "name": "Ponni Rice",
        "category": "FMCG",
        "sub_category": "Rice",
        "description": "Popular Ponni rice variety, medium-grain.",
        "image_url": "https://drive.google.com/uc?export=view&id=1VC-Rp7x6CyThv90gd-9USou7VelKs0FF",
        "price": 45.00,
        "quantity": "1 kg"
    },
    {
        "name": "Matta Rice",
        "category": "FMCG",
        "sub_category": "Rice",
        "description": "Organic Kerala red rice, known for its health benefits.",
        "image_url": "https://drive.google.com/uc?export=view&id=1vCHBSDf2H6zKH8OvWO6JZiX-4YmWfmuz",
        "price": 50.00,
        "quantity": "1 kg"
    },
  

    {
        "name": "White Sugar",
        "category": "FMCG",
        "sub_category": "Sugar",
        "description": "Refined white sugar, perfect for cooking and beverages.",
        "image_url": "https://drive.google.com/uc?export=view&id=12UivM5sPQ4kRWl5FSTV_iaa9UCYM0CE1",
        "price": 30.00,
        "quantity": "1 kg"
    },
    {
        "name": "Brown Sugar",
        "category": "FMCG",
        "sub_category": "Sugar",
        "description": "Natural brown sugar with a rich, molasses flavor.",
        "image_url": "https://drive.google.com/uc?export=view&id=1Y2DsjCxKYc7gAIcginzl0pcjr2BZtiwj",
        "price": 35.00,
        "quantity": "1 kg"
    },

  
    {
        "name": "Sunflower Oil",
        "category": "FMCG",
        "sub_category": "Oil",
        "description": "Refined sunflower oil, ideal for cooking and frying.",
        "image_url": "https://drive.google.com/uc?export=view&id=19liWFPhSUqyUsg-3QzzTkKQW2TMYM4bC",
        "price": 120.00,
        "quantity": "1 liter"
    },
    {
        "name": "Gingerly Oil",
        "category": "FMCG",
        "sub_category": "Oil",
        "description": "Cold-pressed gingerly oil, perfect for traditional cooking.",
        "image_url": "https://drive.google.com/uc?export=view&id=1waPGKfnTKRA1EJVOa-o3wCFDU1xiMDxC",
        "price": 150.00,
        "quantity": "1 liter"
    },
    {
        "name": "Palmolein Oil",
        "category": "FMCG",
        "sub_category": "Oil",
        "description": "Refined palmolein oil for everyday cooking.",
        "image_url": "https://drive.google.com/uc?export=view&id=1ep7QekPSplBccPD7h9XEUJcZdu_aoam4",
        "price": 100.00,
        "quantity": "1 liter"
    },
    {
        "name": "Coconut Oil",
        "category": "FMCG",
        "sub_category": "Oil",
        "description": "Pure coconut oil, known for its multiple uses in cooking and skincare.",
        "image_url": "https://drive.google.com/uc?export=view&id=1tKaAFvAtI0OEneD-7mGfPXMzf05dZLrR",
        "price": 140.00,
        "quantity": "1 liter"
    },
    {
        "name": "Groundnut Oil",
        "category": "FMCG",
        "sub_category": "Oil",
        "description": "Pure groundnut oil, ideal for deep frying and cooking.",
        "image_url": "https://drive.google.com/uc?export=view&id=1vYex8L4ldHyou9QatGK8NadSVbGsk0rp",
        "price": 110.00,
        "quantity": "1 liter"
    },

   
    {
        "name": "Toor Dal",
        "category": "FMCG",
        "sub_category": "Pulses",
        "description": "Premium toor dal, rich in protein and ideal for making dal fry.",
        "image_url": "https://drive.google.com/uc?export=view&id=1NK4zeR4XOVmmSxL43Q3-mx1vNiHTlw0a",
        "price": 90.00,
        "quantity": "1 kg"
    },
    {
        "name": "Urad Dal",
        "category": "FMCG",
        "sub_category": "Pulses",
        "description": "High-quality urad dal, perfect for dals and making vadas.",
        "image_url": "https://drive.google.com/uc?export=view&id=1xExJCX-1H3ACDxL4xYWxj44c32TyAeUi",
        "price": 80.00,
        "quantity": "1 kg"
    },
    {
        "name": "Chana Dal",
        "category": "FMCG",
        "sub_category": "Pulses",
        "description": "Chana dal, known for its rich taste and nutritional value.",
        "image_url": "https://drive.google.com/uc?export=view&id=1H5qfWEf5CiGyJRRl5fm6KXeYkFzfVcX4",
        "price": 70.00,
        "quantity": "1 kg"
    },
    {
        "name": "Moong Dal",
        "category": "FMCG",
        "sub_category": "Pulses",
        "description": "Moong dal, light and nutritious, used in a variety of dishes.",
        "image_url": "https://drive.google.com/uc?export=view&id=1Fdeo0k233sew26ebhBZ0LZRptYHSLfiw",
        "price": 75.00,
        "quantity": "1 kg"
    },

    
    {
        "name": "Crystal Salt",
        "category": "FMCG",
        "sub_category": "Salt",
        "description": "Pure crystal salt, ideal for cooking and seasoning.",
        "image_url": "https://drive.google.com/uc?export=view&id=1fdgkli_oU0osUztcx5rbQo49FsXQ-J3j",
        "price": 20.00,
        "quantity": "500 gm"
    },
    {
        "name": "Powdered Salt",
        "category": "FMCG",
        "sub_category": "Salt",
        "description": "Finely powdered salt for use in all types of recipes.",
        "image_url": "https://drive.google.com/uc?export=view&id=1fdgkli_oU0osUztcx5rbQo49FsXQ-J3j",
        "price": 25.00,
        "quantity": "500 gm"
    }
]

try:
    
    product_collection = db["products"]
    
   
    product_collection.insert_many(products)
    print("Data inserted successfully!")
except pymongo.errors.PyMongoError as e:
    print("Error inserting data:", e)