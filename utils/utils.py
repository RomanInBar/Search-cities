from geopy.geocoders import Nominatim

loc = Nominatim(user_agent="GetLoc")


def add_coordinates(data: dict) -> dict:
    """Добавляет координаты к объекту."""
    city = data['name']
    getloc = loc.geocode(city)
    data['latitute'] = getloc.latitude
    data['longtitute'] = getloc.longitude
    return data


def get_objects(objects: list, coordinates: dict) -> list:
    """Возвращает два ближайших объекта от точки координат."""
    latitute = coordinates['latitute']
    longtitute = coordinates['longtitute']
    out = [None, None]
    distance = [float('inf'), float('inf')]
    for index in range(len(objects)):
        lat = objects[index].latitute - latitute
        lon = objects[index].longtitute - longtitute
        d = ((lat**2) + (lon**2)) ** 0.5
        if d == 0:
            continue
        if d < distance[0]:
            distance[0], distance[1] = d, distance[0]
            out[0], out[1] = objects[index], out[0]
        elif d < distance[1]:
            distance[1] = d
            out[1] = objects[index]
        else:
            continue
    return out
