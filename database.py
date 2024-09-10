# ticket_booking/database.py

from pymongo import MongoClient

mongo_uri = "mongodb+srv://asdatabase:2006@cluster0.iqjfhv6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo_client = MongoClient(mongo_uri)
db = mongo_client['chatbot_to_db']
conversations_collection = db['chat_data']

def store_booking_data(email_address, adult_count, child_count, total_amount, booking_id):
    try:
        conversations_collection.insert_one({
            'email': email_address,
            'adult_count': adult_count,
            'child_count': child_count,
            'total_amount': total_amount,
            'booking_id': booking_id
        })
        print("Data successfully stored in MongoDB")
    except Exception as e:
        print(f"Error storing data in MongoDB: {e}")
