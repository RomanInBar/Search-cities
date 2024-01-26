from typing import Union

from sqlalchemy.exc import IntegrityError, NoResultFound

from cities.repository import CityRepo
from cities.responses import Response
from cities.schemas import CityCreate, CityGet, CoordinatesShema
from utils.utils import add_coordinates, get_objects

responses: Response = Response()


class CityServices:
    def __init__(self, repository):
        self.repo: CityRepo = repository

    async def get(self, **kwargs) -> Union[CityGet, responses]:
        """Возвращает данные объекта."""
        try:
            city = await self.repo.get(**kwargs)
            return CityGet.model_validate(city, from_attributes=True)
        except NoResultFound:
            return responses.not_found
        finally:
            await self.repo.session.close()

    async def all(self) -> list[CityGet]:
        """Возврщает сипсок данных всех объектов таблицы."""
        try:
            cities = await self.repo.all()
            return [
                CityGet.model_validate(city, from_attributes=True)
                for city in cities
            ]
        except Exception as e:
            return responses.error(e)
        finally:
            await self.repo.session.close()

    async def create(self, data: CityCreate) -> CityGet:
        """Записывает данные нового объекта."""
        try:
            data = data.model_dump()
            city_data = add_coordinates(data)
            city = await self.repo.create(**city_data)
            await self.repo.session.commit()
            return CityGet.model_validate(city, from_attributes=True)
        except IntegrityError:
            return responses.unique
        except AttributeError:
            return responses.invalid
        finally:
            await self.repo.session.close()

    async def delete(self, **kwargs) -> responses:
        """Удаляет данные объекта."""
        try:
            result = await self.repo.delete(**kwargs)
            if not result:
                return responses.not_found
            await self.repo.session.commit()
            return responses.deleted
        except IntegrityError:
            return responses.invalid
        finally:
            await self.repo.session.close()

    async def search(self, data: CoordinatesShema) -> list[CityGet]:
        """Возвращает два ближайших города от точки координат."""
        coordinates = data.model_dump()
        try:
            cities = await self.repo.all()
        except Exception as e:
            return responses.error(e)
        finally:
            await self.repo.session.close()
        cities = get_objects(cities, coordinates)
        return [
            CityGet.model_validate(city, from_attributes=True)
            for city in cities
        ]
