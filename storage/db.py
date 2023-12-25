from typing import runtime_checkable, Protocol


@runtime_checkable
class DataBaseInterface(Protocol):
    async def get_data_by_key(self, key_id: str) -> str:
        ...

    async def set_data_by_key(self, key_id, data) -> None:
        ...


def get_database_interface(db: DataBaseInterface, url: str) -> DataBaseInterface:
    return db(url)
