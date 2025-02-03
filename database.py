from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI, DB_NAME

# Connect to MongoDB Atlas
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
users_collection = db["users"]
