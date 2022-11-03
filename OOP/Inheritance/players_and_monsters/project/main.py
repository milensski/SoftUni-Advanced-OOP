from project.elf import Elf
from project.hero import Hero
from project.soul_master import SoulMaster

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
sould_wizard = SoulMaster('S', 190)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
print(elf.__class__.mro())
print(sould_wizard.__class__.mro())