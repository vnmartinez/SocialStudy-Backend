from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    database_url:str 
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int
    model_config=SettingsConfigDict(env_file=".env")
    
config = Config()