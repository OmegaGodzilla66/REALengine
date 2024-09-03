import random

class CombatMaster:
    def __init__(self,userList):
        """UserList not ordered by default CM runs combat initiative"""
        self.userList = userList

    def startEncounter(self):
        print("PRINTS ON")
        for x in self.userList:
            initiative=x.initiate()

        # get in proper order

        for i in self.userList:
            for i in self.userList:
                print(f"{i.name}: {i.hp} remaining")
            input("Press enter to continue\n> ")
            i.take_action(self.userList,self)


    def updateHealth(self,target,damage):
        index=self.userList.index(target)

        self.userList[index].hp-=damage

    def hits(self,target,tohit):
        if self.userList[self.userList.index(target)].ac <= tohit:
            return True
        else:
            return False

class DiceMaster:
    def __init__(self):
        pass

    def d20(self):
        return random.randint(1,20)

    def d10(self):
        return random.randint(1,10)

    def d8(self):
        return random.randint(1,8)

    def d6(self):
        return random.randint(1,6)

    def d4(self):
        return random.randint(1,4)