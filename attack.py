import random


class Enemy:
    atkl = 60
    atkh = 80

    # 'self' is the entire object of this class
    # 'self' is analogous to 'this'
    def getAtk(self):
        print(self.atkl)

enemy1 = Enemy()    # creating object of Enemy classs
enemy1.getAtk()

enemy2 = Enemy()
enemy2.getAtk()
'''

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for", dmg, "points of change. Current HP is", playerhp)

    if playerhp > 30:
        continue

    print("You have low health: You have been teleported to somewhere else")
    break

'''