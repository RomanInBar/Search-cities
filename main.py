from fastapi import FastAPI

from cities.routers import router as city_router


app = FastAPI(
    title='Cities'
)
app.include_router(city_router)
