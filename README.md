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
DRIVER  
USER  
DB_PASS  
DB_HOST  
DB_PORT    
DB_NAME    
POSTGRES_PASSWORD    
POSTGRES_USER   

##
Документация API: https://search-cities-i5t1.onrender.com/docs