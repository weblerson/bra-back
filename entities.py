class User:

    def __init__(self):
        self.first_name: str
        self.last_name: str
        self.cpf: str
        self.cep: str
        self.email: str
        self.password: str
        self.staff: bool

    def from_json(self, json):
        self.first_name: str = json.get('first_name')
        self.last_name: str = json.get('last_name')
        self.cpf: str = json.get('cpf')
        self.cep: str = json.get('cep')
        self.email: str = json.get('email')
        self.password: str = json.get('password')
        self.staff: bool = json.get('staff')

    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'cpf': self.cpf,
            'cep': self.cep,
            'email': self.email,
            'password': self.password,
            'staff': self.staff
        }
