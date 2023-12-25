from motor.motor_asyncio import AsyncIOMotorClient


class MongoDB:
    def __init__(self, db_url: str):
        self.client = AsyncIOMotorClient(db_url)
        self.db = self.client.get_database()

    async def close_mongo_connection(self) -> None:
        self.client.close()

    async def get_data_by_key(self, collection_name: str, key_id: str) -> dict:
        collection = self.db[collection_name]
        data = await collection.find_one({"_id": key_id})
        return data

    async def set_data_by_key(self, collection_name: str, key_id, data) -> None:
        collection = self.db[collection_name]
        await collection.replace_one({"_id": key_id}, data, upsert=True)

