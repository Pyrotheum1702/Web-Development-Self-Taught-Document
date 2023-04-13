from abc import ABC, abstractmethod
from enum import Enum


class AttackMethod(Enum):
    PUNCH = 1
    KICK = 2

# Violate open/closed principle example:


class Human:
    def __init__(self) -> None:
        self.damage = 0

    def set_damage(self, value: int) -> None:
        self.damage = value

    def attack(self, attack_method: AttackMethod) -> None:
        match attack_method:
            case AttackMethod.PUNCH:
                print('Punch:', self.damage)
            case AttackMethod.KICK:
                print('Kick:', self.damage * 1.5)
            case _:
                print('Unknown attack_method!')

# Test section:


duoc = Human()
duoc.set_damage(50)

duoc.attack(AttackMethod.PUNCH)
# Result: Punch: 50

duoc.attack(AttackMethod.KICK)
# Result: Kick: 75.0




# Following open/closed principle example:
class AttackMethodBase(ABC):
    @abstractmethod
    def attack(self, damage: int) -> None:
        pass


class PunchAttackMethod(AttackMethodBase):
    def attack(self, damage: int) -> None:
        print('Punch:', damage)


class KickAttackMethod(AttackMethodBase):
    def attack(self, damage: int) -> None:
        print('Kick:', damage * 1.5)


class Human:
    def __init__(self) -> None:
        self.damage = 0

    def set_damage(self, value: int) -> None:
        self.damage = value

    def attack(self, attack_method: AttackMethodBase) -> None:
        attack_method.attack(self.damage)

# Test section:


duoc = Human()
duoc.set_damage(50)

duoc.attack(PunchAttackMethod())
# Result: Punch: 50

duoc.attack(KickAttackMethod())
# Result: Kick: 75.0
