from ninja import Schema


class User(Schema):
    first_name: str
    last_name: str
    cpf: str
    cep: str
    email: str
    password: str
    staff: bool
