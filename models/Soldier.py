from models.Citizen import Citizen
from dataclasses import dataclass




@dataclass
class Soldier(Citizen):
    type: str = 'Солдат'
    military_unit: str = ""
    rank: str = ""


    def __post_init__(self):
        super().__post_init__()
        addition = [("военная часть", "military_unit"), ("звание", "rank")]
        self.fields.update(addition)

    def read(self):
        super().read()
        self.military_unit = self.io.input('Военная часть:  ')
        self.rank = self.io.input('Звание:  ')

    def write(self):
        super().write()
        self.io.output('Военная часть', self.military_unit)
        self.io.output('Звание', self.rank)