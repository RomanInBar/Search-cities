from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DRIVER: str
    USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    @property
    def URL(self):
        return (
            f'{self.DRIVER}://{self.USER}:{self.DB_PASS}'
            f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )

    class ConfigDict:
        env_file = '.env'


settings = Settings()
