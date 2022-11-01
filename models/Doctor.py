
from dataclasses import dataclass

from models.Citizen import Citizen


@dataclass
class Doctor(Citizen):
    type: str = 'Доктор'
    hospital: str = ""
    specialization: str = ""


    def __post_init__(self):
        super().__post_init__()
        addition = [("название больницы", "hospital"), ("специализация", "specialization")]
        self.fields.update(addition)

    def read(self):
        super().read()
        self.hospital = self.io.input('Название больницы:  ')
        self.specialization = self.io.input('Специализация:  ')

    def write(self):
        super().write()
        self.io.output('Название больницы', self.hospital)
        self.io.output('Специализация', self.specialization)