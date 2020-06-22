
from Scripts.game_name.game import Game
class HouYi(Game):

    def __init__(self):
        # 不加的话会导致子类中的init覆盖父类中的init
        super().__init__()
        self.denfense = 100

    def denfense1(self,enemy_hp,enemy_power):
        # while True:
            self.hp = self.hp + self.denfense - enemy_power
            enemy_hp = enemy_hp - self.power
            print("我的血量是：",self.hp)
            print("敌人的血量是：",enemy_hp)
            if self.hp > enemy_hp:
                print("我赢了")
            elif enemy_hp < self.hp:
                print("敌人赢了")
            else:
                raise Exception("No peace,keep fighting")



houyi = HouYi()
houyi.denfense1(1000,300)