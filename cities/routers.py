from typing import Union

from fastapi import APIRouter, Depends

from cities.depends import CityServices, get_services
from cities.schemas import (CityCreate, CityGet, CoordinatesShema,
                            ResponseSchema)

router = APIRouter(prefix='/cities', tags=['City'])


@router.get(
    '/{pk:int}',
    response_model=Union[CityGet, ResponseSchema],
    summary='Получить данные о городе',
)
async def get(pk: int, service: CityServices = Depends(get_services)):
    response = await service.get(id=pk)
    return response


@router.get(
    '/',
    response_model=Union[list[CityGet], ResponseSchema],
    summary='Получить данные о всех городах',
)
async def get_all(service: CityServices = Depends(get_services)):
    response = await service.all()
    return response


@router.post(
    '/',
    response_model=Union[CityGet, ResponseSchema],
    summary='Создать новую запись',
)
async def create(
    data: CityCreate, service: CityServices = Depends(get_services)
):
    response = await service.create(data)
    return response


@router.delete(
    '/{pk:int}', response_model=ResponseSchema, summary='Удалить запись'
)
async def delete(pk: int, service: CityServices = Depends(get_services)):
    response = await service.delete(id=pk)
    return response


@router.post(
    '/search', response_model=list[CityGet], summary='Поиск ближайших городов'
)
async def search(
    data: CoordinatesShema, service: CityServices = Depends(get_services)
):
    response = await service.search(data)
    return response
