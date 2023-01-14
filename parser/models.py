from pydantic import BaseModel, Field, root_validator


class Address(BaseModel):
    value: str
    lat: float
    lng: float


class Salary(BaseModel):
    from_: int = Field(alias='from')
    to: int


class Phone(BaseModel):
    city: str
    country: str
    number: str


class Contacts(BaseModel):
    email: str
    fullName: str = Field(alias='name')
    phone: Phone

    class Config:
        allow_population_by_field_name = True

    @root_validator(pre=True)
    def validate_phone(cls, values):
        phone = values['phone']
        city = phone[1:4]
        country = phone[0]
        number = phone[4:]
        number = number[0:3] + '-' + number[3:5] + '-' + number[5:]
        values['phone'] = {'city': city, 'country': country, 'number': number}
        return values


class BasePars(BaseModel):
    address: Address
    allow_messages: bool = True
    billing_type: str = 'packageOrSingle'
    business_area: int = 1
    contacts: Contacts
    description: str
    experience: str = {'id': 'noMatter'}
    html_tags: bool = True
    image_url: str = 'https://img.hhcdn.ru/employer-logo/3410666.jpeg'
    name: str
    salary: Salary
    employment: str = Field(alias='shelude')

    class Config:
        allow_population_by_field_name = True

    @root_validator()
    def validate_base(cls, values):
        lat = values['address'].lat
        lng = values['address'].lat
        values['employment'] = {'id': values['employment']}
        values['salary_range'] = {'from': values['salary'].from_, 'to': values['salary'].to}
        values['salary'] = values['salary'].to
        values['coordinates'] = {'latitude': lat, 'longitude': lng}
        values['address'] = values['address'].value
        return values
