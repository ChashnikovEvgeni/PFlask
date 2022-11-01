from dataclasses import dataclass, field

from IO.ConsoleIO import ConsoleIO



@dataclass
class Citizen:
    type: str = 'Житель'
    fields: dict = None
    id: int = 0
    first_name: str = ""
    last_name: str = ""
    age: int = 0

    def __post_init__(self):
        self.io = ConsoleIO()
        self.fields = {"id": "id", "имя": "first_name", "фамилия": "last_name", "возраст": "age"}

    def read(self):
        self.first_name = self.io.input('Имя:  ', )
        self.last_name = self.io.input('Фамилия: ', )
        self.age = self.io.input('Возраст:  ', self.__dataclass_fields__['age'].type)

    def write(self):
        self.io.output(self.type)
        self.io.output('ID', self.id)
        self.io.output('Имя', self.first_name)
        self.io.output('Фамилия', self.last_name)
        self.io.output('Возраст', self.age)
