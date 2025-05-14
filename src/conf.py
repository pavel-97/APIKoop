from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str

    POSTGRES_USER_TEST: str
    POSTGRES_DB_TEST: str
    POSTGRES_PASSWORD_TEST: str
    POSTGRES_HOST_TEST: str

    MODE: str

    @property
    def database_url(self):
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}/{self.POSTGRES_DB}"
        )
    
    @property
    def database_url_test(self):
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER_TEST}:{self.POSTGRES_PASSWORD_TEST}"
            f"@{self.POSTGRES_HOST_TEST}/{self.POSTGRES_DB_TEST}"
        )


settings = Settings()
