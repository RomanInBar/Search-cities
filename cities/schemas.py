from pydantic import BaseModel


class CityGet(BaseModel):
    id: int
    name: str
    latitute: float
    longtitute: float


class CityCreate(BaseModel):
    name: str


class ResponseSchema(BaseModel):
    detail: str


class CoordinatesShema(BaseModel):
    latitute: float
    longtitute: float
