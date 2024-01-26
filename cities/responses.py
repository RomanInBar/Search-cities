class Response:
    """Класс с вариантами ответа на действия пользователя."""

    @property
    def not_found(self):
        return {'detail': 'Объект не найден'}

    @property
    def deleted(self):
        return {'detail': 'Объект удалён'}

    @property
    def invalid(self):
        return {'detail': 'Введены невалидные данные'}

    @property
    def unique(self):
        return {'detail': 'Данные уже существуют'}

    @staticmethod
    def error(error):
        return {'detail': f'Произошла ошибка: {error}'}
