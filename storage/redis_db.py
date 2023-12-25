from redis import from_url as redis_from_url


class RedisDataBase:
    def __init__(self, redis_url: str):
        self.db = redis_from_url(redis_url)

    async def close_redis_connection(self) -> None:
        self.db.close()
        await self.db.wait_closed()

    async def get_data_by_key(self, key_id: str) -> str:
        data: str = await self.db.get(key_id)
        await self.close_redis_connection()

        return data

    async def set_data_by_key(self, key_id, data) -> None:
        await self.db.set(key_id, data)
