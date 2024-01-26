from cities.services import CityRepo, CityServices
from database.engine import session


def get_services():
    """Возвращает рабочую сессию."""
    service = CityServices(CityRepo(session()))
    return service
