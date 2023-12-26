from typing import runtime_checkable, Protocol


@runtime_checkable
class DataBaseInterface(Protocol):
    """
    Interface for DB operations.
    """

    async def get_data_by_key(self, key_id: str) -> str:
        ...

    async def set_data_by_key(self, key_id, data) -> None:
        ...


def get_database_interface(db: DataBaseInterface, url: str) -> DataBaseInterface:
    """
    Make a database.
    :param db: your db
    :param url: url for connecting to db
    :return: database interface
    """
    return db(url)
