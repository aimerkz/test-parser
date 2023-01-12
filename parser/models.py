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


class BaseInputPars(BaseModel):
    description: str
    employment: str
    address: Address
    name: str
    salary: Salary
    contacts: Contacts
