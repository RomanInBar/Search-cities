# Search-cities
## Описание
Приложение по поиску двух ближайших городов от заданной точки координат.  
При запросе к API на добавление нового города клиент указывает только название города, а в хранилище добавляются также координаты.  
Функционал:  
 - добавлять/удалять в хранилище информацию о городах (название)  
 - запрашивать информацию о городах из хранилища  
 - по заданным широте и долготе точки выдаёт 2 ближайших к ней города из присутствующих в хранилище

#### Стэк:
Python 3.11;  
FasAPI;  
SQLAlchemy;  
PostgreSQL;  
Alembic;  
Docker;  
docker-compose  

## Шаблон env файла
DRIVER: str  
USER: str  
DB_PASS: str  
DB_HOST: str  
DB_PORT: str  
DB_NAME: str  
POSTGRES_PASSWORD: str  
POSTGRES_USER: str  

##
Документация API: https://search-cities-i5t1.onrender.com/docs