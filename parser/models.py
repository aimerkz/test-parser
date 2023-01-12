from pydantic import BaseModel, Field


class Address(BaseModel):
    value: str


class Salary(BaseModel):
    from_: int = Field(alias='from')
    to: int


class Contacts(BaseModel):
    fullName: str
    phone: str
    email: str


class BasePars(BaseModel):
    address: Address
    allow_messages: bool = True
    billing_type: str = 'packageOrSingle'
    business_area: int = 1
    contacts: Contacts
    description: str
    employment: str
    name: str
    salary: Salary
