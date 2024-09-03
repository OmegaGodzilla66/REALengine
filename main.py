from entityclass import Entity
from masters import CombatMaster
print("COMBAT TEST")

enemy1=Entity("Enemy 1",12, 15, 1, [[2,'1d4',2],[3,'1d6',1]])

enemy2=Entity('Enemy 2', 11, 20, 1, [[2,'1d4',2],[3,'1d6',1]])

CM= CombatMaster([enemy1,enemy2])

CM.startEncounter()