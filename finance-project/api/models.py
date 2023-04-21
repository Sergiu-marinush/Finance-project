from pydantic import BaseModel, Field
from uuid import UUID


class BaseConfig:
    orm_mode = True


class UserAdd(BaseModel):
    username: str = Field(description="Alphanumeric username between 6 and 20 chars")


class AssetInfoCommon(BaseModel):
    ticker: str
    name: str
    country: str


class AssetAdd(BaseModel):
    ticker: str


class AssetInfoUser(AssetInfoCommon):
    units: float

    class Config(BaseConfig):
        pass


class AssetInfoPrice(AssetInfoCommon):
    current_price: float
    currency: str
    today_low_price: float = Field(description="The lowest price reached today")
    today_high_price: float = Field(description="The highest price reached today")
    open_price: float = Field(description="The price at the beginning of the day")
    closed_price: float
    fifty_day_price: float

    class Config(BaseConfig):
        pass


class UserInfo(BaseModel):
    id: UUID
    username: str
    stocks: list[AssetInfoCommon]

    class Config(BaseConfig):
        pass
