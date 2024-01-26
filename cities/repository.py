from sqlalchemy import delete, insert, select

from cities.models import City


class CityRepo:
    def __init__(self, session):
        self.session = session
        self.model = City

    async def get(self, **kwargs) -> City:
        """Запрос на подучение данных."""
        query = select(self.model).filter_by(**kwargs)
        result = (await self.session.execute(query)).scalar_one()
        return result

    async def create(self, **kwargs) -> City:
        """Запрос на запись данных."""
        stmt = insert(self.model).values(**kwargs).returning(self.model)
        result = (await self.session.execute(stmt)).scalar_one()
        return result

    async def delete(self, **kwargs) -> bool:
        """Запрос на удаление данных."""
        stmt = delete(self.model).filter_by(**kwargs)
        result = await self.session.execute(stmt)
        return bool(result.rowcount)

    async def all(self) -> list[City]:
        """Запрос на получение данных всех объектов таблицы."""
        query = select(self.model)
        result = (await self.session.execute(query)).scalars().all()
        return result
