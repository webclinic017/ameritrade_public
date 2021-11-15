from pydantic import BaseModel, Field
from datetime import datetime


class UserList(BaseModel):
    id: str
    username: str
    password: str
    first_name: str
    last_name: str
    gender: str
    create_at: str
    status: str


class UserEntry(BaseModel):
    username: str = Field(..., example="potinejj")
    password: str = Field(..., example="potinejj")
    first_name: str = Field(..., example="Potine")
    last_name: str = Field(..., example="Sambo")
    gender: str = Field(..., example="M")


class UserUpdate(BaseModel):
    id: str = Field(..., example="Enter your id")
    first_name: str = Field(..., example="Potine")
    last_name: str = Field(..., example="Sambo")
    gender: str = Field(..., example="M")
    status: str = Field(..., example="1")


class UserDelete(BaseModel):
    id: str = Field(..., example="Enter your id")


class InsertDataIntoRegisterOfActions(BaseModel):
    symbol: str = Field(..., example="AAPL")
    candle_date: datetime = Field(..., example="2021-04-23 10:20")
    open_value: float = Field(..., example="30.1")
    close_value: float = Field(..., example="20.9")
    action_type: str = Field(..., example="call condition 5")
    call_or_put: str = Field(..., example="call")
    strike: float = Field(..., example="Strike value")
    ask_price: float = Field(..., example="90.3")
    bid_price: float = Field(..., example="91.2")
    status_of_action: str = Field(..., example="on posession")
    order_date: datetime = Field(..., example="2021-04-23 10:21")
