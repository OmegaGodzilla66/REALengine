import masters
import random
class Entity:
    def __init__(self,name,AC,HP,initiative,actions):
        """ACTIONS FORMATTING
        [[toHitBonus,damageDie (xdx),damagebonus],[etc]"""
        self.name=name

        self.ac=AC
        self.hp=HP
        self.initiative=initiative

        self.actions=actions
        self.dice=masters.DiceMaster()

    def initiate(self):
        return self.dice.d20() + self.initiative

    def take_action(self,targets,combatmaster):
        """Everything is random by default"""
        action=self.action_select(targets, combatmaster)

        # now have list of [combatAction, target]

        # To Hit
        print("ACT:")
        print(action)
        if combatmaster.hits(action[1],self.dice.d20()+action[0][0]):
            print("HIT")
            damageDie=action[0][1].split('d')
            damageDie[0]=int(damageDie[0])
            damageDie[1]=int(damageDie[1])
            damage=0
            for i in range(damageDie[0]):
                damage+=random.randint(0,damageDie[1])

            damage+=action[0][2]
            print(f"You hit for {damage} damage")
            combatmaster.updateHealth(action[1],damage)

        else:
            print("MISS - No damage")
            pass







    def action_select(self, targets, combatmaster):
        """This is purposly random to allow for user inheratince later"""
        selection=[random.choice(self.actions), random.choice(targets)]
        return selection


