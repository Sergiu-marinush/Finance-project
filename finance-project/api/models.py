from pydantic import BaseModel, Field
from uuid import UUID


class BaseConfig:
    orm_mode = True


class UserAdd(BaseModel):
    username: str = Field(description="Alphanumeric username between 6 and 20 chars")


class AssetInfoCommon(BaseModel):
    ticker: str = Field(description="A ticker symbol or stock symbol is an abbreviation"
                                    " used to uniquely identify publicly traded shares of a particular"
                                    " stock on a particular stock market.")
    name: str = Field(description="The name of the company")
    country: str = Field(description="The country where the company's headquarters are located")


class AssetAdd(BaseModel):
    ticker: str


class AssetInfoUser(AssetInfoCommon):
    units: float = Field(description="The amount of units the user has from that particular asset")

    class Config(BaseConfig):
        pass


class AssetInfoPrice(AssetInfoCommon):
    current_price: float = Field(description="Assets's current price")
    currency: str = Field(description="The symbol for that particular asset")
    today_low_price: float = Field(description="The lowest price reached today")
    today_high_price: float = Field(description="The highest price reached today")
    open_price: float = Field(description="The price at the beginning of the day")
    closed_price: float
    fifty_day_price: float

    class Config(BaseConfig):
        pass


class UserInfo(BaseModel):
    id: UUID = Field(description="Unique id for a user")
    username: str = Field(description="Alphanumeric username between 6 and 20 chars")
    stocks: list[AssetInfoCommon] = Field(description="A list of stocks relating to a specific user")

    class Config(BaseConfig):
        pass
